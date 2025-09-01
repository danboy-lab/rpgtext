import json
import random
import os

# Read locations.json
locations_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'locations.json')
with open(locations_path, 'r', encoding='utf-8') as f:
    locations_data = json.load(f)

locations = locations_data['locations']

# Generate maps
maps = {}
for location in locations:
    rows = 10
    cols = 10
    map_data = [[random.randint(0, 5) for _ in range(cols)] for _ in range(rows)]
    player_pos = [random.randint(0, rows - 1), random.randint(0, cols - 1)]
    maps[location] = {
        "rows": rows,
        "cols": cols,
        "map_data": map_data,
        "player_pos": player_pos
    }

# Write to maps.json
maps_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'maps.json')
with open(maps_path, 'w', encoding='utf-8') as f:
    json.dump(maps, f, indent=4, ensure_ascii=False)

print("Maps generated and saved to maps.json")
