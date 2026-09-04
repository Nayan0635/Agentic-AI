# gemini->python

from google import genai
import cv2
import base64
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()

client = genai(
    api_key = os.getenv("gemini_key")
)

camera = cv2.VideoCapture(0) # open the camera
print('Press [Enter] or [Space] to capture')

