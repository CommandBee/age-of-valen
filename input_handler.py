from blessed import Terminal
term = Terminal()

ESC = "\x1b"
ENTER = "\r"

def handleKeys(key):
    if key == "w":
        return {"move": (0, -1)}
    elif key == "s":
        return {"move": (0, 1)}
    elif key == "a":
        return {"move": (-1, 0)}
    elif key == "d":
        return {"move": (1, 0)}
    
    if key == ESC:
        return {"exit": True}
    
    if key == ENTER:
        return {"refresh": True}

    return {}