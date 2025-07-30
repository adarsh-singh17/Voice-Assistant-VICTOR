from Speak import say
import webbrowser
#################################                                 Search with Google                                 ###############################     
def searchgoogle(query):
    try:
        spoken_query = query.strip()  
        encoded_query = '+'.join(spoken_query.split())  

        url = f"https://www.google.com/search?q={encoded_query}"
        webbrowser.open(url)

        print(f"Searching Google for: {spoken_query}")  
        say(f"Searching Google for {spoken_query}")     

    except Exception as e:
        print("Sorry, an error occurred:", e)
        say("Sorry, I couldn't search Google.")


##################################                                 Search On Youtube                                ###############################
def searchyoutube(query):
    try:
        spoken_query = query.strip()  
        encoded_query = '+'.join(spoken_query.split())  

        url = f"https://www.youtube.com/results?search_query={encoded_query}"
        webbrowser.open(url)

        print(f"Searching Youtube for: {spoken_query}")  
        say(f"Searching Youtube for {spoken_query}")     
    except Exception as e:
        print("Sorry, an error occurred:", e)
        say("Sorry, I couldn't search Youtube.")


###################################                                 Search Wikipedia                                 ###############################
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

