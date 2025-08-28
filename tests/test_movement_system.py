#!/usr/bin/env python3
"""
Test script to verify the complete movement and combat system
"""
import sys
sys.path.insert(0, 'src')

from src.map import move, player_pos, display_map
import msvcrt

def simulate_key_press(key):
    """Simulate a key press for testing"""
    # This is a simplified simulation - in real usage, msvcrt.getch() would capture the actual key
    return key.lower()

def test_movement():
    print("Testing movement system:")
    print(f"Initial position: {player_pos}")
    
    # Test valid movements
    test_moves = ['w', 'a', 's', 'd']
    for move_key in test_moves:
        print(f"\nTesting move '{move_key}':")
        # Simulate the key press
        result = move()
        print(f"Move result: {result}, New position: {player_pos}")
    
    # Test invalid movement (try to move out of bounds)
    print(f"\nTesting invalid move (out of bounds):")
    # Reset to corner position
    player_pos[0] = 0
    player_pos[1] = 0
    print(f"Reset position to: {player_pos}")
    result = move()  # Try to move left (should fail)
    print(f"Move result: {result}, Position: {player_pos}")

if __name__ == "__main__":
    test_movement()
