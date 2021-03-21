import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()
import os
import time


client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def search(songs_name):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, 
                                                           client_secret=client_secret))
    results =sp.search(q=songs_name, limit=10)

    print("Here are songs that I found on Spotify")
    time.sleep(1)
    for idx, tracks in enumerate(results['tracks']['items']):
            print(tracks['name'])

    time.sleep(1)
    
    print("Here are the link to the songs")
    
    for idx, urls in enumerate(results['tracks']['items']):
                print(urls['external_urls']['spotify'])   
    time.sleep(1)
    print("Enjoy!")
    
search("Lil Nas X")