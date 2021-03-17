import random
from dotenv import load_dotenv
load_dotenv()
import os
import smtplib

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

security_code = int(random.randint(100, 100000))

def send_email():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email, password)

    subject = "Your verification code to login"
    body = "Hey this your verification code {}".format(security_code)
    message = f"Subject: {subject} \n\n {body}"
    server.sendmail(email,email, message)
    print("EMAIL HAS BEEN SENT!")

def login():
    needs_to_login = True
    if needs_to_login == True:   
        print("Your security code has been sent to your inbox")
        send_email()
        user_input = input("Enter your code: ")
        if int(user_input) == int(security_code):
            print("Valid Security Code")
            needs_to_login = False
        else:
            print("Invalid Security")
            needs_to_login = True
            login()
    else:
        needs_to_login = False

