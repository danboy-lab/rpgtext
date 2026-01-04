import random
from copy import deepcopy

import charactersys
from enemys import Goblin, Orc, Skeleton, Slime
from skillsys import data
from apis import get_random_enemy_name, get_enemy_taunt, get_attack_reaction, get_defeat_phrase
from inventory import ITEMS, show_inventory

# List of available enemies
ENEMIES = [Goblin, Orc, Skeleton, Slime]


def select_random_enemy():
    """Select a random enemy based on player level, using weighted probability."""
    player_lvl = charactersys.Player.lvl

    weights = []
    for enemy in ENEMIES:
        level_diff = abs(player_lvl - enemy.lvl)
        if level_diff == 0:
            weight = 80
        elif level_diff == 1:
            weight = 15
        else:
            weight = 5
        weights.append(weight)

    return random.choices(ENEMIES, weights=weights, k=1)[0]


def get_available_skill_names():
    """Return a list of skills available to the player at their current level."""
    return [
        skill["name"]
        for category in data["skills"].values()
        for skill in category
        if skill["level_required"] <= charactersys.Player.lvl
    ]


def find_skill_by_name(skill_name):
    """Find a skill by name."""
    for category in data["skills"].values():
        for skill in category:
            if skill["name"].lower() == skill_name.lower():
                return skill
    return None


def calculate_damage(attacker, defender, skill):
    """Calculate the damage based on the attack type."""
    base_damage = skill.get("damage", 0)
    if skill["type"] == "physical":
        damage = base_damage + attacker.atk - defender.defense
    elif skill["type"] == "magical":
        damage = base_damage + attacker.int_ - defender.defense
    else:
        damage = base_damage
    return max(1, damage)


def player_attack(current_enemy):
    print("\nYou take the initiative!")
    skills = get_available_skill_names()
    print(f"Available skills: {', '.join(skills)}")

    action = input("Which attack do you want to use? ").strip().capitalize()
    skill = find_skill_by_name(action)

    if not skill or action not in skills:
        print("You don't have that skill!")
        return

    if charactersys.Player.mana < skill["mana_cost"]:
        print("Not enough mana!")
        return

    charactersys.Player.mana -= skill["mana_cost"]
    damage = calculate_damage(charactersys.Player, current_enemy, skill)
    current_enemy.life -= damage

    print(f"You used {action} and dealt {damage} damage!")
    print(f"{current_enemy.name}'s HP: {current_enemy.life}")


def enemy_attack(current_enemy):
    print(f"\n{current_enemy.name}'s turn!")
    damage = max(1, current_enemy.atk - charactersys.Player.defense)
    charactersys.Player.life -= damage
    print(f"{current_enemy.name} attacked and dealt {damage} damage!")
    print(f"Your HP: {charactersys.Player.life}")
    print(f"{current_enemy.name} says: {get_attack_reaction()}")


def attempt_escape(current_enemy):
    """Attempt to escape from combat."""
    if charactersys.Player.agi > current_enemy.agi:
        print("You successfully escaped!")
        return True
    print("You tried to escape but failed, and took a hit!")
    enemy_attack(current_enemy)
    return False


def use_item():
    show_inventory()


def show_ui(current_enemy):
    print("\n=== COMBAT ===")
    print(f"{charactersys.Player.name}: {charactersys.Player.life} HP | "
          f"{current_enemy.name}: {current_enemy.life} HP")

    try:
        action = int(input("1: ATTACK  2: RUN  3: USE ITEM\n> "))
    except ValueError:
        print("Please enter a valid number!")
        return "invalid"

    return action


def combat_loop():
    """Main combat loop."""
    current_enemy = deepcopy(select_random_enemy())

    # Save original type before renaming
    enemy_type = current_enemy.name
    current_enemy.name = get_random_enemy_name()
    current_enemy.life = current_enemy.base_life

    print(f"\nYou encountered {current_enemy.name} the {enemy_type}!")
    print(f"{current_enemy.name} says: {get_enemy_taunt()}")

    escaped = False

    while charactersys.Player.life > 0 and current_enemy.life > 0 and not escaped:
        action = show_ui(current_enemy)

        if action == 1:
            player_attack(current_enemy)
            if current_enemy.life > 0:
                enemy_attack(current_enemy)
        elif action == 2:
            escaped = attempt_escape(current_enemy)
        elif action == 3:
            use_item()
            if current_enemy.life > 0:
                enemy_attack(current_enemy)
        else:
            enemy_attack(current_enemy)

        # Victory / defeat conditions
        if current_enemy.life <= 0:
            print(f"\n{current_enemy.name} says: {get_defeat_phrase()}")
            print(f"You defeated {current_enemy.name}!")
            xp_gain = current_enemy.lvl * 5
            charactersys.Player.xp += xp_gain
            print(f"You gained {xp_gain} XP! Total: {charactersys.Player.xp} XP")

            # Loot system
            looted_items = [item for item in current_enemy.inventory if item in ITEMS]
            for item in looted_items:
                choice = input(f"{current_enemy.name} dropped {ITEMS[item].name}. Pick it up? (y/n): ")
                if choice.lower() == "y":
                    charactersys.Player.inventory.append(item)
                    print(f"{ITEMS[item].name} added to your inventory.")
                    print(f"You have won {current_enemy.gold} coins of gold!")
                    charactersys.Player.gold += current_enemy.gold
                    print(f"You have now {charactersys.Player.gold} coins of gold!")
                else:
                    print(f"You left {ITEMS[item].name} behind.")
            break

        elif charactersys.Player.life <= 0:
            print("\nYou were defeated!")
            break


if __name__ == "__main__":
    pass
