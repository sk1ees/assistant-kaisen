import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 174)     

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Welcome Sir! How can i help you?")