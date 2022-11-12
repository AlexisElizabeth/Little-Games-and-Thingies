from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = XXX
SPOTIPY_CLIENT_SECRET = XXX
REDIRECT_URI = "http://example.com"

date = input("Which date would you like to travel to? "
             "Type the date in this format: YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

number_one_song_html = soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")
top_99_songs_html = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")


number_one_song_title = [number_one_song_html.getText()]
song_titles = [song.getText() for song in top_99_songs_html]
top_100_songs = number_one_song_title + song_titles

top_100_songs = [song.replace("\n", "") for song in top_100_songs]
top_100_songs = [song.replace("\t", "") for song in top_100_songs]
print(top_100_songs)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in top_100_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False, collaborative=False,
                                   description=f"The top 100 from {date}")

sp.playlist_add_items(playlist_id = playlist["id"], items=song_uris)
