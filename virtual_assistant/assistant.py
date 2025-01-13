from speech_recog import listen
from text_to_speech import speak
from commands import parse_command

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if command:
            response = parse_command(command)
            speak(response)
        if 'exit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()