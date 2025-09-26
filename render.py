from blessed import Terminal
term = Terminal()

import textwrap, time, json


def printDialog(sentence: str, max_width: int):
    wrapped = textwrap.fill(text= sentence, width= max_width)
    print(term.move_xy(0,1) + term.clear_eol, end="", flush=True)
    print(term.home + term.clear_eol, end="", flush=True)

    for char in wrapped:
        print(char, end="", flush=True)
        time.sleep(0.01)


def loadStats(filename="stats.json"):
    with open(filename, "r") as f:
        return json.load(f)

def printStats(filename="stats.json"):
    stats = loadStats(filename)

    # Combat stats
    health_cur = stats["health"]["current"]
    health_max = stats["health"]["max"]

    xp_cur = stats["xp"]["current"]
    xp_max = stats["xp"]["max"]

    level = stats.get("level", 0)
    armor = stats.get("armor", 0)
    perception = stats.get("perception", 0)

    # Abilities
    abilities = stats.get("abilities", {})
    str_ = abilities.get("str", 0)
    dex = abilities.get("dex", 0)
    con = abilities.get("con", 0)
    int_ = abilities.get("int", 0)
    wis = abilities.get("wis", 0)
    cha = abilities.get("cha", 0)

    # Print two rows
    print(f"{term.move_xy(0, 21)}"
          f"HP: {health_cur}({health_max}) "
          f"Lv: {level} "
          f"Exp: {xp_cur}({xp_max}) "
          f"AC: {armor} "
          f"Pe: {perception}")

    print(f"Str:{str_} Dex:{dex} Con:{con} "
          f"Int:{int_} Wis:{wis} Cha:{cha}")


def gameRefresh(background: list[list[str]], entity: list[list[str]], player: list[list[str]]):

    scr: list[list[str]] = [
        [entity[y][x] if entity[y][x] != ' ' else background[y][x]
         for x in range(len(background[0]))]
        for y in range(len(background))
    ]

    scr = [
        [player[y][x] if player[y][x] != ' ' else scr[y][x]
         for x in range(len(scr[0]))]
        for y in range(len(scr))
    ]

    print(term.move_xy(0,2), end="", flush=True)

    for row in scr:
        print(''.join(row), flush=True)



