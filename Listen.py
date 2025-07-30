import speech_recognition as sr
import pyttsx3
import time
##################################                                 Function to take voice input                                 ###############################
def takeCommand():   
    r =sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        r.energy_threshold = 300
        r.phrase_time_limit = 5
        print("Listening for your response...")
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google( audio , language="en-in")
            print(f"Input: {query}")
            time
            return query
        except Exception as e:
            print("Sorry, I didn't catch that. Please try again.")
            return ""
 