import os
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

travel_back_date = input("Which date you want to travel back to? Enter the date in YYYY-MM-DD format: ")

year = travel_back_date.split('-')[0]

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{travel_back_date}/"

response = requests.get(BILLBOARD_URL)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")
songs_names = soup.find_all(name="li", class_="o-chart-results-list__item")
songs = []


for song in songs_names:
    try:
        songs.append(song.find(name="h3").text.strip())
    except AttributeError:
        pass

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri=os.getenv("SPOTIFY_REDIRECT_URL"),
                                               scope=scope)
                     )

user_id = sp.current_user()['id']
song_uris = []

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{travel_back_date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
