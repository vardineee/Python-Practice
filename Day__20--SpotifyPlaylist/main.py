from bs4 import BeautifulSoup
import  requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("What year you would like to travel to? format YYY-MM-DD:  ")

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
songs = soup.find_all(name="h3", id = "title-of-a-story", class_="a-no-trucate")
print(songs[0])
song_names = [song.getText().strip() for song in songs]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com/callback",
        client_id="0f5dcf7b1f4940d38fbadd4a476cfbf6",
        client_secret="0f4f474405394c9d8192e3078ce2e629",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
