# command_handler.py
import os
import random
from datetime import datetime

def parse_command(command):
    if 'open calculator' in command:
        open_application('calc')
        return "Opening Calculator."
    elif 'tell me a joke' in command:
        return tell_joke()
    elif 'what time is it' in command:
        return f"The time is {get_current_time()}."
    elif 'set reminder' in command:
        return "Reminder feature coming soon!"
    elif 'exit' in command:
        return "Goodbye!"
    else:
        return "I didn't understand that command."

def open_application(app_name):
    os.system(app_name)  # Runs the system app (e.g., calculator)

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats."
    ]
    return random.choice(jokes)

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
