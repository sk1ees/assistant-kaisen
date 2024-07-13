import pyttsx3
import speech_recognition as sr

import eel
import time
# initializing engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 140)     

# text to speech 
def speak(audio):
    eel.DisplayMessage(audio)
    
    engine.say(audio)
    
    engine.runAndWait()

# converting text to speech 
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        # eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5 , phrase_time_limit=5)

    try:
        print("Recognizing...")
        # eel.DisplayMessage("Recognizing...")
        query  =r.recognize_google(audio , language = 'en-in')
        eel.DisplayMessage(query)
        time.sleep(2)
        
        # eel.showHood()

    except Exception as e:
        
        speak("you haven't said a word..please talk!")
        return ""
    return query

@eel.expose
def allCommands():
    while True:
        try:
            query = takecommand().lower()
            print( query)
            if "you can stop now" in query:
                eel.DisplayMessage("Thank you sir, and have a great day!")
                speak('Thank you sir, and have a great day!')
                eel.showHood()
                break
            if "open" in query:
                from engine.features import openCommand
                openCommand(query)

            if "on youtube" in query :
                from engine.features import playYoutube
                playYoutube(query)
        except:
            print("Error")
