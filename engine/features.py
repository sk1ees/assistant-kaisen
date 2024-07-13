from playsound import playsound
import eel
# playAssistantSound function 

@eel.expose

def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)