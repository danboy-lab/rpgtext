from dataclasses import dataclass
from charactersys import Player

@dataclass
class InventoryItem:
    """
    RPG Inventory System Item
    """
    id: str
    name: str
    type: str   # Weapon, Armor, Consumable, Accessory
    damage: int = 0
    defense: int = 0
    value: int = 0
    rarity: str = "Common"
    effect_value: int = 0   # only used for Consumables
    extra: str = ""

# Define all items in a dictionary for easy lookup by id
ITEMS = {
    "dagger": InventoryItem(
        id="dagger",
        name="Dagger",
        type="Weapon",
        damage=10,
        value=20,
        rarity="Common"
    ),
    "ash_blade": InventoryItem(
        id="ash_blade",
        name="Blade of Eternal Ashes",
        type="Weapon",
        damage=25,
        value=120,
        rarity="Epic"
    ),
    "moon_bow": InventoryItem(
        id="moon_bow",
        name="Full Moon Bow",
        type="Weapon",
        damage=18,
        value=90,
        rarity="Rare"
    ),
    "guardian_armor": InventoryItem(
        id="guardian_armor",
        name="Armor of the Forgotten Guardian",
        type="Armor",
        defense=30,
        value=200,
        rarity="Legendary"
    ),
    "shadow_cloak": InventoryItem(
        id="shadow_cloak",
        name="Silent Shadow Cloak",
        type="Armor",
        defense=10,
        value=150,
        rarity="Rare"
    ),
    "red_potion": InventoryItem(
        id="red_potion",
        name="Crimson Vitality Potion",
        type="Consumable",
        value=30,
        rarity="Common",
        effect_value=50,
        extra="Restore HP"
    ),
    "fury_elixir": InventoryItem(
        id="fury_elixir",
        name="Elixir of Fury",
        type="Consumable",
        value=60,
        rarity="Uncommon",
        effect_value=20,
        extra="+Attack"
    ),
    "arcane_amulet": InventoryItem(
        id="arcane_amulet",
        name="Amulet of Arcane Echo",
        type="Accessory",
        value=250,
        rarity="Epic"
    ),
    "frost_ring": InventoryItem(
        id="frost_ring",
        name="Ring of the Frozen Soul",
        type="Accessory",
        damage=5,
        value=180,
        rarity="Rare",
        extra="+40% Ice Resistance, +5 Ice Damage"
    ),
}

def add_inventory_item(item_id: str):
    """
    Add an item to the Player's inventory by item id.
    """
    if item_id in ITEMS:
        Player.inventory.append(item_id)
        print(f"{ITEMS[item_id].name} Added")
    else:
        print("This item does not exist")

def remove_inventory_item(item_id: str):
    """
    Remove an item from the Player's inventory by item id.
    """
    if item_id in Player.inventory:
        Player.inventory.remove(item_id)
        print(f"{ITEMS[item_id].name} removed from inventory.")
    else:
        print("Item not found in inventory")

def consume(item_id: str):
    """
    Consume a consumable item from the Player's inventory by item id.
    Applies the effect and removes the item.
    """
    if item_id in Player.inventory:
        item = ITEMS.get(item_id)
        if item and item.type == "Consumable":
            print(f"Consuming {item.name}...")
            Player.life += item.effect_value
            Player.inventory.remove(item_id)
            print(f"{item.name} consumed. Life increased by {item.effect_value}. Current life: {Player.life}")
        else:
            print("Item cannot be consumed.")
    else:
        print("Item not in inventory.")

def show_inventory():
    """
    Show the Player's inventory and allow actions (consume/remove).
    """
    if not Player.inventory:
        print("Inventory is empty.")
        return
    
    print("\n========== INVENTORY ==========")
    for i, item_id in enumerate(Player.inventory, 1):
        item = ITEMS.get(item_id)
        if item:
            stats = []
            if item.damage > 0:
                stats.append(f"DMG: {item.damage}")
            if item.defense > 0:
                stats.append(f"DEF: {item.defense}")
            if item.effect_value > 0:
                stats.append(f"Effect: {item.extra} ({item.effect_value})")
            
            stats_str = " | ".join(stats) if stats else "No extra stats"
            print(f"{i}. {item.name} [{item.type}, {item.rarity}] - {stats_str}")
    print("================================")
    
    # Escolher item
    choice = input("Select an item by number (or press Enter to exit): ")
    if not choice.strip():
        return
    
    try:
        choice = int(choice) - 1
        if choice < 0 or choice >= len(Player.inventory):
            print("Invalid choice.")
            return
    except ValueError:
        print("Invalid input.")
        return
    
    item_id = Player.inventory[choice]
    item = ITEMS.get(item_id)
    
    # Perguntar ação
    if item.type == "Consumable":
        action = input(f"Do you want to consume {item.name}? (y/n): ")
        if action.lower() == "y":
            consume(item_id)
    else:
        action = input(f"Do you want to remove {item.name}? (y/n): ")
        if action.lower() == "y":
            remove_inventory_item(item_id)
