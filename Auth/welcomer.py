import random
from dotenv import load_dotenv
load_dotenv()
import os
import smtplib
import datetime

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

def login():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12: 
        morning = "Good Morning"    
    elif hour>=12 and hour<18:
        afternoon = "Good Afternoon!"   
    else:
        evening = "Good Evening!"
    print("Your security code has been sent to your inbox")
    send_email()
    user_input = input("Enter your code: ")
    if user_input == security_code:
        print("Valid Security Code")
    else:
        print("Invalid Security")
login()




