# command_handler.py
import os
import random
from datetime import datetime

def parse_command(command):
    if 'open calculator' in command:
        open_application('calc')
        return "Opening Calculator."
    elif 'open clock' in command:
        open_application('start ms-clock:')
        return "Opening Clock."
    elif 'open camera' in command:
        open_application('start microsoft.windows.camera:')
        return "Opening Camera."
    elif 'open calendar' in command:
        open_application('start outlookcal:')
        return "Opening Calendar."
    elif 'tell me a joke' in command:
        return tell_joke()
    elif 'what time is it' in command:
        return f"The time is {get_current_time()}."
    elif 'open notepad' in command:
        open_application('notepad')
        return "Opening Notepad."
    elif 'exit' in command:
        return "Goodbye!"
    else:
        return "I didn't understand that command."

def open_application(app_name):
    os.system(app_name)  # Runs the system app (e.g., calculator)

def tell_joke():
    jokes =  "Why don't scientists trust atoms? Because they make up everything!"
    return jokes
def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")
