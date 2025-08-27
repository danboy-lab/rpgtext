map_data = [
    [0, 1, 2, 3, 5],
    [1, 2, 3, 4, 5],
    [2, 3, 1, 4, 5],
    [0, 0, 0, 0, 0],
    [5, 4, 3, 2, 1]
]
player_pos = [0,1]

def display_map():
    print("\n=== RPG MAP ===")
    for r, row in enumerate(map_data):
        for c, tile in enumerate(row):
            print(f"[P]" if [r, c] == player_pos else f" {tile} ", end=" ")
        print()
def move():
    d = input("Move (w/a/s/d): ").strip().lower()
    r, c = player_pos
    if d == 'w' and r > 0: player_pos[0] -= 1
    elif d == 's' and r < 4: player_pos[0] += 1
    elif d == 'a' and c > 0: player_pos[1] -= 1
    elif d == 'd' and c < 4: player_pos[1] += 1
    else: return False
    print(f"Moved to {player_pos}")
    display_map()
    return True
while True:
    display_map()
    move()
    
