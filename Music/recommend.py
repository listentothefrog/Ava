import json
import os 

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
access_token = os.getenv("ACCESS_TOKEN")

class RecommendMusic:
  def __init__(self):
      pass
  def recommend_music(self):
    print("Music....")
    

rc = RecommendMusic()
rc.recommend_music()