import charactersys

def calculate_xp_to_next_level():
    """Calculates how much XP is needed to reach the next level."""
    xptonextlvl = charactersys.Player.lvl ** 2
    return xptonextlvl

def perform_level_up():
    """Executes the level up: increases level and resets/subtracts XP."""
    charactersys.Player.lvl += 1
    # Opção melhorada: mantém XP excedente
    xptonextlvl = calculate_xp_to_next_level()  # XP needed for the new next level
    excess_xp = charactersys.Player.xp - (charactersys.Player.lvl - 1) ** 2
    charactersys.Player.xp = excess_xp
    print(f"LEVEL UP! YOU ARE NOW LEVEL {charactersys.Player.lvl}!")

def show_xp_progress():
    """Shows current XP progress toward the next level."""
    xptonextlvl = calculate_xp_to_next_level()
    print(f"{charactersys.Player.xp} / {xptonextlvl}.")

def lvlsystem():
    """
    Main leveling system function.
    Checks if the player can level up (possibly multiple times)
    and shows progress when no more level ups are possible.
    """
    leveled_this_call = False
    
    while True:
        xptonextlvl = calculate_xp_to_next_level()
        
        if charactersys.Player.xp >= xptonextlvl:
            perform_level_up()
            leveled_this_call = True
        else:
            show_xp_progress()
            break
    
    # Opcional: retornar se houve level up nesta chamada
    return leveled_this_call