import random
from dotenv import load_dotenv
load_dotenv()
import os


os.getenv("SECURITY_CODE") = random.randint(100, 10000) 


