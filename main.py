# libs 
import speech_recognition as sr
import os
import datetime
from gtts import gTTS
import playsound
import datetime
# my files 
from nlp import nlp
from Auth.welcomer import *

# init packages
r = sr.Recognizer()

credential_path = "api_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# text to speech    
def ava(audio_string):
    tts = gTTS(text=audio_string, lang="en", tld='ie')
    file = "output_audio.mp3"
    tts.save(file)
    playsound.playsound(file) 
    os.remove(file)
    
# speech recognition
def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Sorry, My services are down")

        return voice_data

    
# calling these functions
login()
ava("How can I help you?")
voice_data = get_audio()
nlp(voice_data)

# print what the user said 
print(voice_data)