import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os   
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("How can i help you?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("....")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if "stop" in query or "ok bye" in query:
            speak("Shutting down")
            print("Shutting down...")
            break

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Here is your request")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Here is your request")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Here is your request")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("Here is your request")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com/login")
            speak("Here is your request")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
        
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
