import pytest
from enemys import Goblin, Orc

def test_goblin_initialization():
    assert Goblin.name == "Goblin"
    assert Goblin.life == 10
    assert Goblin.atk == 4
    assert Goblin.defense == 1
    assert "Bite" in Goblin.skills

def test_orc_initialization():
    assert Orc.name == "Orc"
    assert Orc.life == 18
    assert Orc.atk == 7
    assert Orc.defense == 3
    assert Orc.lvl == 2
    assert "Smash" in Orc.skills

def test_enemy_attributes():
    # Test that both enemies have required attributes
    for enemy in [Goblin, Orc]:
        assert hasattr(enemy, 'name')
        assert hasattr(enemy, 'life')
        assert hasattr(enemy, 'atk')
        assert hasattr(enemy, 'defense')
        assert hasattr(enemy, 'skills')
        assert hasattr(enemy, 'inventory')
