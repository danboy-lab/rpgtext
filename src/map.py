from showstats import *
from inventory import *
import random

def generate_map(rows=5, cols=5, min_val=0, max_val=5):
    """Gera uma matriz de mapa dinâmica."""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Parâmetros do mapa
ROWS = 10
COLS = 10

# Gerar mapa dinâmico
map_data = generate_map(ROWS, COLS)

# Posição inicial do player aleatória
player_pos = [random.randint(0, ROWS - 1), random.randint(0, COLS - 1)]

def display_map():
    tile_symbols = {
        0: " ",  # empty space
        1: "#",  # wall or tree
        2: "T",  # tree
        3: "~",  # water
        4: ".",  # grass
        5: "^",  # mountain
    }
    print("\n=== RPG MAP ===")
    for r, row in enumerate(map_data):
        for c, tile in enumerate(row):
            if [r, c] == player_pos:
                print("[P]", end=" ")
            else:
                symbol = tile_symbols.get(tile, "?")
                print(f" {symbol} ", end=" ")
        print()

def move():
    """Move o player com base na tecla w/a/s/d"""
    d = input("Move (w/a/s/d, i para inventário, sv para salvar, l para carregar, q para sair, o para abrir status): ").strip().lower()
    if d == 'q':
        return False
    # May return to main menu in a further version
    elif d == 'sv':
        from save_load import save_game
        save_game()
        return True
    elif d == 'l':
        from save_load import load_game
        load_game()
        return True
    elif d == 'i':
        show_inventory()
        return True
    elif d == 'o':
        manage_status()

    r, c = player_pos
    if d == 'w' and r > 0:
        player_pos[0] -= 1
    elif d == 's' and r < len(map_data) - 1:
        player_pos[0] += 1
    elif d == 'a' and c > 0:
        player_pos[1] -= 1
    elif d == 'd' and c < len(map_data[0]) - 1:
        player_pos[1] += 1

    else:
        print("Movimento inválido.")
        return True  # continua o loop mesmo com tecla inválida

    print(f"Moved to {player_pos}")
    return True

# Loop principal
#while True:
#    display_map()
#    if not move():
#        print("Saindo do jogo.")
#        break
