from charactersys import *
from enemys import Goblin
from skillsys import data

namesskillsdisponiveis = []
escaped = False  # Initialize escaped to False

def getnamesskillsdisponiveis():
    namesskillsdisponiveis.clear()  # Clear the list to avoid duplicates
    for category in data["skills"]:
        for skill in data["skills"][category]:
            if skill["level_required"] <= Player.lvl:
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

def player_attack():
    print("Você tem a iniciativa!")
    getnamesskillsdisponiveis()
    print(f"Habilidades disponíveis: {', '.join(namesskillsdisponiveis)}")
    action = input("Qual ataque deseja usar? ")
    
    skill = find_skill_by_name(action)
    if skill and action.capitalize() in namesskillsdisponiveis:
        if Player.mana >= skill["mana_cost"]:
            Player.mana -= skill["mana_cost"]
            damage = calculate_damage(Player, Goblin, skill)
            Goblin.life -= damage
            print(f"Você usou {action} e causou {damage} de dano!")
            print(f"Vida do Goblin: {Goblin.life}")
        else:
            print("Mana insuficiente!")
    else:
        print("Você não tem esse ataque!")

def enemy_attack():
    print(f"\nTurno do {Goblin.name}!")
    # Simple enemy attack - just a basic attack
    damage = max(1, Goblin.atk - Player.defense)
    Player.life -= damage
    print(f"{Goblin.name} atacou e causou {damage} de dano!")
    print(f"Sua vida: {Player.life}")

def run():
    if Player.agi > Goblin.agi:
        print("Você conseguiu fugir!")
    elif Player.agi < Goblin.agi:
        print("Você tentou fugir mas não conseguiu, então tomou um ataque!")
        enemy_attack()

def use_item():
    print("Sistema de itens ainda não implementado")

def ui():
    print(f"\n=== COMBATE ===")
    print(f"{Player.name}: {Player.life} HP | {Goblin.name}: {Goblin.life} HP")
    print(f"O que você deseja fazer?: ")
    
    try:
        action = int(input("1: ATACAR 2: FUGIR 3: USAR ITEM: "))
        if action == 1:
            player_attack()
            if Goblin.life > 0:
                enemy_attack()
        elif action == 2:
            run()
        elif action == 3:
            use_item()
            enemy_attack()
        else:
            print("Opção inválida!")
            enemy_attack()
    except ValueError:
        print("Por favor, digite um número válido!")
        enemy_attack()

def combat_loop():
    print("Você entrou em combate com um Goblin!")
    
    while Player.life > 0 and Goblin.life > 0 and not escaped:
        ui()
        
        if Goblin.life <= 0:
            print(f"\nVocê derrotou o {Goblin.name}!")
            Player.xp += 5  # Give XP for defeating enemy
            print(f"Ganhou 5 XP! Total: {Player.xp} XP")
            break
        elif Player.life <= 0:
            print("\nVocê foi derrotado!")
            break

# Start combat only when run directly
if __name__ == "__main__":
    #combat_loop()
