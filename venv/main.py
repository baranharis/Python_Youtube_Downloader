# 1- python3 -m venv venv --> créer un environnement virtuel Python.
# 2-    Sur les systèmes Unix ou MacOS, utilisez : source venv/bin/activate
#       Sur Windows, utilisez : .\venv\Scripts\activate
# 3- python3 -m pip install customtkinter
# 4- python3 -m pip install pytube

import tkinter
import customtkinter
from pytube import YouTube, Playlist
import re
from tkinter import ttk
import os
from pytube.exceptions import RegexMatchError, ExtractError, AgeRestrictedError


def download_video(video, path, prefix):
    try:
        video.streams.get_highest_resolution().download(path)
        file_name = f"{prefix}_{video.title}.mp4"
        original_file_path = os.path.join(path, video.title + ".mp4")

        # Vérifier si le fichier a été téléchargé
        if os.path.exists(original_file_path):
            new_file_path = os.path.join(path, file_name)
            os.rename(original_file_path, new_file_path)
            # Maintenant le fichier a été renommé avec le préfixe et l'index
        else:
            print(f"Erreur : Le fichier {video.title}.mp4 n'a pas été téléchargé correctement.")
    except AgeRestrictedError:
        print(f"Erreur : La vidéo {video.title} est restreinte en fonction de l'âge et nécessite une connexion pour être téléchargée.")
    except Exception as e:
        print(f"Erreur : Une erreur inattendue s'est produite lors du téléchargement de la vidéo {video.title}. Erreur : {str(e)}")


def download_audio(video, path, prefix):
    audio_stream = video.streams.filter(only_audio=True).first()
    file_name = f"{prefix}_{video.title}.mp3"
    audio_stream.download(output_path=path, filename=file_name)

    
def download_playlist(playlist_url, path, prefix, message_text_widget, progress_bar, download_format):

    if not playlist_url:
        message_text_widget.insert(tkinter.END, "Error: Please enter the URL of the playlist.\n")
        return

    if not prefix:
        message_text_widget.insert(tkinter.END, "Error: Please enter the prefix.\n")
        return
    
    yt_playlist = Playlist(playlist_url)
    # print("Download_playlist - 1")
    total_videos = len(yt_playlist.videos)
    progress_bar['maximum'] = total_videos
    
    message_text_widget.insert(tkinter.END, "********************************************* \n")
    message_text_widget.insert(tkinter.END, "Download_playlist - "+ yt_playlist.title + " (Vidéo: "+ str(total_videos) +")\n")
    message_text_widget.insert(tkinter.END, "********************************************* \n")
    message_text_widget.update_idletasks()

    
    download_func = download_video if download_format == "MP4" else download_audio

    # Parcours de toutes les vidéos de la playlist et les télécharges dans le répertoire passer en paramètre
    for index, video in enumerate(yt_playlist.videos, start=1):
        message_text_widget.insert(tkinter.END, "Downloading : " + video.title + "\n")
        message_text_widget.update_idletasks()

        download_func(video, path, prefix)

        progress_bar['value'] = index
        progress_bar.update()

def clear_messages(message_text_widget):
    message_text_widget.delete("1.0", tkinter.END)


# Sytem Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame for app
app = customtkinter.CTk()
app.geometry("720x720")
app.title("Youtube downloader - by HBA")

# Adding UI element
title = customtkinter.CTkLabel(app,text="Insert your youtube link")
title.pack(padx=10, pady=10)

# Adding link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=30, textvariable=url_var)
link.pack()

# Adding prefix input
prefix_var = tkinter.StringVar()
prefix_label = customtkinter.CTkLabel(app, text="Enter the prefix:")
prefix_label.pack(padx=10, pady=5)
prefix_entry = customtkinter.CTkEntry(app, width=50, height=30, textvariable=prefix_var)
prefix_entry.pack()

# Display message
message_text_widget = tkinter.Text(app, width=70, height=20)
message_text_widget.pack()

# Progress bar
progress_bar = ttk.Progressbar(app, orient=tkinter.HORIZONTAL, length=200, mode='determinate')
progress_bar.pack()

# Download format selection
download_formats = ["MP4", "MP3"]
selected_format = tkinter.StringVar(value=download_formats[0])
format_selection = ttk.Combobox(app, textvariable=selected_format, values=download_formats)
format_selection.pack()

# Download button
# path = "/Users/harisbaran/Downloads/Temp_Musique"
path = "/Users/harisbaran/Documents/_Projets/Python/Python_Automation_Scripts/Python_Youtube_Downloader/venv/video"

def on_download_clicked():
    url = url_var.get()
    prefix = prefix_var.get()

    clear_messages(message_text_widget)

    if not url:
        message_text_widget.insert(tkinter.END, "Error: Please enter the URL of the playlist.\n")
    elif not prefix:
        message_text_widget.insert(tkinter.END, "Error: Please enter the prefix.\n")
    else:
        download_playlist(url, path, prefix, message_text_widget, progress_bar, selected_format.get())

download_btn = customtkinter.CTkButton(app, text="Download", command=on_download_clicked)
download_btn.pack(padx=10, pady=10)
# download_btn = customtkinter.CTkButton(app, text="Download", command=lambda: download_playlist(url_var.get(), path, prefix_var.get(), message_text_widget, progress_bar, selected_format.get()))

# Clear button
clear_btn = customtkinter.CTkButton(app, text="Clear", command=lambda: clear_messages(message_text_widget))
clear_btn.pack(padx=10, pady=5)


# Run app
app.mainloop()
# test_playlist_url = "https://www.youtube.com/playlist?list=PLh6ROTLQSgi2VMz08SUujr9yBiQuORXAb"
# test_path = "/Users/harisbaran/Downloads/Temp_Musique"
# print("Début du traitement...")
# download_playlist(test_playlist_url, test_path)
# print("Fin du traitement")
# print("Les musiques se trouvent : " + chemin_du_dossier_de_destination)
 