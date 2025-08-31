import charactersys
from enemys import Goblin, Orc
import random
from skillsys import data
from apis import get_random_enemy_name, get_enemy_taunt, get_attack_reaction, get_defeat_phrase
from inventory import ITEMS, show_inventory

namesskillsdisponiveis = []
escaped = False  # Initialize escaped to False

# List of available enemies
enemies = [Goblin, Orc]

def select_random_enemy():
    """Select a random enemy based on player level"""
    player_lvl = charactersys.Player.lvl

    # Calculate weights based on level difference
    weights = []
    for enemy in enemies:
        level_diff = abs(player_lvl - enemy.lvl)
        # Higher weight for enemies closer to player level
        # Weight decreases significantly as level difference increases
        if level_diff == 0:
            weight = 80  # Same level: very high chance
        elif level_diff == 1:
            weight = 15  # One level difference: low chance
        else:
            weight = 5   # Large difference: very low chance
        weights.append(weight)

    # Select enemy based on weights
    total_weight = sum(weights)
    rand = random.uniform(0, total_weight)
    cumulative = 0
    for i, weight in enumerate(weights):
        cumulative += weight
        if rand <= cumulative:
            return enemies[i]

    # Fallback
    return enemies[0]

def getnamesskillsdisponiveis():
    namesskillsdisponiveis.clear()  # Clear the list to avoid duplicates
    for category in data["skills"]:
        for skill in data["skills"][category]:
            if skill["level_required"] <= charactersys.Player.lvl:
                namesskillsdisponiveis.append(skill["name"])

def find_skill_by_name(skill_name):
    for category in data["skills"]:
        for skill in data["skills"][category]:
            if skill["name"] == skill_name:
                return skill
    return None

def calculate_damage(attacker, defender, skill):
    base_damage = skill.get("damage", 0)
    if skill["type"] == "physical":
        damage = base_damage + attacker.atk - defender.defense
    elif skill["type"] == "magical":
        damage = base_damage + attacker.int_ - defender.defense
    else:
        damage = base_damage
    
    # Ensure minimum damage of 1
    return max(1, damage)

def player_attack(current_enemy):
    print("Você tem a iniciativa!")
    getnamesskillsdisponiveis()
    print(f"Habilidades disponíveis: {', '.join(namesskillsdisponiveis)}")
    action = input("Qual ataque deseja usar? ").strip().lower()
    
    skill = find_skill_by_name(action.capitalize())
    if skill and action.capitalize() in namesskillsdisponiveis:
        if charactersys.Player.mana >= skill["mana_cost"]:
            charactersys.Player.mana -= skill["mana_cost"]
            damage = calculate_damage(charactersys.Player, current_enemy, skill)
            current_enemy.life -= damage
            print(f"Você usou {action.capitalize()} e causou {damage} de dano!")
            print(f"Vida do {current_enemy.name}: {current_enemy.life}")
        else:
            print("Mana insuficiente!")
    else:
        print("Você não tem esse ataque!")

def enemy_attack(current_enemy):
    print(f"\nTurno do {current_enemy.name}!")
    # Simple enemy attack - just a basic attack
    damage = max(1, current_enemy.atk - charactersys.Player.defense)
    charactersys.Player.life -= damage
    print(f"{current_enemy.name} atacou e causou {damage} de dano!")
    print(f"Sua vida: {charactersys.Player.life}")
    print(f"{current_enemy.name} diz: {get_attack_reaction()}")

def run(current_enemy):
    if charactersys.Player.agi > current_enemy.agi:
        print("Você conseguiu fugir!")
    elif charactersys.Player.agi < current_enemy.agi:
        print("Você tentou fugir mas não conseguiu, então tomou um ataque!")
        enemy_attack(current_enemy)

def use_item():
    show_inventory()

def ui(current_enemy):
    print(f"\n=== COMBATE ===")
    print(f"{charactersys.Player.name}: {charactersys.Player.life} HP | {current_enemy.name}: {current_enemy.life} HP")
    print(f"O que você deseja fazer?: ")
    
    try:
        action = int(input("1: ATACAR 2: FUGIR 3: USAR ITEM: "))
        if action == 1:
            player_attack(current_enemy)
            if current_enemy.life > 0:
                enemy_attack(current_enemy)
        elif action == 2:
            run(current_enemy)
        elif action == 3:
            use_item()
            enemy_attack(current_enemy)
        else:
            print("Opção inválida!")
            enemy_attack(current_enemy)
    except ValueError:
        print("Por favor, digite um número válido!")
        enemy_attack(current_enemy)

def combat_loop():
    # Select random enemy based on player level
    current_enemy = select_random_enemy()
    
    # Create a copy of the enemy to avoid modifying the original
    from copy import deepcopy
    current_enemy = deepcopy(current_enemy)
    
    # Salvar o tipo original antes de renomear
    enemy_type = current_enemy.name  
    
    # Gerar nome aleatório (ex: "Gruk", "Thorn", etc.)
    current_enemy.name = get_random_enemy_name()
    print(f"Você entrou em combate com {current_enemy.name} the {enemy_type}!")
    print(f"{current_enemy.name} diz: {get_enemy_taunt()}")
    
    # Reset enemy life to base value
    current_enemy.life = current_enemy.base_life
    
    while charactersys.Player.life > 0 and current_enemy.life > 0 and not escaped:
        ui(current_enemy)

        if current_enemy.life <= 0:
            print(f"\n{current_enemy.name} diz: {get_defeat_phrase()}")
            print(f"Você derrotou o {current_enemy.name}!")
            charactersys.Player.xp += current_enemy.lvl * 5  # Give XP based on enemy level
            print(f"Ganhou {current_enemy.lvl * 5} XP! Total: {charactersys.Player.xp} XP")

            # Loot items
            looted_items = [item for item in current_enemy.inventory if item in ITEMS]
            if looted_items:
                print(f"{current_enemy.name} dropped: {', '.join(ITEMS[item].name for item in looted_items)}")
                for item in looted_items:
                    choice = input(f"Do you want to pick up {ITEMS[item].name}? (y/n): ")
                    if choice.lower() == 'y':
                        charactersys.Player.inventory.append(item)
                        print(f"{ITEMS[item].name} added to inventory.")
                    else:
                        print(f"You left {ITEMS[item].name} behind.")
            break
        elif charactersys.Player.life <= 0:
            print("\nVocê foi derrotado!")
            break
        
# Start combat only when run directly
if __name__ == "__main__":
    pass
