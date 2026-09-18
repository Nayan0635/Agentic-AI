from google import genai
from google.genai import types
import cv2 #to capture image from webcam
import base64 # to convert image to binary
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()

client = genai(
    api_key = os.getenv("gemini_key")
)
# this 
camera = cv2.VideoCapture(0) # open the camera
print('Press [Enter] or [Space] to capture')

while True:
    success, frame = camera.read()
    if not success:
        print("Error Opening Camera")
        break
    cv2.imshow("WebCame", frame)
    key = cv2.waitkey(1)
    
    if key == 13 or key == 32:
        filename = 'img-' + str(randint(1000, 9999)) + ".jpg"
        cv2.imwrite(filename, frame)
        print("Image captured successfully")
        
        camera.release() #close camera
        cv2.destroyAllWindows()
        
        with open(filename, "rb") as img:
            image_bytes = img.read()
        
        user_input = input("ask me about image: ")
        if user_input.lower() == 'exit':
            print("Agent: Cya!")
            exit(0)
        
        prompt =  f"""
            - You are an Image Analysis AI
            - Tell number of persons
            - Person details
            - Object Identifications
            - Facial Expression
            - Answer user's Question: {user_input}
        """
        
        response = client.models.generate_content(
            model = 'gemini-2.5-flash',
            contents = [
                types.Part.from_bytes(
                    data = image_bytes,
                    mime_type= "image/jpeg"
                ),
                prompt
            ]
        )
print("Agent: ", response.text)
        