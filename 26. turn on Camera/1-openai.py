from openai import OpenAI
import cv2
from random import randint
from dotenv import load_dotenv
import os
import base64
load_dotenv()
client = OpenAI(
     api_key=os.getenv("openai_key")
)
print("Connected to OpenAI")

camera = cv2.VideoCapture(0)
print("Press Enter or Space to Capture The Image")

 
while True:
     success,frame = camera.read()
     if not success:
          print("Error Opening WebCamera")
          break
     cv2.imshow("WebCam",frame) #shows the camera window
     key = cv2.waitKey(1) # waits for a key to be pressed

     if key == 13 or key==32: #Save The image
          filename = 'capture-'+str(randint(1000,9999))+".jpg"
          cv2.imwrite(filename,frame)
          print("Image Captured successfully")
          camera.release()#Closing camera
          cv2.destroyAllWindows()#Closing the webCam window
          with open(filename,"rb") as img:#We need to convert Image File to Binaries
               base64Image = base64.b64encode(img.read()).decode("utf-8")
          user_input = input("Ask Something related to Image:")
          if user_input.lower()=='exit':
               print("Agent :Bye Bye")
               exit(0)
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
                                   -Answer user's Question:{user_input}'''
                              },
                              {
                                   "type":"image_url",
                                   "image_url":{"url":f"data:image/jpeg;base64,{base64Image}"}
                              }
                         ]
                    }
               ]
          )
message = responses.choices[0].message.content
print("Agent Reply :",message)

        
    