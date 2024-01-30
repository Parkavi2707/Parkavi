#Requied packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listener=sr.Recognizer()
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voices', voice[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening............")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        print(f"An error occurred: {e}")

    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Searching for ' + song + ' on YouTube.')
        url = f"https://www.youtube.com/results?search_query={song}"
        webbrowser.open(url)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S')
        talk('Current time ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

run_alexa()

