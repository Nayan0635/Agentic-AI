import smtplib as send
from email.mime.text import MIMEText
from langchain.tools import tool
from dotenv import load_dotenv
import os


load_dotenv()

@tool
def sendMail(receiver, subject, body):
    '''send mail to recipent'''
    
    message = MIMEText(body)
    
    sender = os.getenv("mail")
    password = os.getenv("pwd")
    
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    
    try:
        with send.SMTP("smtp.gmail.com", 587) as server: #XXX📞 Connect to Gmail
            # start the local smtp server to send the mail
            server.starttls()
            #XXX🔑 tell who you are ..login there
            server.login(sender, password)
            server.send_message(message)
    
    except Exception as e:
        print("Error sending your mail: ", e)
        return str(e)
    
    finally:
        return 'Email sent succefully.'