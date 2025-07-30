import requests
import re
import webbrowser
import os
from Speak import say
################################                                 Function to play first video on youtube                                 ###############################

def playfirstvideo(query):
    try:
        search_query = '+'.join(query.strip().split())
        url = f"https://www.youtube.com/results?search_query={search_query}"
        response = requests.get(url)

        # Extract video URLs using regex (match video ID format)
        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)

        if video_ids:
            video_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
            webbrowser.open(video_url)
            print(f"Playing: {video_url}")
            say(f"Playing the top result for {query} on YouTube.")
        else:
            say("Sorry, I couldn't find any videos.")
            print("No video ID found.")

    except Exception as e:
        print("Error:", e)
        say("An error occurred while trying to play the video.")
