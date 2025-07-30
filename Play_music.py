import os
import random
import time
from playsound import playsound
from Speak import say
import platform

################################                                 Function to play music from a specific folder                                 ###############################
def playmusic():
    musicFolder = r"D:\Songs\songs mix\Hindi songs_1"
    musicFiles = [f for f in os.listdir(musicFolder) if f.endswith('.mp3')]
    
    if musicFiles:
        randomSong = random.choice(musicFiles)
        songPath = os.path.join(musicFolder, randomSong)
        print(f"Playing music: {randomSong}")
        os.startfile(songPath) # Use os.startfile to play the music file
        say(f"Playing music...")
    else:
        say("No music files found in the specified folder.")

def closemusic():
    try:
        if platform.system() == "Windows":
            mediaPlayer = ["wmplayer.exe", "vlc.exe", "iTunes.exe","spotify.exe","groove.exe", "music.ui.exe", "Music.UI.exe"]
            for player in mediaPlayer:
                os.system(f"taskkill /f /im {player}")
            say("Closed the music player...")
        else:
            say("Stopping the song is not supported on this platform....")
    except Exception as e:
        say("I couldn't stop the music player...")