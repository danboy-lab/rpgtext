"""
Main entry point for RPG Text Adventure
Handles game initialization and main game loop
"""
from dataclasses import dataclass
import charactersys
from map import *
from combat import *
from lvlsys import lvlsystem
from random import randint
from apis import get_random_event_fact
from skillsys import data
from menu import display_main_menu
import random

# Main game initialization
if __name__ == "__main__":
    # Display main menu and get player setup
    game_started = display_main_menu()

    if game_started and charactersys.Player:
        # Update skills_disponiveis based on player level
        for category in data["skills"]:
            for skill in data["skills"][category]:
                if skill["level_required"] <= charactersys.Player.lvl:
                    charactersys.skills_disponiveis.append(skill)

        # Main game loop
        print(f"\n🎮 Welcome, {charactersys.Player.name}! Your adventure begins now...")
        print("Use W/A/S/D to move, I for inventory, SV to save, L to load, Q to quit")

        while True:
            if charactersys.Player.life <= 0:
                print(" YOU DIED "*200)
                display_main_menu()
            r = random.randint(1, 10)
            display_map()
            move()
            if r > 5:
                combat_loop()
                lvlsystem()
            else:
                print("...")
    else:
        print("Game not started. Exiting...")
