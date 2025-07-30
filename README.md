# 🧠 Voice-Assistant-VICTOR

A Python-based AI voice assistant inspired by Alexa, Siri, and Google Assistant. Victor can perform multiple smart tasks through voice commands, acting as a fully offline or online digital assistant.

---

## 🚀 Features

✅ Voice-controlled interactions using speech recognition  
✅ Text-to-speech response  
✅ Weather updates via API  
✅ YouTube control (search & play first video)  
✅ Google search and Wikipedia summary  
✅ Music player from local folder  
✅ System time/date and power info  
✅ Note-taking and saving text files  
✅ Python file modularized into reusable components  
✅ Future scope: Android deployment, mobile control, sensor access

---

## 📂 Project Structure

```bash
.
├── 0__main__.py                # 🔹 Main entry file
├── README.md                   # 📄 Project description
├── AI_response.py              # Gemini/AI content generator
├── AI_text_file.py             # Save AI response to file
├── Apps_And_Sites.py           # Open apps/sites like Google, YouTube
├── Chat.py                     # Casual conversation
├── GreetMe.py                  # Welcome & greet logic
├── Listen.py                   # Voice input handling
├── Play_music.py               # Music player
├── Playing_yt_first_vdo.py     # YouTube video player
├── Power.py                    # Battery and system info
├── Search.py                   # Google/Wikipedia search
├── Speak.py                    # TTS (Text to Speech)
├── Time_And_Date.py            # Fetch current time/date
├── temperature.py              # Weather via API
├── Youtube_Control.py          # YouTube tab navigation
└── Panther/                    # Notes/text saving folder

## ✨ Victor Voice Assistant – Features Overview

| **Feature**              | **Description**                          | **Example Prompt**                          |
| ------------------------ | ---------------------------------------- | ------------------------------------------- |
| Wake Up                  | Activates the assistant                  | `wake up`                                   |
| Greetings                | Basic hello interaction                  | `hello`, `hi`, `hey`                        |
| AI Response (Panther)    | Triggers AI response + saves query       | `Panther tell me a joke`                    |
| Open Apps/Websites       | Opens installed apps or any website      | `open YouTube`, `open Spotify`              |
| Close Apps/Websites      | Closes apps or tabs                      | `close YouTube`, `close Chrome`             |
| Google Search            | Searches Google                          | `search Google for weather in Delhi`        |
| YouTube Search           | Searches on YouTube                      | `search YouTube for music`                  |
| Wikipedia Search         | Searches Wikipedia                       | `search Wikipedia for Einstein`             |
| Temperature / Weather    | Reports temperature & weather            | `what's the weather in Mumbai`              |
| Date & Time              | Tells date or time                       | `what time is it`, `what's today's date`    |
| YouTube Control          | Play/pause/skip YouTube video            | `pause YouTube`, `play YouTube`             |
| Focus YouTube Tab        | Focuses Chrome tab where YouTube is open | `focus YouTube`                             |
| Play Random Music        | Plays random music from folder           | `play music`, `start songs`                 |
| Close Music              | Stops the music being played             | `stop music`, `close songs`                 |
| Play First YouTube Video | Searches & plays first result            | `play song by Arijit`, `search on YouTube`  |
| Calculator / Math        | Solves math expressions                  | `calculate 25 + 43`, `what is 10*12`        |
| Wikipedia Info           | Tells info on any topic                  | `who is Newton`, `define quantum mechanics` |
| Shutdown System          | Shuts down PC                            | `shutdown`, `power off`                     |
| Restart System           | Restarts PC                              | `restart computer`, `reboot system`         |
| Sleep Mode               | Puts PC to sleep or hibernate            | `put computer to sleep`, `hibernate mode`   |
| AI Chat                  | Fallback to chatbot if no match          | Anything else (e.g., `tell me a story`)     |
| AI Response              | Response for query in text form          | Panther to awaken the AI bot for text       |