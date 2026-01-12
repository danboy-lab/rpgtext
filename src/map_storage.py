import json
import os
import random

DATA_DIR = "data"
MAPS_FILE = os.path.join(DATA_DIR, "maps.json")


def generate_map(rows, cols, min_val=0, max_val=5):
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def load_maps(rows, cols):
    os.makedirs(DATA_DIR, exist_ok=True)

    if os.path.exists(MAPS_FILE):
        try:
            with open(MAPS_FILE, "r") as f:
                maps_data = json.load(f)
        except json.JSONDecodeError:
            maps_data = {}
    else:
        maps_data = {}

    if not isinstance(maps_data, dict):
        maps_data = {}

    maps_data.setdefault("maps", [])
    maps_data.setdefault("current", 0)

    if maps_data["current"] >= len(maps_data["maps"]):
        maps_data["current"] = max(0, len(maps_data["maps"]) - 1)

    if not maps_data["maps"]:
        map_data = generate_map(rows, cols)
        maps_data["maps"].append(map_data)
        maps_data["current"] = 0
    else:
        map_data = maps_data["maps"][maps_data["current"]]

    return maps_data, map_data


def save_maps(maps_data):
    with open(MAPS_FILE, "w") as f:
        json.dump(maps_data, f)
