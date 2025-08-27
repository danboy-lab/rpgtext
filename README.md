# RPG Game

A text-based RPG game built in Python with character progression, combat system, and map exploration.

## 🎯 Features

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

### Game Mechanics
- Turn-based combat with attack/defense mechanics
- XP gain from defeating enemies
- Level progression with automatic stat increases
- Random encounter system
- Map exploration with terrain-based encounter rates

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- No external dependencies required

### Installation
1. Clone or download the project
2. Navigate to the project directory

### Running the Game
```bash
python src/main.py
```

## 🎮 How to Play

1. Run `python src/main.py` to start the game
2. Use WASD keys to move around the map
3. Encounter enemies randomly based on your position
4. Choose to attack or flee during combat
5. Gain XP and level up your character
6. Survive as many turns as possible!

## 📁 Project Structure

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
└── README.MD             # This file
```

## 🛠 Development

### Running Tests
```bash
python -m pytest tests/
```

### Adding New Features
- Follow the modular structure
- Add tests for new functionality
- Update documentation accordingly

## 📊 Version History

- v0.1.0: Initial release with core systems integrated
  - Basic combat, leveling, and map navigation
  - Single enemy type (Goblin)
  - Functional game loop

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by classic text-based RPG games
- Built with Python standard library
