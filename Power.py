import os
from Speak import say 
from Listen import takeCommand


def power_shutdown():
        
        say("Are you sure you want to shut down the computer? Please say yes or no.")
        confirmation = takeCommand().lower()
        print(f"Confirmation captured: {confirmation}")

        if "yes" in confirmation:
            say("Shutting down the system. Goodbye.")
            os.system("shutdown /s /t 1")
        elif "no" in confirmation:
            say("Shutdown cancelled.")
        else:
            say("I didn't understand your response. Shutdown aborted.")
def power_restart():
        say("Are you sure you want to restart the computer? Please say yes or no.")
        confirmation = takeCommand().lower()
        print(f"Confirmation captured: {confirmation}")

        if "yes" in confirmation:
            say("Restarting the system. Goodbye.")
            os.system("shutdown /r /t 1")
        elif "no" in confirmation:
            say("Restart cancelled.")
        else:
            say("I didn't understand your response. Restart aborted.")

def power_sleep():
        say("Are you sure you want to put the computer to sleep? Please say yes or no.")
        confirmation = takeCommand().lower()
        print(f"Confirmation captured: {confirmation}")

        if "yes" in confirmation:
            say("Putting the system to sleep. Goodbye.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "no" in confirmation:
            say("Sleep cancelled.")
        else:
            say("I didn't understand your response. Sleep aborted.")