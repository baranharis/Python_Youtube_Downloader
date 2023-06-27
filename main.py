# 1- python3 -m venv venv --> créer un environnement virtuel Python.
# 2-    Sur les systèmes Unix ou MacOS, utilisez : source venv/bin/activate
#       Sur Windows, utilisez : .\venv\Scripts\activate

# pip install moviepy
# brew install ffmpeg
# pip install pytube

import ssl
import pytube
from pytube import Playlist

ssl._create_default_https_context = ssl._create_unverified_context

# link = "https://www.youtube.com/watch?v=Tp5dI-GDerM&ab_channel=AliYounes"
# yt = pytube.YouTube(link)
# yt.streams.get_highest_resolution().download()
# print("Downloaded", link)


def download_playlist(playlist_url, path):
    playlist = Playlist(playlist_url)
    
    # Parcours de toutes les vidéos de la playlist et leur téléchargement
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path=path)


# Utilisation de la fonction
# HBA Playlist
lien_vers_la_playlist = "https://www.youtube.com/playlist?list=PLh6ROTLQSgi2VMz08SUujr9yBiQuORXAb"
# Gelmiş geçmiş en iyi Türkçe şarkılar
# lien_vers_la_playlist = "https://www.youtube.com/watch?v=5J7OoSZ3nKg&list=PLHxEztxikVr7ozs8cHUF65i-kdm0hEA-3&ab_channel=seka28"
# Mix - İbrahim Tatlıses
# lien_vers_la_playlist = "https://www.youtube.com/watch?v=E_zUxFrJ_SE&list=PLRiHAPb9-vYoW7AtK0rlVW88wpWKI5CCi&ab_channel=idobaym%C3%BCzik"
chemin_du_dossier_de_destination = "/Users/harisbaran/Downloads/Temp_Musique"

print("Début du traitement...")
download_playlist(lien_vers_la_playlist, chemin_du_dossier_de_destination)
print("Fin du traitement")
print("Les musiques se trouvent : " + chemin_du_dossier_de_destination)
 