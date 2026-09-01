import smtplib
from email.mime.text import MIMEText
from langchain.tools import tool
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def sendMail(receiver:str,subject:str,body:str)->str:
    '''sending email to recipents'''
    message = MIMEText(body)
    sender = os.getenv("mail")
    password = os.getenv("mail_pwd")

    message['Subject'] = subject
    message['From']    = sender
    message['To']      = receiver
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as server: 
            #start the local smtp server in order to send mail
            server.starttls()
            #login using cridentials
            server.login(sender,password) 
            server.send_message(message) 
            return 'Email sent successfully'
    except Exception as ex:
        print("Error sending email:", ex)
        return str(ex)
    

