#!/usr/bin/env python3
"""
Test script to verify combat trigger system
"""
import sys
sys.path.insert(0, 'src')

from src.main import check_for_combat, chance
from random import seed

# Test the chance function
print("Testing chance function:")
combat_triggers = 0
total_tests = 100

for i in range(total_tests):
    if chance():
        combat_triggers += 1

print(f"Combat triggered {combat_triggers} out of {total_tests} times ({combat_triggers/total_tests*100:.1f}%)")

# Test check_for_combat function
print("\nTesting check_for_combat function:")
combat_count = 0
for i in range(20):
    if check_for_combat():
        combat_count += 1
        print(f"Combat #{combat_count} triggered!")

print(f"Total combats triggered: {combat_count}/20")
