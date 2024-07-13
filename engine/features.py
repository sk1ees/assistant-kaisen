import os
import re
from playsound import playsound
import eel
import pywhatkit as pwt
from engine.command import speak
from engine.config import ASSISTANT_NAME
# playAssistantSound function 

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("can you please open", "")
    query.lower()

    if query!="":
        speak("Wait a second...Opening" + query)
        os.system('start' +query)
    else:
        speak("not found")

def playYoutube(query):
    search_term = extract_yt_term(query)
    if search_term!=None:
        speak("Playing " + search_term + " on Youtube")
        pwt.playonyt(search_term);
    else:
        speak("you haven't said what do i search on youtube!")

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None