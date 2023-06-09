
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

clientID = "38caf74efb5e4e5ba39bf377069c6201"
clientSecret = "268cbdbfeb2a47d5bad2daf65a7880c0"

client_credentials_manager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getPlaylistJSON(playlistLink: str) -> dict:
    
    playlist_id = playlistLink.split('/')[-1]  # Extract playlist ID from the link
    
    try:
        playlist = sp.playlist(playlist_id)

    except spotipy.exceptions.SpotifyException:

        return {"error":"invalid_link"}
    
    except requests.ConnectionError:

        return {"error":"no_internet"}

    return playlist

def getTrackNames(playlistJSON: dict) -> list[tuple[str]]:

    tracks = playlistJSON["tracks"]["items"]
    trackNames = []

    for track in tracks:

        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        trackNames.append( (track_name, artist_name) )

    return trackNames

if __name__=="__main__":

    link = str(input("Playlist Link: "))

    playlist = getPlaylistJSON(link)

    if len(playlist)==1:

        print(playlist["error"])
        exit(0)

    tracks = getTrackNames(playlist)

    for track in tracks:

        print(track)