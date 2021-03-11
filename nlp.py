from google.cloud import language_v1
import os

client = language_v1.LanguageServiceClient()

credential_path = "api_key.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

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

