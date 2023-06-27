# pip install moviepy
# pip install pytube


from pytube import Playlist

def download_playlist(playlist_url, path):
    playlist = Playlist(playlist_url)
    
    # Parcours de toutes les vidéos de la playlist et leur téléchargement
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path=path)


# Utilisation de la fonction
# HBA Playlist
# lien_vers_la_playlist = "https://www.youtube.com/playlist?list=PLh6ROTLQSgi2VMz08SUujr9yBiQuORXAb"
# Gelmiş geçmiş en iyi Türkçe şarkılar
lien_vers_la_playlist = "https://www.youtube.com/watch?v=5J7OoSZ3nKg&list=PLHxEztxikVr7ozs8cHUF65i-kdm0hEA-3&ab_channel=seka28"
chemin_du_dossier_de_destination = "/Users/harisbaran/Musique"

print("Début du traitement...")
download_playlist(lien_vers_la_playlist, chemin_du_dossier_de_destination)
print("Fin du traitement")
print("Les musiques se trouvent : " + chemin_du_dossier_de_destination)
 