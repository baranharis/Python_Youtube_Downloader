# 1- python3 -m venv venv --> créer un environnement virtuel Python.
# 2-    Sur les systèmes Unix ou MacOS, utilisez : source venv/bin/activate
#       Sur Windows, utilisez : .\venv\Scripts\activate
# 3- python3 -m pip install customtkinter
# 4- python3 -m pip install pytube

import tkinter
import customtkinter
from pytube import YouTube, Playlist
import re


def download_playlist(playlist_url, path):
    yt_playlist = Playlist(playlist_url)
    # yt_playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print("Download_playlist - 1")

    # Parcours de toutes les vidéos de la playlist et les télécharges dans le répertoire passer en paramètre
    # print(playlist.length)
    # print(f'Downloading: {playlist.title}')
    for video in yt_playlist.videos:
        video.streams.get_lowest_resolution().download("/Users/harisbaran/Documents/_Projets/Python/Python_Automation_Scripts/Python_Youtube_Downloader/venv/video")
        print("Video downloaded : ", video.title)

# def StartDownload(playlist_url, path):
#     try:
#         ytLink = link.get()
#         ytObject = YouTube(ytLink)
#         video = ytObject.streams.get_highest_resolution().download(output_path=path)
#         # Parcours de toutes les vidéos de la playlist et leur téléchargement
#         # for video in ytObject.videos:
#             # video.streams.get_highest_resolution().download(output_path=path)
#     except:
#         print("ERREUR - Link not correct")
#         return
#     print("Download completed!")

# Sytem Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame for app
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader - by HBA")

# Adding UI element
title = customtkinter.CTkLabel(app,text="Insert your youtube link")
title.pack(padx=10, pady=10)

# Adding link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=30, textvariable=url_var)
link.pack()

# Download button
chemin_du_dossier_de_destination = "/Users/harisbaran/Downloads/Temp_Musique"
# download_btn = customtkinter.CTkButton(app, text="Download", command=StartDownload(url_var, chemin_du_dossier_de_destination))
# download_btn.pack(padx=10, pady=10)

# Run app
# app.mainloop()
test_playlist_url = "https://www.youtube.com/playlist?list=PLh6ROTLQSgi2VMz08SUujr9yBiQuORXAb"
test_path = "/Users/harisbaran/Downloads/Temp_Musique"
print("Début du traitement...")
download_playlist(test_playlist_url, test_path)
print("Fin du traitement")
print("Les musiques se trouvent : " + chemin_du_dossier_de_destination)
 