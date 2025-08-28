from dataclasses import dataclass
from charactersys import *
@dataclass
class InventoryItem:
    """
    RPG Inventory System
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


# Weapons
Dagger = InventoryItem(
    id="dagger",
    name="Dagger",
    type="Weapon",
    damage=10,
    value=20,
    rarity="Common"
)

AshBlade = InventoryItem(
    id="ash_blade",
    name="Blade of Eternal Ashes",
    type="Weapon",
    damage=25,
    value=120,
    rarity="Epic"
)

MoonBow = InventoryItem(
    id="moon_bow",
    name="Full Moon Bow",
    type="Weapon",
    damage=18,
    value=90,
    rarity="Rare"
)


# Armors
ForgottenGuardianArmor = InventoryItem(
    id="guardian_armor",
    name="Armor of the Forgotten Guardian",
    type="Armor",
    defense=30,
    value=200,
    rarity="Legendary"
)

SilentShadowCloak = InventoryItem(
    id="shadow_cloak",
    name="Silent Shadow Cloak",
    type="Armor",
    defense=10,
    value=150,
    rarity="Rare"
)


# Consumables (must have numeric effects)
RedPotion = InventoryItem(
    id="red_potion",
    name="Crimson Vitality Potion",
    type="Consumable",
    value=30,
    rarity="Common",
    effect_value=50,  # Restores 50 HP
    extra="Restore HP"
)

FuryElixir = InventoryItem(
    id="fury_elixir",
    name="Elixir of Fury",
    type="Consumable",
    value=60,
    rarity="Uncommon",
    effect_value=20,  # +20 Attack for 3 turns
    extra="+Attack"
)


# Accessories
ArcaneEchoAmulet = InventoryItem(
    id="arcane_amulet",
    name="Amulet of Arcane Echo",
    type="Accessory",
    value=250,
    rarity="Epic"
)

FrostSoulRing = InventoryItem(
    id="frost_ring",
    name="Ring of the Frozen Soul",
    type="Accessory",
    damage=5,
    value=180,
    rarity="Rare",
    extra="+40% Ice Resistance, +5 Ice Damage"
)

def add_inventory_item(item):
    Player.inventory = [item]
    print(f"{item[1]} Added")

def remove_inventory_item(item):
    Player.inventory.remove(item)
    
def consume(item):
    if item in Player.inventory and item.type == "Consumable":
        print(f"Consuming {item.name}...")
        # Apply effect based on effect_value; here assuming it restores life points
        Player.life += item.effect_value
        # Remove item from inventory after consumption
        Player.inventory.remove(item)
        print(f"{item.name} consumed. Life increased by {item.effect_value}. Current life: {Player.life}")
    else:
        print("Item cannot be consumed or not in inventory.")

