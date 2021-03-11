import speech_recognition as sr
import os
from gtts import gTTS
import playsound
from nlp import nlp
import datetime

# init packages
r = sr.Recognizer()

# text to speech    
def ava(audio_string):
    tts = gTTS(text=audio_string, lang="en", tld='ie')
    file = "output_audio.mp3"
    tts.save(file)
    playsound.playsound(file) 
    os.remove(file)
    
# wish user good morning 

def wish():
    greeted = False
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 9:
        greeted = False
        ava("Good Morning, Shashank did you have a great night sleep")
    else:
        greeted = True
        pass
wish()
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
voice_data = get_audio()
nlp(voice_data)

# print what the user said 
print(voice_data)