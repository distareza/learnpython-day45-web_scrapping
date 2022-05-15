"""
    Create a Spotify Play list of top 100 song of particular date in past

    Step 1 - Scraping the Billboard Hot 100
            https://www.billboard.com/charts/hot-100/2009-05-01
    Step 2 - Authentication with Spotify
            http://spotify.com/signup/
            https://developer.spotify.com/dashboard/
            https://spotipy.readthedocs.io/

            HINT 1: You need your own Spotify app Client ID and Secret.
            HINT 2: This is the method you'll need: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth
            HINT 3: Try passing the Client ID and Secret directly into the SpotifyOAuth() constructor instead of using export or set.
                    Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username).
                    As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.
            HINT 4: You need the "playlist-modify-private" scope in order to create a private playlist on Spotify.
            HINT 5:  If successful, you should see the "confirmation" page show up automatically (be sure to click Agree):
                    Then it will take you to the page, example.com and you need to copy the entire URL in the address bar:
                    Finally, you need to paste the URL into the prompt in PyCharm:
                    Now if you close PyCharm and restart, you should see a new file in this project called token.txt

    Step 3 - Search Spotify for the Songs from Step 1
    Step 4 - Creating and Adding to Spotify Playlist
"""
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import my_configuration
import spotipy
from spotipy.oauth2 import SpotifyOAuth

while True:
    try:
        input_date = input("Which year do you want too travel to? Type the date in format YYYY-MM-DD")
        datetime.strptime(input_date, "%Y-%m-%d")
        break
    except Exception as ex:
        print(ex)
#input_date = "2000-08-12"

# Scraping Billboard 100
billboard_url = f"https://www.billboard.com/charts/hot-100/{input_date}/"
response = requests.get(billboard_url)
response.raise_for_status()
html_song = BeautifulSoup(response.text, 'html.parser')
songs = [ el.getText().strip() for el in html_song.select("li h3#title-of-a-story")]

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=my_configuration.spotify_client_id,
        client_secret=my_configuration.spotify_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
year = input_date.split("-")[0]
song_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
