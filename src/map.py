import sys
import random
from rich.panel import Panel
from rich import print
from rich.console import Console

from showstats import *
from inventory import *
from combat import *
from lvlsys import *

from map_storage import load_maps, save_maps, generate_map

ROWS = 10
COLS = 10

console = Console()

maps_data, map_data = load_maps(ROWS, COLS)

player_pos = [random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]


def display_map():
    tile_symbols = {
        0: ".",
        1: "#",
        2: "T",
        3: "~",
        4: ",",
        5: "^",
    }

    output = []

    for r, row in enumerate(map_data):
        line = ""
        for c, tile in enumerate(row):
            if [r, c] == player_pos:
                line += "[bold red][P][/bold red] "
            else:
                line += f" {tile_symbols.get(tile, '?')} "
        output.append(line)

    print(
        Panel.fit(
            "\n".join(output),
            title="[bold red]RPGTEXT[/bold red]",
            border_style="red"
        )
    )


def move():
    global map_data

    d = input("~>").strip().lower()
    moved = False

    if d == "q":
        save_maps(maps_data)
        sys.exit("Thanks for playing!")

    elif d == "sv":
        from save_load import save_game
        save_game()
        return False

    elif d == "l":
        from save_load import load_game
        load_game()
        return False

    elif d == "i":
        show_inventory()
        return False

    elif d == "o":
        manage_status()
        return False

    elif d == "help":
        from menu import help
        help()
        return False

    r, c = player_pos

    if d == "w":
        if r > 0:
            player_pos[0] -= 1
            moved = True
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] += 1
            map_data = generate_map(ROWS, COLS)
            maps_data["maps"].append(map_data)
            player_pos[0] = ROWS - 1
            moved = True

    elif d == "s":
        if r < len(map_data) - 1:
            player_pos[0] += 1
            moved = True
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] += 1
            map_data = generate_map(ROWS, COLS)
            maps_data["maps"].append(map_data)
            player_pos[0] = 0
            moved = True

    elif d == "a":
        if c > 0:
            player_pos[1] -= 1
            moved = True
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] -= 1 if maps_data["current"] > 0 else 0
            map_data = maps_data["maps"][maps_data["current"]]
            player_pos[1] = COLS - 1
            moved = True

    elif d == "d":
        if c < len(map_data[0]) - 1:
            player_pos[1] += 1
            moved = True
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] += 1
            map_data = generate_map(ROWS, COLS)
            maps_data["maps"].append(map_data)
            player_pos[1] = 0
            moved = True

    if moved:
        save_maps(maps_data)
        console.clear()

        if random.randint(1, 100) <= 30:
            combat_loop()
            lvlsystem()

    return moved
