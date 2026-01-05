import charactersys

def check_level_up():
    """
    Checks if the player has enough XP to level up.
    If yes, levels up the player (possibly multiple times) and keeps excess XP.
    Prints progress or level up messages.
    Returns True if at least one level was gained, False otherwise.
    """
    leveled_up = False
    
    while True:
        # XP required to reach the NEXT level (current level squared)
        xp_needed = charactersys.Player.lvl ** 2
        
        if charactersys.Player.xp >= xp_needed:
            # Level up!
            charactersys.Player.xp -= xp_needed
            charactersys.Player.lvl += 1
            leveled_up = True
            print(f"LEVEL UP! YOU ARE NOW LEVEL {charactersys.Player.lvl}!")
        else:
            # Not enough XP yet → show progress
            print(f"{charactersys.Player.xp} / {xp_needed} XP to next level.")
            break
    
    return leveled_up