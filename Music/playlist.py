import json
import datetime
import requests
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

rc = RecommendMusic()
rc.create_playlist()