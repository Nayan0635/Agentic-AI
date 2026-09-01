import cv2
from random import randint
#create a camera Object
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64
load_dotenv()
client = OpenAI(
     api_key=os.getenv("OPENAI_API_KEY")
)
print("Connected to OpenAI")

camera = cv2.VideoCapture(0)
print("Press Enter or Space to Capture The Image")

 
while True:
 success,frame = camera.read()
 if not success:
        #print("Error Opening WebCamera")
        break
   
 cv2.imshow("WebCam",frame)
 key = cv2.waitKey(1)

 if key == 13 or key==32:
     #Save The image
        filename = 'capture-'+str(randint(1000,9999))+".jpg"
        cv2.imwrite(filename,frame)
        print("Image Captured successfully")
        #Closing camera
        camera.release()
        #Closing the webCam window
        cv2.destroyAllWindows()
        #We need to convert Image File to Binaries
        with open(filename,"rb") as img:
              
             base64Image = base64.b64encode(img.read()).decode("utf-8")
        #Asking from the user's end
        user_input = input("Ask Something related to Image:")
        if user_input.lower()=='exit':
             print("Agent :Bye Bye")
             exit(0)
        #We will call LLM i.e openAI for analysis the image
        responses = client.chat.completions.create(
             model="gpt-4.1-mini",
             messages=[
                  {
                       "role":"user",
                       "content":[
                            {
                                 "type":"text",
                                 "text":f'''
                               -You are an Image Ananlysis AI
                               -Who can tell no of Persons
                               -Person details 
                               -Object Identifications
                               -Facial Expression
                               -Answer user's Question:{user_input}
                               
                               '''
                            },
                            {
                                 "type":"image_url",
                                 "image_url":{
                                      "url":f"data:image/jpeg;base64,{base64Image}"
                                 }
                            }
                       ]
                  }
             ]
        )
        message = responses.choices[0].message.content
        print("Agent Reply :",message)

        
    