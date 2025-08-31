import charactersys

def lvlsystem():
    xptonextlvl = charactersys.Player.lvl ** 2
    if charactersys.Player.xp >= xptonextlvl:
        charactersys.Player.lvl += 1
        charactersys.Player.xp = 0
        print(f"Você passou de nivel! agora você é lvl {charactersys.Player.lvl} parabéns!")
    else:
        print(f"Você tem {charactersys.Player.xp} de xp! Precisa de {xptonextlvl} para o próximo nível.")
