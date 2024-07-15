import pyttsx3
import speech_recognition as sr

import eel
import time




# initializing engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)     

# text to speech 
def speak(audio):
    audio = str(audio)
    eel.DisplayMessage(audio)
    
    engine.say(audio)
    eel.receiverText(audio)
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
def allCommands(message=1):
    if message == 1:
        query = takecommand().lower()
        
        print( query)
        eel.senderText(query)
      
    else:
        query = message
        eel.senderText(query)
    try:
         
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query :
            from engine.features import playYoutube
            playYoutube(query)
        else:
            from engine.features import chatBot
            chatBot(query)
            
        while True:

            if "you can stop now" in query:
                eel.DisplayMessage("Thank you sir, and have a great day!")
                speak('Thank you sir, and have a great day!')
                eel.showHood()
                break
            if "goodbye" in query:
                eel.DisplayMessage("dont call me for this silly type questions unless its for NASA")
                speak('dont call me for this silly type questions unless its for NASA')
                eel.showHood()
                break
            else:
                query = takecommand().lower()
                print( query)
                allCommands(query)
            break
        
    except:
        print("Error")
    eel.showHood()
