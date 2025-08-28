import pytest
from src.charactersys import Character
from src.enemys import Goblin

@pytest.fixture
def test_player():
    return Character(
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

@pytest.fixture
def test_goblin():
    return Goblin
