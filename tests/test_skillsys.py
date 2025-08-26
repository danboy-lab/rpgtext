import pytest
import json
from skillsys import data

def test_skills_data_structure():
    assert "skills" in data
    assert "skill_categories" in data
    assert "version" in data
    
    assert isinstance(data["skills"], dict)
    assert isinstance(data["skill_categories"], list)
    assert isinstance(data["version"], str)

def test_skill_categories():
    expected_categories = ["physical", "magical", "support"]
    assert data["skill_categories"] == expected_categories
    
    for category in expected_categories:
        assert category in data["skills"]
        assert isinstance(data["skills"][category], list)

def test_skill_structure():
    for category in data["skills"]:
        for skill in data["skills"][category]:
            assert "id" in skill
            assert "name" in skill
            assert "description" in skill
            assert "type" in skill
            assert "level_required" in skill
            assert "target" in skill
            
            # Check numeric fields
            assert isinstance(skill["level_required"], int)
            
            # Check type-specific fields
            if skill["type"] in ["physical", "magical"]:
                assert "damage" in skill
                assert isinstance(skill["damage"], int)
                assert "mana_cost" in skill
                assert isinstance(skill["mana_cost"], int)
            elif skill["type"] == "support":
                assert "mana_cost" in skill
                assert isinstance(skill["mana_cost"], int)

def test_slash_skill():
    slash_skill = None
    for skill in data["skills"]["physical"]:
        if skill["name"] == "Slash":
            slash_skill = skill
            break
    
    assert slash_skill is not None
    assert slash_skill["damage"] == 8
    assert slash_skill["mana_cost"] == 0
    assert slash_skill["level_required"] == 1
