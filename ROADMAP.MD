# RPG Game Roadmap

## 🎯 Project Overview
A text-based RPG game built in Python with character progression, combat system, and map exploration.

## 📋 Current Features (Implemented)

### Core Systems
- **Character System** (`charactersys.py`)
  - Character class with stats (life, mana, xp, atk, DEF, lvl)
  - Leveling system with XP requirements
  - Combat mechanics with damage calculation
  - Player instance with balanced starting stats

- **Enemy System** (`enemys.py`)
  - Goblin enemy with predefined stats
  - Easy to extend with more enemy types

- **Map System** (`map.py`)
  - 5x5 grid map with different terrain values
  - Player position tracking
  - Movement system (WASD controls)
  - Visual map display with player marker

- **Main Game Loop** (`main.py`)
  - Integrated combat encounters
  - Random enemy encounters based on map position
  - Turn-based gameplay
  - Player stat management

### Game Mechanics
- Turn-based combat with attack/defense mechanics
- XP gain from defeating enemies
- Level progression with automatic stat increases
- Random encounter system
- Map exploration with terrain-based encounter rates

## 🚧 Planned Features

### Short Term (Phase 2)
- [ ] Inventory system with items and equipment
- [ ] Multiple enemy types (Orcs, Dragons, etc.)
- [ ] Quest system with objectives
- [ ] Save/Load game functionality
- [ ] Shop system for buying/selling items

### Medium Term (Phase 3)
- [ ] Magic system with spells and mana
- [ ] Boss battles with special mechanics
- [ ] Day/Night cycle affecting gameplay
- [ ] Weather system impacting encounters
- [ ] NPC interactions and dialogue system

### Long Term (Phase 4)
- [ ] Multi-region map system
- [ ] Crafting system
- [ ] Faction reputation system
- [ ] Multiplayer capabilities
- [ ] Graphical interface (PyGame or similar)

## 🛠 Technical Architecture

### File Structure
```
RPG/
├── main.py          # Main game loop and integration
├── charactersys.py  # Character class and combat system
├── enemys.py       # Enemy definitions
├── map.py          # Map navigation system
├── ROADMAP.MD      # This document
└── TODO.md         # Development progress tracking
```

### Dependencies
- Python 3.6+
- Standard library only (no external dependencies)

## 🎮 How to Play
1. Run `python main.py` to start the game
2. Use WASD keys to move around the map
3. Encounter enemies randomly based on your position
4. Choose to attack or flee during combat
5. Gain XP and level up your character
5. Survive as many turns as possible!

## 🔧 Development Notes
- All game data is stored in memory (no persistence yet)
- Easy to extend with new features
- Modular design allows for independent development of systems
- Portuguese language support (easily translatable)

## 📊 Version History
- v0.1.0: Initial release with core systems integrated
  - Basic combat, leveling, and map navigation
  - Single enemy type (Goblin)
  - Functional game loop
