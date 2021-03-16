import random
from dotenv import load_dotenv
load_dotenv()
import os
import smtplib

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

security_code = random.randint(100, 100000)

def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email, password)

    subject = "Your verification code to login"
    body = "Hey this your verification code {}".format(security_code)
    message = "Subject: {}".format(subject) + " \n\n {}".format(body)
    server.sendmail(email,email, message)
    print("EMAIL HAS BEEN SENT!")
send_email()


