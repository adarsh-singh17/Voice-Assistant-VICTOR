import pyautogui
import webbrowser
from Speak import say
import pygetwindow as gw
import time
################################                                 Function to control youtube                                ###############################

def focus_youtube_tab():
    try:
        for window in gw.getWindowsWithTitle('YouTube'):
            if window.isActive == False:
                window.activate()
                time.sleep(0.5)
                return True
        say("YouTube window not found.")
        return False
    except Exception as e:
        print("Error focusing YouTube:", e)
        return False

def youtube_control(command):
    try:
        if command == "pause":
            pyautogui.press("k")
            say("Paused the video.")
        elif command == "play":
            pyautogui.press("k")
            say("Playing the video.")
        elif command == "next":
            pyautogui.hotkey("shift", "n")
            say("Playing the next video.")
        elif command == "previous":
            pyautogui.hotkey("shift", "p")
            say("Playing the previous video.")
        elif command == "mute":
            pyautogui.press("m")
            say("Muted the video.")
        elif command == "unmute":
            pyautogui.press("m")
            say("Unmuted the video.")
        elif command == "fullscreen":
            pyautogui.press("f")
            say("Entered fullscreen mode.")
        elif command == "exit fullscreen":
            pyautogui.press("f")
            say("Exited fullscreen mode.")
        elif command == "volume up":
            pyautogui.press("up")
            say("Increased the volume.")
        elif command == "volume down":
            pyautogui.press("down")
            say("Decreased the volume.")
        elif command == "skip":
            for i in range(2):
                pyautogui.press("right")
                time.sleep(0.1)
            say("Skipped the video.")
        elif command == "forward":
            pyautogui.press("right")
            say("Forwarded the video.")
        elif command == "rewind":
            pyautogui.press("left")
            say("Rewound the video.")
        elif command == "stop":
            pyautogui.press("k")
            say("Stopped the video.")
        elif command == "miniplayer":
            pyautogui.press("i")
            say("Entered miniplayer mode.")
        elif command == "close":
            pyautogui.hotkey("ctrl", "w")
            say("Closed the YouTube tab.")

        else:
            say("Invalid command for YouTube control.")
    except Exception as e:
        print("Error controlling YouTube:", e)
