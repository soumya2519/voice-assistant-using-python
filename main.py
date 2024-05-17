'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Sorry, my speech service is down."

def main():
    speak("Hello! How can I help you today?")
    while True:
        command = listen()
        print(f"You said: {command}")
        if 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye!")
            break
        elif 'hello' in command:
            speak("Hello! How are you?")
        elif 'your name' in command:
            speak("I am your voice assistant.")
        else:
            speak("I am sorry, I don't know how to respond to that.")

if __name__ == "__main__":
    main()
