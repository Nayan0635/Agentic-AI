from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template('''
    -You are a Python Teacher who can only answer related to Python
    -Apart from that Please Say I can't help .
    -Question :{question}
''')