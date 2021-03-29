import datetime
from secrets import bearer
import time
import requests
from endpoints import end_point_url, limit, market,  seed_artists, seed_genres, seed_tracks

class RecommendMusic:
  def __init__(self):
    self.end_point_url = end_point_url
    self.limit = limit
    self.market = market
    self.seed_artists = seed_artists
    self.seed_genres = seed_genres
    self.seed_tracks = seed_tracks
    self.bearer = bearer
    
  def get_recommended_music(self):
      query = f"{self.end_point_url}?limit={self.limit}&market={self.market}&seed_artists={self.seed_artists}&seed_genres={self.seed_genres}&seed_tracks={self.seed_tracks}"
      response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {self.bearer}"})
      res = response.json()
      for i in res['tracks']:
            print(f"{i['name']} by {i['artists'][0]['name']}") 
  def time_check(self):
    hour = int(datetime.datetime.now().hour)
    if hour >= 7 and hour <= 8:
          print("I have created a playlist with song recommends for Shashank to listen to")
          rc.get_recommended_music()
    else:
          print("Not the time to do it...")
    time.sleep(2700)
                
rc = RecommendMusic()
rc.time_check()
