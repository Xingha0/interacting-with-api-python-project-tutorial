
import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy import SpotifyClientCredentials

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager= SpotifyClientCredentials(client_id, client_secret))


id_artista = '05aVtfDzBvg9eVu9MAZPGD'
respuesta = sp.artist_top_tracks(id_artista)
tracks = respuesta['tracks']


df_tracks = pd.DataFrame.from_records(tracks)
df_tracks


df_tracks.sort_values(['popularity'],inplace=True)
df_tracks

df_tracks.head(3)


import matplotlib.pyplot as plt

plt.scatter(x=df_tracks['popularity'],y=df_tracks['duration_ms'])
plt.show

