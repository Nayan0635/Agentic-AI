import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("gemini_key"),
    model="gemini-3.1-flash-lite",
    temperature=1
)

st.title("Image Analysis AI")

# Camera section
image = st.camera_input("Camera")

if image is not None:

    # Show captured image
    st.image(image, caption="Captured Image")

    # Query section
    user_input = st.text_input("Ask something about the image:")

    # Analyze button
    if st.button("click"):

        if user_input.strip() == "":
            st.warning("Please enter a question.")

        else:

            # Convert image to base64
            image_bytes = image.getvalue()
            base64Image = base64.b64encode(image_bytes).decode("utf-8")

            # Send image + query to Gemini
            response = llm.invoke([
                {
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

            message = response.content

            st.subheader("Agent Reply")
            st.write(message)
            
# python -m streamlit run _gstream.py