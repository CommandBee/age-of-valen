from input_handler import handle_keys

import os
from blessed import Terminal

term = Terminal()
ESC = "\x1b"

def main() -> None:
    screen_width: int = 80
    screen_height: int = 24

    player_x:int = screen_width // 2
    player_y:int = screen_height // 2

    with term.fullscreen(), term.cbreak():
        key = None

        print(f"{term.home()}{term.white_on_black}{term.clear}", end='')
        print(term.move_xy(player_x, player_y) + "@", end='')                          # Initialise a player

        while True:
            action = handle_keys()
            
            move = action.get("move")
            exit = action.get("exit")

            if move:
                dx, dy = move
                print(term.move_xy(player_x, player_y) + " ", end='')                   # Removes Players Prev Position
                player_x += dx
                player_y += dy
                print(term.move_xy(player_x, player_y) + "@", end='')                   # Refresh Player
            
            if exit:
                break



    

if __name__ == "__main__":
    main()