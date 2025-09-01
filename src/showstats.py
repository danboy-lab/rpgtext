import charactersys
from enemys import *

def manage_status():
    def show_status(subject):
        status = f"""
================= [ {subject.__class__.__name__.upper()} STATUS ] =================
 Name:            {subject.name}
 Level:           {subject.lvl}
 XP:              {subject.xp}
 Gold:            {subject.gold}

------------------ ATTRIBUTES -----------------------
 Agility:         {subject.agi}
 Attack:          {subject.atk}
 Defense:         {subject.defense}
 Dexterity:       {subject.dex}
 Intelligence:    {subject.int_}
 Luck:            {subject.luck}

------------------ RESOURCES ------------------------
 Life Points:     {subject.life}
 Mana:            {subject.mana}

------------------ EQUIPMENT ------------------------
 Inventory:       {subject.inventory}

------------------ SKILLS ---------------------------
 Skills:          {subject.skills}

------------------ STATUS EFFECTS -------------------
 Effects:         {subject.status_effects}
=====================================================
"""
        print(status)

    while True:
        try:
            which = int(input("You want see: My Status [1] Enemy Status [2] Back [3] "))
        except ValueError:
            print("Please, enter a valid number (1, 2 or 3).")
            continue

        if which == 1:
            show_status(charactersys.Player)
        elif which == 2:
            # Se tiver vários inimigos, basta colocar em uma lista:
            enemies = [Goblin, Orc]
            for enemy in enemies:
                show_status(enemy)
        elif which == 3:
            print("Ok, going back...")
            break
        else:
            print("Invalid option. Try again.")
