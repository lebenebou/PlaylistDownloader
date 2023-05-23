
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import spotifyClient

# main window initiation ====================
mw = Tk()
mw.title("Playlist Downloader")
mw_width, mw_height = 380, 300
mw.minsize(mw_width, mw_height)
mw.geometry('+400+200')
# mw.iconbitmap("./icon.ico")
mw.resizable(False, False)

# variables =================================
chosenFolder = StringVar()
chosenFolder.set("") # set to empty string if no folder is chosen

# functions =================================
def askForDirectory() -> str:

    folderPath = filedialog.askdirectory()
    chosenFolder.set(folderPath)
    return folderPath

def fetchSongsFromLink() -> str:

    link = link_entry.get()
    playlist = spotifyClient.getPlaylistJSON(link)

    print(playlist)
# frames - widgets - buttons ================

link_label = ttk.Label(mw, text="Playlist Link")
link_label.place(x=18, y=10)

link_entry = ttk.Entry(mw, width=42)
link_entry.place(x=20, y=30)

fetch_btn = ttk.Button(mw,text="Fetch", command=fetchSongsFromLink)
fetch_btn.place(x=283 ,y=28)

song_list_box = Listbox(mw, width=56, height=11)
song_list_box.place(x=19, y=75)

choose_dir_button = ttk.Button(mw,text="Choose Folder", command=askForDirectory)
choose_dir_button.place(x=18,y=mw_height-35)

download_btn = ttk.Button(mw,text="Download")
download_btn.place(x=mw_width - 96,y=mw_height-35)

# ===========================================
if __name__=="__main__":
    mw.mainloop()