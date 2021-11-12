import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
SPOTIPY_CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
SPOTIPY_REDIRECT_URL = os.environ["SPOTIPY_REDIRECT_URL"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URL,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))

user_id = sp.current_user()["id"]


def get_top_100():
    user_date = input("Which year do you want to travel to? (YYYY-MM-DD): ")
    URL = "https://www.billboard.com/charts/hot-100"
    response = requests.get(f"{URL}/{user_date}")
    webpage = response.text
    soup = BeautifulSoup(webpage, "html.parser")

    # error = soup.select_one(selector="div p").getText()
    top_100 = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
    top_100 = [song.getText() for song in top_100]

    # if error:
    #     return error
    return top_100, user_date.split("-")[0]


# get_user_id()

top_100_tuple = get_top_100()
song_names = top_100_tuple[0]
year = top_100_tuple[1]


def create_song_uri_list():
    song_uris = []

    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")

        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(song)
        except IndexError:
            print(f"{song} not available in Spotify... Skipping.")
    return song_uris



def create_playlist():
    playlist = sp.user_playlist_create(user_id, name=f"{year} Billboard 100", public=False)
    playlist_id = playlist["id"]
    return playlist_id


def add_songs(playlist_id, uris):
    sp.playlist_add_items(playlist_id=playlist_id, items=uris)


def run():
    uris = create_song_uri_list()
    pl_id = create_playlist()
    add_songs(pl_id, uris)

run()