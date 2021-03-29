import datetime
from secrets import bearer, user_id
import time
import json
import requests
from endpoints import end_point_url, limit, market,  seed_artists, seed_genres, seed_tracks, uris

class RecommendMusic:
  def __init__(self):
    self.end_point_url = end_point_url
    self.limit = limit
    self.market = market
    self.seed_artists = seed_artists
    self.seed_genres = seed_genres
    self.seed_tracks = seed_tracks
    self.bearer = bearer
    self.user_id = user_id
  def get_recommended_music(self):
      query = f"{self.end_point_url}?limit={self.limit}&market={self.market}&seed_artists={self.seed_artists}&seed_genres={self.seed_genres}&seed_tracks={self.seed_tracks}"
      response =requests.get(query, 
               headers={"Content-Type":"application/json", 
                        "Authorization":f"Bearer {self.bearer}"})
      res = response.json()
      for i in res['tracks']:
            uris.append(f"{i['uri']}")
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
      playlist_id = res.json()['id']
      playlist_url = res.json()['external_urls']['spotify']
      endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
      request_body = json.dumps({
          "uris" : uris
        })
      response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                      "Authorization":f"Bearer {self.bearer}"})
      print(f'Your playlist is ready at {playlist_url}')
  
  def time_check(self):
    hour = int(datetime.datetime.now().hour)
    if hour >= 7 and hour <= 8:
          rc.get_recommended_music()
          rc.create_playlist()
    else:
          print("Not the time to do it...")
    time.sleep(2700)

if __name__ == "__main__": 
  rc = RecommendMusic()
  rc.time_check()
