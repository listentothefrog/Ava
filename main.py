# import libs
from typing import Text
import speech_recognition as sr
import os
from gtts import gTTS
import playsound
from google.cloud import language_v1

# api keys access
credential_path = "api_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# init packages
r = sr.Recognizer()
client = language_v1.LanguageServiceClient()

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
            print("Sorry, I didn't understand that")
        except sr.RequestError:
            print("Sorry, My services are down")

        return voice_data

print("How can I help you?")

# anlayze text using nlp
def nlp(text):
    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entity_sentiment(request = {'document': document, 'encoding_type': encoding_type})

    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))
        
        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

        
        sentiment = entity.sentiment
        print(u"Entity sentiment score: {}".format(sentiment.score))
        
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{} = {}".format(metadata_name, metadata_value))

    print(u"Language of the text: {}".format(response.language))


# calling these functions
voice_data = get_audio()
ava(voice_data)
nlp(voice_data)

# print what the user said 
print(voice_data)