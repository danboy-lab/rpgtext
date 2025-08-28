from dataclasses import dataclass
from charactersys import Player  # Import the Player instance from charactersys
from map import *
from combat import *
from lvlsys import lvlsystem
from random import randint

while True:
    r = random.randint(1, 10)
    display_map()
    move()
    if r > 5:
        # print(r) DEBUG PORPUSES
        combat_loop()
        lvlsystem()
    else:
        # print(r) # DEBUG PORPUSES
        None
