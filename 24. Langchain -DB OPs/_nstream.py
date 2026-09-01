# import streamlit as st
# from langchain_nvidia_ai_endpoints import ChatNVIDIA
# from dotenv import load_dotenv
# import os
# from tools import *

# load_dotenv()

# # connect to llm
# llm = ChatNVIDIA(
#     api_key=os.getenv("nvidia_key"),
#     model="meta/muse-glimmer-30b",
#     temperature=1,
#     top_p=0.95,
#     max_completion_tokens=8192
# )

# # binding the llm with specified tools
# llm = llm.bind_tools([
#     addNewUser,
#     getUser,
#     getAllUsers,
#     deleteUser,
#     updateUser
# ])

# tools_by_name: dict = {
#     "addNewUser": addNewUser,
#     "getAllUsers": getAllUsers,
#     "getUser": getUser,
#     "deleteUser": deleteUser,
#     "updateUser": updateUser
# }


# st.title("DB Agent")

# textArea = st.text_area("Question :")
# sendBtn = st.button("Submit")

# if sendBtn:

#     responses = llm.invoke(f'''
#     Prompt : {textArea}
#     ''')

#     if responses.tool_calls:

#         tool_name = responses.tool_calls[0]["name"]
#         tool_args = responses.tool_calls[0]["args"]

#         st.write("Agent is using tool :", tool_name)

#         result = tools_by_name.get(tool_name).invoke(tool_args)

#         st.write("Agent Response :", result)

#     else:
#         st.write("Agent : Sorry I cann't help with that.")

'''nvidia'''
import streamlit as st

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

import os

from tools import *


# PAGE CONFIG

st.set_page_config(
    page_title="DB Agent",
    page_icon="🤖",
    layout="centered"
)


# CUSTOM CSS

st.html("""
<style>

    .stApp {
        background:
            radial-gradient(circle at top left, #1e1b4b, transparent 35%),
            radial-gradient(circle at bottom right, #172554, transparent 35%),
            #0f172a;
    }

    .block-container {
        max-width: 850px;
        padding-top: 40px;
    }

    /* HERO */
    .hero {
        text-align: center;
        padding: 30px 20px 35px;
    }

    .hero-icon {
        font-size: 60px;
        margin-bottom: 8px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 800;
        color: #a78bfa;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 16px;
        line-height: 1.6;
    }

    /* INPUT TITLE */
    .section-title {
        font-size: 22px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 12px;
    }

    /* BUTTON */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(
            90deg,
            #6366f1,
            #8b5cf6
        );
        color: white;
        font-size: 17px;
        font-weight: 700;
    }

    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #4f46e5,
            #7c3aed
        );
        color: white;
    }

    /* TOOL CARD */
    .tool-card {
        margin-top: 25px;
        padding: 20px;
        border-radius: 16px;
        background: rgba(99, 102, 241, 0.12);
        border: 1px solid rgba(139, 92, 246, 0.3);
    }

    .tool-name {
        color: #c4b5fd;
        font-size: 18px;
        font-weight: 700;
    }

    .tool-description {
        color: #94a3b8;
        margin-top: 6px;
    }

    /* RESPONSE */
    .response-card {
        margin-top: 20px;
        padding: 20px;
        border-radius: 16px;
        background: rgba(16, 185, 129, 0.08);
        border: 1px solid rgba(16, 185, 129, 0.25);
    }

    .response-title {
        color: #6ee7b7;
        font-size: 20px;
        font-weight: 700;
    }

</style>
""")


# CONNECT TO LLM

load_dotenv()

llm = ChatNVIDIA(
    api_key=os.getenv("nvidia_key"),
    model="meta/muse-glimmer-30b",
    temperature=1,
    top_p=0.95,
    max_completion_tokens=8192
)


# BIND TOOLS

llm = llm.bind_tools([
    addNewUser,
    getUser,
    getAllUsers,
    deleteUser,
    updateUser
])


tools_by_name = {
    "addNewUser": addNewUser,
    "getAllUsers": getAllUsers,
    "getUser": getUser,
    "deleteUser": deleteUser,
    "updateUser": updateUser
}


# HERO

st.html("""
<div class="hero">

    <div class="hero-icon">🤖</div>

    <div class="hero-title">
        DB Agent
    </div>

    <div class="hero-subtitle">
        AI-powered database assistant<br>
        Ask questions and let the agent manage your database.
    </div>

</div>
""")


# QUESTION

st.html("""
<div class="section-title">
    💬 Ask your database
</div>
""")

textArea = st.text_area(
    "Question",
    placeholder="""Try something like:

• Show all users
• Find user with ID 5
• Add a new user
• Delete user 3
• Update user 2""",
    height=160,
    label_visibility="collapsed"
)


sendBtn = st.button("🚀  Run Agent")


# AGENT

if sendBtn:

    if not textArea.strip():

        st.warning("Please enter a question first.")

    else:

        with st.spinner("🧠 Agent is thinking..."):

            responses = llm.invoke(
                f"""
                Prompt : {textArea}
                """
            )

        if responses.tool_calls:

            tool_name = responses.tool_calls[0]["name"]
            tool_args = responses.tool_calls[0]["args"]

            st.html(f"""
            <div class="tool-card">

                <div class="tool-name">
                    🔧 Using tool: {tool_name}
                </div>

                <div class="tool-description">
                    The AI selected this database operation.
                </div>

            </div>
            """)

            tool = tools_by_name.get(tool_name)

            if tool:

                result = tool.invoke(tool_args)

                st.html("""
                <div class="response-card">

                    <div class="response-title">
                        ✨ Agent Response
                    </div>

                </div>
                """)

                st.write(result)

        else:

            st.warning(
                "🤔 Sorry, I couldn't find a suitable database operation."
            )


# FOOTER

st.html("""
<div style="
    text-align:center;
    color:#64748b;
    margin-top:40px;
    padding-bottom:20px;
    font-size:13px;
">
    Powered by LangChain + NVIDIA AI 🚀
</div>
""")