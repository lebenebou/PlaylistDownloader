
import os
import requests
from googleapiclient.discovery import build
from pytube import YouTube

# YouTube Data API key
API_KEY = "AIzaSyAZNHbEWlckahgNDXHg0FcRs_j0XXp5lBU"

def getFirstYoutubeURL(_searchQuery: str) -> str:

    youtube = build("youtube", "v3", developerKey=API_KEY)

    search_response = youtube.search().list(
        q = _searchQuery,
        part="snippet",
        maxResults=1,  # Limit to one result
        type="video"
    ).execute()

    video_id = search_response["items"][0]["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    return video_url

def downloadSong(youtubeURL, dir, filename) -> None:

    video = YouTube(youtubeURL)
    audioStream = video.streams.filter(only_audio = True).first()

    audioStream.download(output_path=dir, filename=filename)

if __name__=="__main__":

    song_name = str(input("Song Name: "))
    artist = str(input("Artist Name: "))
    download_directory = "."

    song_url = getFirstYoutubeURL(_searchQuery = f"{song_name} {artist} lyrics")
    downloadSong(song_url, ".", "file.mp3")