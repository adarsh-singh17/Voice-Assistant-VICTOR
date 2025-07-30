import webbrowser
from Speak import say

################################                                 Function to search Wikipedia                                 ###############################

def searchwikipedia(query):
    try:
        spoken_query = query.strip()  
        encoded_query = '+'.join(spoken_query.split())  

        url = f"https://en.wikipedia.org/wiki/{encoded_query}"
        webbrowser.open(url)

        print(f"Searching Wikipedia for: {spoken_query}")  
        say(f"Searching Wikipedia for {spoken_query}")     
    except Exception as e:
        print("Sorry, an error occurred:", e)
        say("Sorry, I couldn't search Wikipedia.")
