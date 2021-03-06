from typing import Text
import speech_recognition as sr
import os
from gtts import gTTS
import playsound

credential_path = "api_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

r = sr.Recognizer()

def ava(audio_string):
    tts = gTTS(text=audio_string, lang="en", tld='ie')
    file = "output_audio.mp3"
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)


def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that")
        except sr.RequestError:
            print("Sorry, My services are down")

        return voice_data


print("How can I help you?")
voice_data = get_audio()
ava(voice_data)
print(voice_data)