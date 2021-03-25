import json
import requests
import datetime
from secrets import user_id, bearer
class RecommendMusic:
  def __init__(self):
    self.user_id = user_id
    self.bearer = bearer
  
  def create_playlist(self):
        today_date = datetime.date.today()
        body = json.dumps({
          "name": f"{today_date} Playlist",
          "description": "A playlist with song recommends for Shashank to listen to",
            "public": False
        })
        query = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        res = requests.post(
          query,
          data=body,
          headers ={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.bearer}"
          }
        )
        response = res.json()
        print(response)
    
  def recommend_music(self):
    hour = int(datetime.datetime.now().hour)
    if hour >= 21 and hour <= 22:
          print("I have created a playlist with song recommends for Shashank to listen to")
          rc.create_playlist()
    else:
          print("Not the time to do it...")

rc = RecommendMusic()
rc.recommend_music()