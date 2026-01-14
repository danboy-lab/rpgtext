import json
import os
import charactersys as cs
from rich import print
import rich.console
import inventory

"""Camping module for RPG Text Game."""
# Initialize Player character
# TODO : Load player data from a save file
# FIX : Set base stats for player
# This cs.Player above is temporary for testing purposes

cs.Player = cs.Character(
    name="Hero",
    class_="mage",
    life=100,
    mana=50,
    xp=0,
    lvl=1,
    atk=10,
    defense=5,
    agi=5,
    int_=5,
    str_=5,
    dex=5,
    luck=5,
    skills=["Slash", "Block"],
    inventory=["red_potion", "blue_potion"],
    gold=20,
    status_effects=[],
    equipment={
        "weapon": None,
        "armor": None,
        "accessory": None
    }
)

def fish():
    inventory.add_inventory_item("common_fish")
def train():
    if cs.Player.class_ == "mage":
        cs.Player.int_ += 1
        print("You trained your Intelligence! Current Intelligence:", cs.Player.int_)
    elif cs.Player.class_ == "rogue":  
        cs.Player.agi += 1
        print("You trained your Agility! Current Agility:", cs.Player.agi)
    elif cs.Player.class_ == "warrior":
        cs.Player.str_ += 1
        print("You trained your Strength! Current Strength:", cs.Player.str_)
    
def sleep():
    print("Sleeping action not yet implemented.")

def read():
    locations_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'locations.json')
    with open(locations_path, 'r', encoding='utf-8') as f:
        locations_data = json.load(f)
        locations = locations_data['locations']
        display_location = locations_data['display_location']
    return locations, display_location

def actions():
    locations, display_location = read()
    console = rich.console.Console()
    console.print(f"{display_location[0]}")
    player_chose = str(input("Train: 1\nFishing: 2\nSleep: 3\n~>"))
    if player_chose == "1":
        print("You chose to train.")
        train()
    elif player_chose == "2":
        print("You chose to fish.")
        fish()
    elif player_chose == "3":
        sleep()
        print("You chose to sleep.")
    else:
        print("Invalid choice.")
