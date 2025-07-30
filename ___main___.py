import os
import webbrowser
import subprocess
import re
from Speak import say
from Listen import takeCommand
from Playing_yt_first_vdo import playfirstvideo
from GreetMe import greet
from Apps_And_Sites import open_site_or_app,close_site_or_app
from Search import searchgoogle, searchyoutube, searchwikipedia
from temperature import get_temperature
from Time_And_Date import get_date_and_time
from Youtube_Control import youtube_control, focus_youtube_tab
from Calculation import calculate
from search_wikipedia import searchwikipedia
from Play_music import playmusic , closemusic
from Power import power_shutdown, power_restart, power_sleep
from AI_response import ai
from Chat import chat
from AI_text_file import Save_text
###############################                                 Main Function to run the AI                                 ###############################

if __name__ == '__main__':
    print("Your Personal Assistant Responsing")
    say(" Hi,I am your Personal Assistant Victor , how may I help you")
    while True:
        print("Listening.....")
        query = takeCommand()

##################################                                 Wake up Command                                 ###############################
        if "wake up".lower() in query.lower():
            greet()

#################################                                 Hello Command                                 ###############################
        if any(greet in query.lower() for greet in ["hello", "hi", "hey"]):
            say("Hello! How can I assist you today?")

#################################                                 AI Response                                 ###############################
        elif "Panther".lower() in query.lower():
            command = query.replace("panther", "").replace("Panther","").strip()
            say(f"Generating AI response for: {command}")
            print(f"User asked: {command}")

            Save_text(command) 
            say("AI response generated. Is there anything else I can assist you with?")
        
##################################                                Open sites and Apps                                  ###############################
        elif "open " in query.lower():
            open_site_or_app(query)

#################################                                 Close sites and apps                                ###############################
        elif "close" in query.lower():
            close_site_or_app(query)
            
#################################                                 Search with Google                                 ###############################
        elif "google" in query.lower():
            cleaned_query = query.lower().replace("searching google for:", "")
            cleaned_query = cleaned_query.replace("google", "").replace("for", "", 1).strip()
            searchgoogle(cleaned_query)

            

#################################                                 Search On Youtube                                ###############################
        elif "search youtube" in query.lower():
            cleaned_query = query.lower().replace("search youtube", "").replace("for ","",1).strip()
            searchyoutube(cleaned_query)

##################################                                 Search Wikipedia                                 ###############################

        elif "search wikipedia" in query.lower():
            cleaned_query = query.lower().replace("search wikipedia", "").replace("for ","",1).strip()
            searchwikipedia(cleaned_query)

#################################                                 Temperature                                 ###############################

        elif "temperature" in query.lower() or "weather" in query.lower():
            if "in" in query.lower():
                city = query.split("in")[-1].strip()
                city = query.replace("temperature", "").replace("in", "").strip()
                temperature, humidity, pressure, weather_description = get_temperature(city)

            if temperature is None:
                say(weather_description)
            else:
                print(f"The temperature in {city} is {temperature}°C with {humidity}% humidity and {pressure} hPa pressure. Weather description: {weather_description}.")
                say(f"The temperature in {city} is {temperature}°C with {humidity}% humidity and {pressure} hPa pressure. Weather description: {weather_description}.")

#################################                                 Date and Time                                 ###############################
        elif "date and time" in query.lower() or "date" in query.lower() or "time" in query.lower() or "the date and time" in query.lower():
            get_date_and_time(query)

##################################                                 YouTube Control                                 ###############################
        elif "youtube" in query.lower():
            if "focus" in query.lower():
                if focus_youtube_tab():
                    say("Focused on YouTube tab.")
                else:
                    say("Could not find the YouTube tab.")
            else:
                command = query.lower().replace("youtube", "").strip()
                youtube_control(command)

##################################                                Play Random Music from folder                               ###############################
        elif any(phrase in query.lower() for phrase in ["play music", "start music", "music please", "start songs"]):
            playmusic()

#################################                                 Close the random music played                                ###############################
        elif any(phrase in query.lower() for phrase in ["stop music", "stop songs", "close music", "close songs"]):
            closemusic()

#################################                                 Play First Video on YouTube                                ###############################
        elif any(keyword in query.lower() for keyword in ["play first video", "play first video on youtube", "play first video for", "play", "play this", "play song", "i want to listen", 
            "search on youtube", "play something", "search and play", "play a video", "play a song"]):
            cleaned_query = query.lower()
            for keyword in ["play first video", "play first video on youtube", "play first video for", "play", "play this", "play song", "i want to listen",
                            "search on youtube", "play something", "search and play", "play a video", "play a song"]:
                cleaned_query = cleaned_query.replace(keyword, "").strip()
            if cleaned_query:
                print(f"Playing first video for : {cleaned_query}")
            else:
                print("No specific query provided, playing first video for general search.")
            playfirstvideo(cleaned_query)

#################################                                Calculations                                 ###############################
        elif any(word in query for word in ["calculate", "plus", "minus", "multiply", "divide", "+", "-", "*", "/"]):
            expression = query.replace("calculate", "").replace("what is", "").replace("solve", "").strip()

            try:
                result = calculate(expression)
                say(result)
            except:
                say("Opening calculator instead...")
                os.system("calc")

#################################                                Searching on wikipedia                                ###############################
        elif any(keyword in query.lower() for keyword in ["search wikipedia", "wikipedia", "wikipedia search","who is", "what is", "tell me about", "wikipedia", 
                "define", "explain", "know about", "information about"]):
            cleaned_query =query.lower()
            for keyword in ["search wikipedia", "wikipedia", "wikipedia search", "who is", "what is", "tell me about", "define", "explain", "know about", "information about"]:
                cleaned_query = cleaned_query.replace(keyword, "").strip()
            if cleaned_query:
                searchwikipedia(cleaned_query)
            else:
                say("Please provide a topic to search on Wikipedia.")

##################################                                 Power System                                ###############################
        elif any(keyword in query.lower() for keyword in ["shutdown", "shutdown system", "power off", "turn off","power down", "shutdown computer"]):
            power_shutdown()

        elif any(keyword in query.lower() for keyword in ["restart system", "restart computer", "restart", "reboot", "reboot system", "reboot computer", "restart the computer", "restar computer"]):
            power_restart()
        
        elif any(keyword in query.lower() for keyword in ["sleep", "put computer to sleep", "hibernate", "put computer to hibernate", "sleep mode", "hibernate mode", "put computer to sleep mode", "put computer to hibernate mode", "sleep the computer", "hibernate the computer"]):
            power_sleep()

##############################                                 Exit command                               ###############################
        elif any(keyword in query.lower() for keyword in ["exit", "quit", "close", "stop", "end"]):
            print("Exiting the program.")
            say("Goodbye! My friend Have a great day!")
            break

#################################                                 Chat with AI                                 ###############################
        else:
            print("Chatting with AI...")
            chat(query)