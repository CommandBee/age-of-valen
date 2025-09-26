from blessed import Terminal
term = Terminal()

from render import gameRefresh, printDialog, printStats
from input_handler import handleKeys

PLAYER = term.green_on_black('@')

def main():

    SCR_W: int = 80
    SCR_H: int = 19

    player_x: int = int(SCR_W / 2)
    player_y: int = int(SCR_H / 2)

    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        background = [[term.on_black(" ") for _ in range(SCR_W)] for _ in range(SCR_H)]
        entity = [[" " for _ in range(SCR_W)] for _ in range(SCR_H)]
        player = [[" " for _ in range(SCR_W)] for _ in range(SCR_H)]

        player[player_y][player_x] = PLAYER # Initalise player to screen

        entity[5][8] = term.yellow_on_black('$') # Add a item to the screen

        background[7][10] = term.on_black("#")
        background[7][11] = term.on_black("#")

        background[7][11] = collide = True

        background[7][13] = term.on_black("y")

        gameRefresh(background, entity, player)

        printStats()
        printDialog('Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet consectetur adipiscing elit quisque faucibus.', max_width= SCR_W)

        while True:
            action = handleKeys(term.getch())

            move = action.get("move")
            exit = action.get("exit")
            refresh = action.get("refresh")

            if move:
                dx, dy = move
                player[player_y][player_x] = ' '

                new_x = player_x + dx
                new_y = player_y + dy

                if 0 <= new_x < SCR_W and 0 <= new_y < SCR_H:
                    if background[new_y][new_x] != collide:
                        player_x, player_y = new_x, new_y
                    
                player[player_y][player_x] = PLAYER
                gameRefresh(background, entity, player)

            if exit:
                break

            if refresh:
                printDialog('Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet consectetur adipiscing elit quisque faucibus.', max_width= SCR_W)
        

if __name__ == "__main__":
    main()