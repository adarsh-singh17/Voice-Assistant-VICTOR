#####################################                      Chat with AI              #####################################
from Speak import say
from AI_response import ai
from Listen import takeCommand

def chat(query):
    try:
        print(f"You: {query}")
    
        # Clean the query to remove unwanted characters
        cleaned_query = query.strip()
        # Generate AI response
        response=ai(cleaned_query)
        print(f"AI: {response[:200]}")
        say(response[:200]) # Limit response to 200 characters for speaking
    except Exception as e:
        print("An error occurred while chatting with AI:", e)
        say("Sorry, I couldn't process your request.")