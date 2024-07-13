import pyttsx3
import speech_recognition as sr
import eel
# initializing engine 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 174)     

# text to speech 
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
@eel.expose
# converting text to speech 
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=5 , phrase_time_limit=5)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query  =r.recognize_google(audio , language = 'en-in')
        eel.DisplayMessage(query)
        speak(query)
        eel.showHood()

    except Exception as e:
        speak("you haven't said a word..please talk!")
        return ""
    return query.lower()



# if __name__ == '__main__':
#     while True:
#         text = takecommand().lower()
#         if "you can stop now" in text:
#             speak('Thank you sir, and have a great day!')
#             break