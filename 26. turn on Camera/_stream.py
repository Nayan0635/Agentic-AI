import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.title("Image Analysis AI")

# Camera section
image = st.camera_input("Camera")

if image is not None:

    # Show captured image only once
    st.image(image, caption="Captured Image")

    # Query section
    user_input = st.text_input("Ask something about the image:")

    # Analyze button
    if st.button("Capture Image"):

        if user_input.strip() == "":
            st.warning("Please enter a question.")

        else:
            # Convert image to base64
            image_bytes = image.getvalue()
            base64Image = base64.b64encode(image_bytes).decode("utf-8")

            # Send image + query to OpenAI
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"""
                                        You are an Image Analysis AI.

                                        You can:
                                        - Tell the number of persons
                                        - Identify objects
                                        - Describe visible person details
                                        - Identify facial expressions
                                        - Answer questions about the image

                                        Answer the user's question:{user_input}"""
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64Image}"
                                }
                            }
                        ]
                    }]
            )

            message = response.choices[0].message.content

            st.subheader("Agent Reply")
            st.write(message)