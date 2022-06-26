import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import os
import datetime
from time import strftime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)


def speak(message):
    engine.say(message)
    engine.runAndWait()


def wishme():
    hr = int(datetime.datetime.now().hour)
    if hr >= 6 and hr < 12:
        speak('Good Morning!!')
    elif hr >= 12 and hr < 16:
        speak('Good Afternoon')
    elif hr >= 16:
        speak('Good Evening ')


def takeorders():
    R = sr.Recognizer()
    with sr.Microphone() as src:
        print("Listening...")
        R.pause_threshold = 1
        audio = R.listen(src)
        try:
            print("Recogning...")
            query = R.recognize_google(audio, language='en-in')
            print(query)
            return query
        except Exception as e:
            print("Say That Again Please!!")
            return "none"


if __name__ == '__main__':
    wishme()
    while True:
        query = takeorders().lower()
        if 'wikipedia' in query:
            query = query.replace('wikipedia', '')
            result = wp.summary(query, sentences=2)
            speak("According to wikipedia" + result)
            print(result)

        if 'open google' in query:
            wb.register('chrome',None,wb.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
            wb.get('chrome').open('https://www.google.com')

        if 'open youtube' in query:
            wb.register('chrome',None,wb.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
            wb.get('chrome').open('https://www.youtube.com')

        if 'open visual studio code' in query or 'open vs code' in query:
            path = "C:/Users/my pc/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(path)

        if 'time' in query:
            h = int(datetime.datetime.now().strftime('%H'))
            m = int(datetime.datetime.now().strftime('%M'))
            ampm = str((('am' , 'pm')[h >= 12 and h < 24]))
            speak('The time is' + str(h%12) + ampm + str(m) + 'minutes')
            print(ampm)

        if 'exit' in query:
            speak("Thankyou for using desktop assistant")
            quit()


