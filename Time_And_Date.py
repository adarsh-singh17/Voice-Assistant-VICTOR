import datetime
import win32com.client
import time
from Speak import say

def get_date_and_time(query):
    
    try:
        now = datetime.datetime.now()
        year = now.year
        month = now.strftime("%B")  # Converts num → month name
        day = now.day
        weekday = now.strftime("%A")
        hour = now.hour
        minute = now.minute
        second = now.second

        if "the date and time" in query.lower() or "date and time" in query.lower() or "the date and the time" in query.lower():
            print(f"The Date is {day} {month} {year} and Time is {hour}:{minute}:{second} and today is {weekday}")
            say(f"The date is {day} {month} {year}, and the time is {hour} hours {minute} minutes and {second} seconds and today is {weekday}.")

        elif "the date" in query.lower():
            print(f"The Date is {day} {month} {year} and today is {weekday}")
            say(f"The date is {day} {month} {year} and today is {weekday}.")

        elif "the time" in query.lower():
            print(f"The Time is {hour}:{minute}:{second}")
            say(f"The time is {hour} hours {minute} minutes and {second} seconds.")

    except Exception as e:
        print("An error occurred while getting the date and time:", e)
        say("Sorry, I couldn't retrieve the date and time.")