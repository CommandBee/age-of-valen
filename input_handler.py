from blessed import Terminal

term = Terminal()
ESC = "\x1b"

def handle_keys():
    with term.cbreak(), term.hidden_cursor():
        key = term.getch()  # Get a single key press

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

        return {}