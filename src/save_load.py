import json
import os
import charactersys
from map import player_pos

SAVE_FILE = "savegame.json"

def save_game():
    """
    Save the current game state to a JSON file.
    """
    try:
        # Prepare player data
        player_data = {
            "name": charactersys.Player.name,
            "class": charactersys.Player.class_,
            "lvl": charactersys.Player.lvl,
            "xp": charactersys.Player.xp,
            "life": charactersys.Player.life,
            "mana": charactersys.Player.mana,
            "atk": charactersys.Player.atk,
            "defense": charactersys.Player.defense,
            "agi": charactersys.Player.agi,
            "int_": charactersys.Player.int_,
            "str_": charactersys.Player.str_,
            "dex": charactersys.Player.dex,
            "luck": charactersys.Player.luck,
            "base_atk": charactersys.Player.base_atk,
            "base_defense": charactersys.Player.base_defense,
            "base_agi": charactersys.Player.base_agi,
            "base_int_": charactersys.Player.base_int_,
            "base_str_": charactersys.Player.base_str_,
            "base_dex": charactersys.Player.base_dex,
            "base_luck": charactersys.Player.base_luck,
            "inventory": charactersys.Player.inventory,
            "equipment": charactersys.Player.equipment,
            "skills": charactersys.Player.skills,
            "gold": charactersys.Player.gold,
            "status_effects": charactersys.Player.status_effects
        }

        # Prepare map data
        map_data = {
            "player_pos": player_pos
        }

        # Combine all data
        save_data = {
            "player": player_data,
            "map": map_data
        }

        # Write to file
        with open(SAVE_FILE, 'w') as f:
            json.dump(save_data, f, indent=4)

        print("Game saved successfully!")

    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    """
    Load the game state from a JSON file.
    """
    try:
        if not os.path.exists(SAVE_FILE):
            print("No save file found!")
            return False

        with open(SAVE_FILE, 'r') as f:
            save_data = json.load(f)

        # Load player data
        player_data = save_data["player"]
        charactersys.Player.name = player_data["name"]
        charactersys.Player.class_ = player_data.get("class", "fighter")  # Default to fighter if not present
        charactersys.Player.lvl = player_data["lvl"]
        charactersys.Player.xp = player_data["xp"]
        charactersys.Player.life = player_data["life"]
        charactersys.Player.mana = player_data["mana"]
        charactersys.Player.atk = player_data["atk"]
        charactersys.Player.defense = player_data["defense"]
        charactersys.Player.agi = player_data["agi"]
        charactersys.Player.int_ = player_data["int_"]
        charactersys.Player.str_ = player_data["str_"]
        charactersys.Player.dex = player_data["dex"]
        charactersys.Player.luck = player_data["luck"]
        charactersys.Player.base_atk = player_data["base_atk"]
        charactersys.Player.base_defense = player_data["base_defense"]
        charactersys.Player.base_agi = player_data["base_agi"]
        charactersys.Player.base_int_ = player_data["base_int_"]
        charactersys.Player.base_str_ = player_data["base_str_"]
        charactersys.Player.base_dex = player_data["base_dex"]
        charactersys.Player.base_luck = player_data["base_luck"]
        charactersys.Player.inventory = player_data["inventory"]
        charactersys.Player.equipment = player_data["equipment"]
        charactersys.Player.skills = player_data["skills"]
        charactersys.Player.gold = player_data["gold"]
        charactersys.Player.status_effects = player_data["status_effects"]

        # Load map data
        map_data = save_data["map"]
        player_pos[0] = map_data["player_pos"][0]
        player_pos[1] = map_data["player_pos"][1]

        print("Game loaded successfully!")
        return True

    except Exception as e:
        print(f"Error loading game: {e}")
        return False

def has_save_file():
    """
    Check if a save file exists.
    """
    return os.path.exists(SAVE_FILE)
