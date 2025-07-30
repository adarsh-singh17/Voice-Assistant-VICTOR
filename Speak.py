import speech_recognition as sr
import pyttsx3  
import win32com.client
import time
#############################                                 Function to speak text                                ###############################
def say(text): 
   
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    time.sleep(0.5)
    speaker.Speak(text)
    time.sleep(0.2)