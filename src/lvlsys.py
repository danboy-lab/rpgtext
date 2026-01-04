import charactersys

def lvlsystem():
    xptonextlvl = charactersys.Player.lvl ** 2
    if charactersys.Player.xp >= xptonextlvl:
        charactersys.Player.lvl += 1
        charactersys.Player.xp = 0
        print(f"LEVEL UP! YOU ARE NOW  LEVEL {charactersys.Player.lvl}!")
    else:
        print(f"{charactersys.Player.xp} / {xptonextlvl}.")
