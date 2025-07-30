import os
from Speak import say
import webbrowser
import pyautogui
import pyttsx3
import subprocess
import platform
from time import sleep 
sites = [
        ["youtube", "https://www.youtube.com/"],
        ["wikipedia", "https://www.wikipedia.org/"],
        ["google", "https://www.google.com/"],
        ["facebook", "https://www.facebook.com/"],
        ["twitter", "https://www.twitter.com/"],
        ["instagram", "https://www.instagram.com/"],
        ["linkedin", "https://www.linkedin.com/"],
        ["github", "https://www.github.com/"],
        ["stackoverflow", "https://stackoverflow.com/"],
        ["reddit", "https://www.reddit.com/"],
        ["netflix", "https://www.netflix.com/"],
        ["amazon", "https://www.amazon.com/"],
        ["flipkart", "https://www.flipkart.com/"],
        ["coursera", "https://www.coursera.org/"],
        ["khan academy", "https://www.khanacademy.org/"],
        ["spotify", "https://www.spotify.com/"],
        ["gmail", "https://mail.google.com/"],
        ["drive", "https://drive.google.com/"]
        ]


apps = {
    "command prompt": "cmd",
    "cmd": "cmd",
    "paint": "mspaint",
    "ms paint": "mspaint",
    "word": "winword",
    "ms word": "winword",
    "excel": "excel",
    "ms excel": "excel",
    "chrome": "chrome",
    "google chrome": "chrome",
    "vs code": "code",
    "vscode": "code",
    "powerpoint": "powerpnt",
    "ms powerpoint": "powerpnt",
    "notepad": "notepad",
    "calculator": "calc",
    "file explorer": "explorer",
    "explorer": "explorer",
    "control panel": "control",
    "settings": "start ms-settings:",
    "task manager": "taskmgr",
    "snipping tool": "snippingtool",
    "windows security": "windowsdefender:",
    "media player": "wmplayer",
    "edge": "msedge",
    "microsoft edge": "msedge",
    "spotify": "spotify",
    "zoom": "zoom",
    "skype": "skype",
    "teams": "teams",
    "onenote": "onenote",
    "outlook": "outlook",
    "adobe reader": "AcroRd32",
    "telegram": "telegram",
    "camera": r"C:\Users\asus\OneDrive\Desktop\Camera.lnk",
    "whatsapp": "start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App",
    "discord": "discord",
}
uwp_apps = {
    "whatsapp": "WhatsApp",
    "camera": "WindowsCamera"
}

def open_site_or_app(query):
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            print(f"Opening {site[0]}...")
            say(f"Opening {site[0]}.")
            webbrowser.open(site[1])
            return
    for app in apps:
        if f"open {app}".lower() in query.lower():
            print(f"Opening {app}...")
            say(f"Opening {app}.")
            if app == "whatsapp":
                subprocess.Popen(['explorer', 'shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App'],
                               creationflags=subprocess.CREATE_NO_WINDOW)
            elif app == "camera":
                subprocess.Popen(apps[app],shell=True)
            else:
                os.system(f"start {apps[app]}")
            return
    # print("No matching site or app found to open.")
    # say("No matching site or app found to open.")
def close_site_or_app(query):
    if f"close tab" in query.lower():
        pyautogui.hotkey('ctrl', 'w')
        print("Closing the current tab...")
        say("Closing the current tab.")
    elif "close all tabs" in query.lower():
        pyautogui.hotkey('ctrl', 'shift', 'w')
        return
    
    for app in apps:
        if f"close {app}".lower() in query.lower():
            print(f"Closing {app}...")
            say(f"Closing {app}.")
            if app in ["whatsapp", "camera"]:
                os.system(f'powershell "Get-Process {uwp_apps[app]} | Stop-Process -Force"')
            else:
                os.system(f"taskkill /im {apps[app]}.exe /f")
            return
    for app in uwp_apps:
        if f"close {app}".lower() in query.lower():
            print(f"Closing {app}...")
            say(f"Closing {app}.")
            os.system(f'powershell "Get-Process {uwp_apps[app]} | Stop-Process -Force"')
            return
    # print("No matching site or app found to close.")
    # say("No matching site or app found to close.")