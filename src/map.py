import sys
import time
from showstats import *
from inventory import *
import random
from combat import *
from lvlsys import *
import json
import os

def generate_map(rows=5, cols=5, min_val=0, max_val=5):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

ROWS = 10
COLS = 10

DATA_DIR = "data"
MAPS_FILE = os.path.join(DATA_DIR, "maps.json")

os.makedirs(DATA_DIR, exist_ok=True)

if os.path.exists(MAPS_FILE):
    with open(MAPS_FILE, "r") as f:
        maps_data = json.load(f)
else:
    maps_data = {"maps": [], "current": 0}

if not maps_data["maps"]:
    map_data = generate_map(ROWS, COLS)
    maps_data["maps"].append(map_data)
else:
    map_data = maps_data["maps"][maps_data["current"]]

player_pos = [random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]

def save_maps():
    with open(MAPS_FILE, "w") as f:
        json.dump(maps_data, f)

def display_map():
    tile_symbols = {
        0: ".",
        1: "#",
        2: "T",
        3: "~",
        4: ",",
        5: "^",
    }
    print("\n=== RPG MAP ===")
    for r, row in enumerate(map_data):
        for c, tile in enumerate(row):
            if [r, c] == player_pos:
                print("[P]", end=" ")
            else:
                symbol = tile_symbols.get(tile, "?")
                print(f" {symbol} ", end=" ")
        print()

def move():
    global map_data
    print("In case you dont know what to do, maybe you shall try help command")
    d = input("~>").strip().lower()
    if d == 'q':
        save_maps()
        return sys.exit("Thanks for playing!")
    elif d == 'sv':
        from save_load import save_game
        save_game()
        return True
    elif d == 'l':
        from save_load import load_game
        load_game()
        return True
    elif d == 'i':
        show_inventory()
        return True
    elif d == 'o':
        manage_status()
    elif d == 'help':
        from menu import help
        help()

    r, c = player_pos

    if d == 'w':
        if r > 0:
            player_pos[0] -= 1
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] += 1
            map_data = generate_map(ROWS, COLS)
            maps_data["maps"].append(map_data)
            player_pos[0] = ROWS - 1
            save_maps()
            return True
    elif d == 's':
        if r < len(map_data) - 1:
            player_pos[0] += 1
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] += 1
            map_data = generate_map(ROWS, COLS)
            maps_data["maps"].append(map_data)
            player_pos[0] = 0
            save_maps()
            return True
    elif d == 'a':
        if c > 0:
            player_pos[1] -= 1
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] -= 1 if maps_data["current"] > 0 else 0
            map_data = maps_data["maps"][maps_data["current"]]
            player_pos[1] = COLS - 1
            save_maps()
            return True
    elif d == 'd':
        if c < len(map_data[0]) - 1:
            player_pos[1] += 1
        else:
            maps_data["maps"][maps_data["current"]] = map_data
            maps_data["current"] += 1
            map_data = generate_map(ROWS, COLS)
            maps_data["maps"].append(map_data)
            player_pos[1] = 0
            save_maps()
            return True
    else:
        print("Invalid movement.")
        return False

    if random.randint(1, 100) <= 30:
        combat_loop()
        lvlsystem()
        time.sleep(1)
        return True
