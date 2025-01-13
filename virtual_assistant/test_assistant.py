import unittest
from unittest.mock import patch
from assistant import main
from speech_recog import listen
from text_to_speech import speak
from commands import parse_command


class TestVirtualAssistant(unittest.TestCase):

    # Test the listen() function
    @patch('speech_recognition.Recognizer.listen')
    @patch('speech_recognition.Recognizer.recognize_google')
    def test_listen(self, mock_recognize_google, mock_listen):
        # Mock the speech recognition output
        mock_listen.return_value = "open calculator"
        mock_recognize_google.return_value = "open calculator"

        command = listen()
        self.assertEqual(command, "open calculator")

    # Test the speak() function
    @patch('pyttsx3.init')
    def test_speak(self, mock_init):
        mock_engine = mock_init.return_value
        speak("Hello!")
        
        # Check if pyttsx3's engine's say method was called
        mock_engine.say.assert_called_with("Hello!")
        mock_engine.runAndWait.assert_called()

    # Test the parse_command() function for 'open calculator'
    def test_parse_command_open_calculator(self):
        response = parse_command("open calculator")
        self.assertEqual(response, "Opening Calculator.")

    # Test the parse_command() function for a joke
    def test_parse_command_joke(self):
        response = parse_command("tell me a joke")
        self.assertIn("Why don't scientists trust atoms?", response)  # Check if joke is returned

    # Test the parse_command() function for time
    def test_parse_command_time(self):
        response = parse_command("what time is it")
        self.assertTrue(response.startswith("The time is"))

    # Test the parse_command() function for unknown command
    def test_parse_command_unknown(self):
        response = parse_command("unknown command")
        self.assertEqual(response, "I didn't understand that command.")

if __name__ == '__main__':
    unittest.main()
