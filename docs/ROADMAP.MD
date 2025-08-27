# RPG Game Roadmap

## 🎯 Project Overview
A text-based RPG game built in Python with character progression, combat system, and map exploration.

## 📋 Current Features (Implemented)

### Core Systems
- **Character System** (`src/charactersys.py`)
  - Character class with stats (life, mana, xp, atk, DEF, lvl)
  - Leveling system with XP requirements
  - Combat mechanics with damage calculation
  - Player instance with balanced starting stats

- **Enemy System** (`src/enemys.py`)
  - Goblin enemy with predefined stats
  - Easy to extend with more enemy types

- **Combat System** (`src/combat.py`)
  - Turn-based combat with attack/defense mechanics
  - Skill-based combat system
  - XP gain from defeating enemies

- **Map System** (`src/map.py`)
  - 5x5 grid map with different terrain values
  - Player position tracking
  - Movement system (WASD controls)
  - Visual map display with player marker

- **Skills System** (`src/skillsys.py`)
  - Skill database with different categories
  - Level-based skill unlocking
  - Skill types (physical, magical)

- **Main Game Loop** (`src/main.py`)
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
├── src/                    # Source code directory
│   ├── __init__.py        # Make src a package
│   ├── charactersys.py    # Character system
│   ├── combat.py          # Combat system
│   ├── enemys.py          # Enemy definitions
│   ├── map.py             # Map navigation
│   ├── showstats.py       # Stats display
│   ├── skillsys.py        # Skills system
│   └── main.py            # Main game loop
├── data/                  # Data files directory
│   └── skills.json        # Skills data
├── docs/                  # Documentation directory
│   ├── ROADMAP.MD         # Project roadmap
│   └── TODO.MD            # Development tasks
├── tests/                 # Test directory
│   ├── conftest.py
│   ├── test_charactersys.py
│   ├── test_combat.py
│   ├── test_enemys.py
│   └── test_skillsys.py
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
└── README.MD             # Main project documentation
```

### Dependencies
- Python 3.6+
- Standard library only (no external dependencies)

## 🎮 How to Play
1. Run `python src/main.py` to start the game
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
