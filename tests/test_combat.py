import pytest
from combat import calculate_damage, find_skill_by_name
from charactersys import Character
from enemys import Goblin

def test_calculate_damage():
    attacker = Character(name="Attacker", life=20, mana=10, xp=0, lvl=1, atk=10, defense=2, agi=3, int_=4, str_=5, dex=3, luck=2)
    defender = Goblin  # Using Goblin as the defender
    skill = {"damage": 5, "type": "physical"}
    
    damage = calculate_damage(attacker, defender, skill)
    assert damage >= 1  # Ensure damage is at least 1

def test_calculate_magical_damage():
    attacker = Character(name="Mage", life=20, mana=20, xp=0, lvl=1, atk=5, defense=2, agi=3, int_=10, str_=3, dex=3, luck=2)
    defender = Goblin
    skill = {"damage": 8, "type": "magical"}
    
    damage = calculate_damage(attacker, defender, skill)
    assert damage >= 1

def test_find_skill_by_name():
    skill = find_skill_by_name("Slash")
    assert skill is not None
    assert skill["name"] == "Slash"
    assert skill["type"] == "physical"

def test_find_nonexistent_skill():
    skill = find_skill_by_name("NonexistentSkill")
    assert skill is None
