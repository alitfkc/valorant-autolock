import gui
import threading
from pynput import keyboard
import win32gui
import pyautogui
import re
#Global Arg
keys = []
selected_key = ""
running = False
lis = ""
controller = False
screen_width, screen_height = pyautogui.size()


def save_settings():
    key_and_char = gui.keys_chars.get(1.0, "end-1c")
    value = key_and_char.split(',')
    global  keys
    keys = []
    for v in value:
        try:
            key, char = v.split("-")

            keys.append([ key.lower(),char.lower()])
        except:
            print("Hatalı işlem")
    print(keys)
    th = threading.Thread(target = mode_status)

    th.start()



def mode_status():
    global running 
    running = True
    if running:
        start_mode()


def stop_click(key):
    pushed_key = ""
    try:
        pushed_key =  key.char
    except AttributeError:
        pushed_key =  key.name
    if pushed_key == selected_key:
        return False
    
def click_object(char):
    with keyboard.Listener(on_press=stop_click) as listener2:
        while True:
            if not listener2.running:
                stop()
                break
            else:
                numbers = re.findall(r'\d+', char)
                numbers = [int(number) for number in numbers]
                intege = numbers[0]
                if intege <= 11:
                    intege = 0.24+(intege * 0.045)
                    pyautogui.moveTo(screen_width*intege,screen_height*0.85)
                    pyautogui.click(screen_width*intege,screen_height*0.85)
                    pyautogui.moveTo(screen_width*0.5,screen_height*0.75)
                    pyautogui.click(screen_width*0.5,screen_height*0.75)
                else:
                    intege = intege - 10
                    intege = 0.24+(intege * 0.04)
                    pyautogui.moveTo(screen_width*intege,screen_height*0.94)
                    pyautogui.click(screen_width*intege,screen_height*0.85)
                    pyautogui.moveTo(screen_width*0.5,screen_height*0.75)
                    pyautogui.click(screen_width*0.5,screen_height*0.75)
                    




def on_press(key):
    global running
    if running:
        pushed_key = ""
        try:
            pushed_key =  key.char
        except AttributeError:
            pushed_key =  key.name
        global selected_key 
        selected_key = pushed_key
        for k,c in keys:
            if k == pushed_key:
                click_object(c)
                return False




def stop():
    global selected_key 
    selected_key = ""
    global controller
    controller = True
    controller = False
    th = threading.Thread(target = mode_status)
    th.start()


def start_mode():
    with keyboard.Listener(on_press=on_press) as listener:
        global lis
        lis = listener
        listener.join()











