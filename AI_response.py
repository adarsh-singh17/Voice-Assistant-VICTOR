##################################                          To get reply in text form from AI                          ###############################
import os
import google.generativeai as genai
import openai
import re

def clean_text(text):
    # Remove any unwanted characters or formatting
    return re.sub(r"[*_`~>#\-\+]", "", text).strip()

def ai(prompt): 
    text = f"🧠 Generating AI response for: {prompt}\n\n📌 Response:\n\n"

    google_key = os.getenv("GOOGLE_API_KEY")

    gemini_response = ""

    try:
        # Try Gemini response
        if google_key:
            genai.configure(api_key=google_key)
            gemini_model = genai.GenerativeModel('gemini-1.5-flash')
            gemini_response = gemini_model.generate_content(prompt).text.strip()
            gemini_response = clean_text(gemini_response)
    except Exception as e:
        gemini_response = "I'm sorry, Can you please repeat again"
    return gemini_response
    

  