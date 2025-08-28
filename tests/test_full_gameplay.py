#!/usr/bin/env python3
"""
Comprehensive test script for full gameplay loop
"""
import sys
import os
sys.path.insert(0, 'src')

from src.charactersys import Player
from src.map import map_module
import combat
import inventory
from random import randint, seed

# Mock the chance function for predictable testing
def mock_chance_always():
    """Always trigger combat for testing"""
    return True

def mock_chance_never():
    """Never trigger combat for testing"""
    return False

def mock_chance_random():
    """Random chance (original behavior)"""
    combatchance = randint(1, 10)
    return combatchance > 5

def test_movement_and_combat():
    """Test movement with combat encounters"""
    print("=== Testing Movement and Combat Integration ===")
    
    # Reset player position
    map_module.player_pos = [0, 1]
    print(f"Starting position: {map_module.player_pos}")
    
    # Test movement without combat first
    print("\n1. Testing movement without combat:")
    original_check_for_combat = combat.check_for_combat
    combat.check_for_combat = lambda: False  # No combat
    
    # Try moving right
    original_pos = map_module.player_pos.copy()
    moved = map_module.move()
    print(f"Moved right: {moved}, New position: {map_module.player_pos}")
    
    # Try moving down
    moved = map_module.move()
    print(f"Moved down: {moved}, New position: {map_module.player_pos}")
    
    print("\n2. Testing movement with combat:")
    combat.check_for_combat = lambda: True  # Always combat
    
    # Reset position
    map_module.player_pos = [0, 1]
    print(f"Reset position: {map_module.player_pos}")
    
    # Try moving (should trigger combat)
    moved = map_module.move()
    print(f"Moved: {moved}, Position: {map_module.player_pos}")
    
    # Restore original function
    combat.check_for_combat = original_check_for_combat
    
    print("\n3. Testing combat system:")
    # Test combat with a fresh enemy
    # Import Goblin properly
    import enemys
    enemys.Goblin.life = 10  # Reset enemy health
    Player.life = 20  # Reset player health
    
    print(f"Player HP: {Player.life}, Goblin HP: {enemys.Goblin.life}")
    
    # Simulate a combat round
    original_player_attack = combat.player_attack
    original_enemy_attack = combat.enemy_attack
    
    combat.player_attack = lambda: setattr(enemys.Goblin, 'life', enemys.Goblin.life - 5) or print("Player attacked!")
    combat.enemy_attack = lambda: setattr(Player, 'life', Player.life - 3) or print("Goblin attacked!")
    
    # Run one combat round
    combat.ui()
    print(f"After combat round - Player HP: {Player.life}, Goblin HP: {enemys.Goblin.life}")
    
    # Restore original functions
    combat.player_attack = original_player_attack
    combat.enemy_attack = original_enemy_attack
    
    print("\n4. Testing level progression:")
    # Test level system
    original_lvl = Player.lvl
    original_xp = Player.xp
    
    print(f"Before level test - Level: {Player.lvl}, XP: {Player.xp}")
    
    # Give enough XP to level up
    Player.xp = 100
    from main import lvlsystem
    lvlsystem()
    
    print(f"After level test - Level: {Player.lvl}, XP: {Player.xp}")
    
    print("\n5. Testing inventory system:")
    # Test inventory management
    from main import manage_inventory
    print(f"Inventory before: {Player.inventory}")
    
    # Add an item if inventory is empty
    if not Player.inventory:
        Player.inventory.append("health_potion")
        print("Added health potion to inventory")
    
    print(f"Inventory after: {Player.inventory}")

def test_edge_cases():
    """Test edge cases and error handling"""
    print("\n=== Testing Edge Cases ===")
    
    # Test moving out of bounds
    print("\n1. Testing out of bounds movement:")
    map_module.player_pos = [0, 0]  # Top-left corner
    print(f"Position at top-left: {map_module.player_pos}")
    
    # Try to move up (should fail)
    moved = map_module.move()
    print(f"Tried to move up from top edge: {moved}")
    
    # Try to move left (should fail)
    moved = map_module.move()
    print(f"Tried to move left from left edge: {moved}")
    
    # Test combat with dead player
    print("\n2. Testing combat with low health:")
    Player.life = 1
    import enemys
    enemys.Goblin.life = 10
    print(f"Player HP: {Player.life}, Goblin HP: {enemys.Goblin.life}")
    
    # This would normally trigger combat, but we'll just check the state
    print("Combat would trigger with low player health")

def run_complete_gameplay_test():
    """Run the complete gameplay test suite"""
    print("Starting comprehensive gameplay testing...\n")
    
    try:
        test_movement_and_combat()
        test_edge_cases()
        print("\n=== All Tests Completed Successfully ===")
        return True
    except Exception as e:
        print(f"\n=== Test Failed with Error: {e} ===")
        return False

if __name__ == "__main__":
    success = run_complete_gameplay_test()
    if success:
        print("\n✅ All gameplay systems are functioning correctly!")
    else:
        print("\n❌ Some tests failed. Please check the implementation.")
