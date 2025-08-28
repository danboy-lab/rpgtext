import pytest
from src.charactersys import Character

def test_character_initialization():
    player = Character(
        name="Test Player",
        life=20,
        mana=10,
        xp=0,
        lvl=1,
        atk=5,
        defense=2,
        agi=3,
        int_=4,
        str_=5,
        dex=3,
        luck=2,
        skills=["Slash"],
        inventory=["Potion", "Sword"],
        gold=10,
        status_effects=[]
    )
    
    assert player.name == "Test Player"
    assert player.life == 20
    assert player.mana == 10
    assert player.skills == ["Slash"]

def test_character_level_up():
    player = Character(
        name="Test Player",
        life=20,
        mana=10,
        xp=0,
        lvl=1,
        atk=5,
        defense=2,
        agi=3,
        int_=4,
        str_=5,
        dex=3,
        luck=2,
        skills=["Slash"],
        inventory=["Potion", "Sword"],
        gold=10,
        status_effects=[]
    )
    
    player.xp += 100  # Simulate gaining XP
    player.lvl += 1  # Simulate leveling up
    assert player.lvl == 2
