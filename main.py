'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine as e
e = pyttsx3.init()

def speak(text):
    e.say(text)
    e.runAndWait()

def listen():
  # Initializing recognizer as re
    re = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = re.listen(source)
        try:
            command = re.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Sorry, my speech service is down."

def main():
    speak("Hello! How can I help you today?")
    while True:
      # intialising command as c
        c = listen()
        print(f"You said: {c}")
        if 'exit' in c or 'quit' in c or 'stop' in c:
            speak("Goodbye!")
            break
        elif 'hello' in c:
            speak("Hello! How are you?")
        elif 'your name' in c:
            speak("I am your voice assistant.")
        else:
            speak("I am sorry, I don't know how to respond to that.")

if __name__ == "__main__":
    main()
