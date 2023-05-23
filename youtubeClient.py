
import os
import requests
from googleapiclient.discovery import build
from pytube import YouTube

# YouTube Data API key
API_KEY = "AIzaSyAZNHbEWlckahgNDXHg0FcRs_j0XXp5lBU"

def getYoutubeURL(songName: str, artist: str) -> None:

    youtube = build("youtube", "v3", developerKey=API_KEY)

    search_response = youtube.search().list(
        q=f"{songName} {artist} lyrics",
        part="snippet",
        maxResults=1,  # Limit to one result
        type="video"
    ).execute()

    video_id = search_response["items"][0]["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url

def downloadSong(url, dir, fileName):

    pass

if __name__=="__main__":

    song_name = str(input("Song Name: "))
    artist = str(input("Artist Name: "))
    download_directory = "."

    song_url = getYoutubeURL(song_name, artist)
    print(song_url)