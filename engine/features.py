import os
import re
import sqlite3
import webbrowser
from playsound import playsound
import eel
import pywhatkit as pwt
from engine.command import speak
from engine.config import ASSISTANT_NAME
# playAssistantSound function 
conn = sqlite3.connect("assistant.db")

cursor = conn.cursor()
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("can you please open", "")
    query.lower()

    app_name = query.strip()
    if app_name!="":
        try:
            cursor.execute(
                'SELECT path FROM sys_commands WHERE name IN (?)',(app_name,))
            results = cursor.fetchall()

            if len(results)!=0: 
                speak('Opening ' + query)
                os.startfile(results[0][0])

            elif len(results)==0:
                cursor.execute(
                    'SELECT url FROM web_commands WHERE name IN (?)',(app_name,))
                results = cursor.fetchall()
                
                if len(results)!=0:
                    speak('Opening ' + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening" +query)
                    try:
                        os.system('start' + query)
                    except:
                        speak("not found")
        except:
            speak("something went wrong")

            

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