from AI_response import ai
from Speak import say
import os
import re
def Save_text(prompt, folder="Panther"):
    """
    Save the AI response to a text file in the specified folder.
    """
    try:
        # Clean the prompt to create a valid filename
        cleaned_prompt = re.sub(r"[^\w\s]", "", prompt).strip()
        # Ensure the folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)
        # Define the file name
        file_name= f"{folder}/{cleaned_prompt.replace(' ','_')[:50]}.txt"  # Limit filename length to 50 characters
        # Generate AI response
        response = ai(prompt)
        # Write the AI response to the file
        with open(file_name, "w", encoding='utf-8') as f:
            f.write(response)

        print(f"Response saved to: {file_name}")
    except Exception as e:
        print("Error saving response:", e)