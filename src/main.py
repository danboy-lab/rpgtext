from dataclasses import dataclass
from src.charactersys import Player  # Import the Player instance from charactersys

print(Player)


def lvlsystem():
    xptonextlvl = Player.lvl ** 2
    if Player.xp >= xptonextlvl:
        Player.lvl += 1
        Player.xp = 0
        print(f"Você passou de nivel! agora você é lvl {Player.lvl} parabéns!")
    else:
        print(f"Você tem {Player.xp} de xp! Precisa de {xptonextlvl} para o próximo nível.")
