from inventory import ITEMS

# Define base stats for classes
CLASS_STATS = {
    "fighter": {
        "life": 30,
        "mana": 5,
        "atk": 8,
        "defense": 5,
        "agi": 4,
        "int_": 2,
        "str_": 7,
        "dex": 4,
        "luck": 3,
        "skills": ["Slash"],
        "inventory": ["dagger"],
        "gold": 10,
    },
    "mage": {
        "life": 20,
        "mana": 30,
        "atk": 3,
        "defense": 2,
        "agi": 5,
        "int_": 9,
        "str_": 2,
        "dex": 4,
        "luck": 4,
        "skills": ["Fireball"],
        "inventory": ["red_potion"],
        "gold": 15,
    },
    "rogue": {
        "life": 25,
        "mana": 10,
        "atk": 6,
        "defense": 3,
        "agi": 8,
        "int_": 4,
        "str_": 5,
        "dex": 7,
        "luck": 6,
        "skills": ["Backstab"],
        "inventory": ["dagger"],
        "gold": 12,
    }
}

def generate_player(class_name: str):
    from charactersys import Character  # Import here to avoid circular import
    class_name = class_name.lower()
    if class_name not in CLASS_STATS:
        raise ValueError(f"Unknown class: {class_name}")

    stats = CLASS_STATS[class_name]
    player = Character(
        name=class_name.capitalize(),
        class_=class_name,
        life=stats["life"],
        mana=stats["mana"],
        xp=0,
        lvl=1,
        atk=stats["atk"],
        defense=stats["defense"],
        agi=stats["agi"],
        int_=stats["int_"],
        str_=stats["str_"],
        dex=stats["dex"],
        luck=stats["luck"],
        skills=stats["skills"],
        inventory=stats["inventory"],
        gold=stats["gold"],
        status_effects=[],
        equipment={}
    )
    return player

# Example usage:
# player = generate_player("fighter")
# print(player)
