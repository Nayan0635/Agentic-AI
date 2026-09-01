import cv2
from random import randint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

# Connect to Gemini
client = ChatGoogleGenerativeAI(
    api_key=os.getenv("gemini_key"),
    model="gemini-2.5-flash"
)
print("Connected to Gemini")
# Create a camera object
camera = cv2.VideoCapture(0)
print("Press Enter or Space to Capture The Image")

while True:
    success, frame = camera.read()

    if not success:
        break
    cv2.imshow("WebCam", frame)
    key = cv2.waitKey(1)

    if key == 13 or key == 32:
        # Save the image
        filename = "capture-" + str(randint(1000, 9999)) + ".jpg"
        cv2.imwrite(filename, frame)
        print("Image Captured successfully")
        # Closing camera
        camera.release()
        # Closing the webcam window
        cv2.destroyAllWindows()
        # Convert image to Base64
        with open(filename, "rb") as img:
            base64Image = base64.b64encode(img.read()).decode("utf-8")
        # Ask the user
        user_input = input("Ask Something related to Image: ")

        if user_input.lower() == "exit":
            print("Agent: Bye Bye")
            exit(0)

        # Send image + question to Gemini
        response = client.invoke([
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""
You are an Image Analysis AI.

You can:
- Tell the number of persons
- Describe persons
- Identify objects
- Analyze facial expressions
- Answer questions about the image

Answer the user's question:

{user_input}
"""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64Image}"
                        }
                    }
                ]
            }
        ])

        print("Agent Reply:", response.content)

        break
