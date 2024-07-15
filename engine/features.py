import os
import re
import sqlite3
import struct
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
import pywhatkit as pwt
import pvporcupine
from engine.command import speak
from engine.config import ASSISTANT_NAME
from engine.helper import extract_yt_term
from hugchat import hugchat


# playAssistantSound function 
conn = sqlite3.connect("assistant.db")

cursor = conn.cursor()
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\starting.wav"
    playsound(music_dir)
@eel.expose
def playSiriSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

# added open-command with the help of sqlite database
def openCommand(query):
    query = query.replace("can you please", "")
    query = query.replace("open", "")
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
# added search-query function to play on youtube 
def playYoutube(query):
    search_term = extract_yt_term(query)
    if search_term!=None:
        speak("Playing " + search_term + " on Youtube")
        pwt.playonyt(search_term);
    else:
        speak("you haven't said what do i search on youtube!")
# added hotword-key-detection
def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        # trained-keywords 
        porcupine = pvporcupine.create(keywords=["jarvis","alexa"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        # streaming loop 
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from the mic 
            keyword_index = porcupine.process(keyword)

            # checking first keyword detected for not 
            if keyword_index>=0:
                print("hotword detected")

                # presssing shortcut key 
                import pyautogui as autogui
                autogui.keyDown('win')
                autogui.press('j')
                time.sleep(2)
                autogui.keyUp('win')
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
# chatbot 
def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response =  chatbot.chat(user_input)
    print(response)
    speak(response)
    return response