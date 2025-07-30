###############################                                 GreetMe                                ###############################

from Speak import say
import datetime

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        greeting = "Good Morning, sir" 
        say(greeting)
    elif hour < 18:
        greeting = "Good Afternoon, sir" 
        say(greeting)
    else:
        greeting = "Good Evening, sir" 
        say(greeting)
    say("How may I help you")