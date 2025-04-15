# main.py

import pyttsx3
from audio_recognition import listen_for_command
from command_processor import process_command
from config import WAKE_WORD

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the assistant's response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Entry point of the voice assistant
# Listens for the wake word, processes commands when triggered
def main():
    speak("Voice Assistant is listening...")  # Initial prompt via text-to-speech
    print("Voice Assistant is listening...")

    while True:
        # Listen for voice input
        text = listen_for_command()

        if text:
            print(f"User said: {text}")
            
            # Check if wake word is in the transcribed text
            if WAKE_WORD in text.lower():
                # Remove the wake word from the command
                command = text.lower().replace(WAKE_WORD, "").strip()
                print(f"Processing command: {command}")

                # Process the command
                response = process_command(command)
                
                if response:
                    speak(response)  # Speak out the response
            else:
                speak("Sorry, I didn’t catch that. Please say the wake word to begin.")
        else:
            speak("Sorry, I didn’t catch that. Please try again.")

if __name__ == "__main__":
    main()
