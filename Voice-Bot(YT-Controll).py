import speech_recognition as sr
import pyaudio
import webbrowser
import os
# import pyttsx3
import pyautogui as gui
import pyperclip
from Open_App import open_app
import hand_control

def sttxt():
    global text
    while True:
        try:
            with sr.Microphone() as mic:
                # print("Adjusting your mic...")
                # r.adjust_for_ambient_noise(mic)
                print("---Speak---")
                audio = r.listen(mic)
                text = r.recognize_google(audio)
                text = text.lower()

                if text.lower() == "exit":
                    print("Exit Programm")
                    break
                else:
                    runcheak()
        except:
            print("Didn't listen")

def runcheak():
    try :
        words = text.split()
        if words[0] == "python":
            print(f"Yes Sir")
            print(text)

            if len(words) > 2 and words[2] in open_app.keys():
                webbrowser.open(open_app[words[2]])
            elif words[1] == "search":
                gui.moveTo(705, 61, duration= 1)
                gui.click(705, 61 , duration=1)
                search()
            elif words[1] == "scroll":
                gui.moveTo(1350, 310 , duration=1)
                if len(words) > 2 and words[2] == "up":
                    gui.scroll(700)
                if len(words) > 2 and words[2] == "down":
                    gui.scroll(-700)
            elif words[1] == "youtube" and words[2] == "search" :
                gui.moveTo(813 , 108 , duration=1)
                gui.click(813 , 108)
                gui.hotkey("ctrl","a")
                gui.press("backspace")
                search()
            elif words[2]=="hand" and words[3] == "control":
                hand_control.full_control()
                pass
        else:
            print(f"You said: {text}")
    except:
        print("Error While Runing The Code")

def search():
    try:
       with sr.Microphone() as mic:
            # print("Adjusting your mic...")
            # r.adjust_for_ambient_noise(mic)
            print("---Speak---")
            audio = r.listen(mic)
            search_text = r.recognize_google(audio)
            pyperclip.copy(search_text)
            gui.hotkey("ctrl" , "v")
            gui.press("enter")
    except:
        print("error")
        
r = sr.Recognizer()
# engin = pyttsx3.init()

sttxt()

