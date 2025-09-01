<p align="center">
  <h1 align="center"> Text based RPG</h1>
  <p>Built in Python with character progression, turn-based combat, map exploration, NPC interactions, and a menu-driven interface.</p>
  <p>
    <strong>Technologies Used:</strong><br>
    🐍 Python 3.6+ &nbsp;&nbsp;|&nbsp;&nbsp; 📄 JSON &nbsp;&nbsp;|&nbsp;&nbsp; ⚙️ Standard Library
  </p>
</p>


## 🎯 Features

### Core Systems
- **Character System** (`src/charactersys.py`)
  - Character class with comprehensive stats (life, mana, xp, atk, defense, lvl, agi, int, str, dex, luck)
  - Three distinct character classes: Fighter, Mage, and Rogue
  - Leveling system with XP requirements and stat progression
  - Combat mechanics with damage calculation and status effects

- **Menu System** (`src/menu.py`)
  - Beautiful ASCII art main menu with emoji decorations
  - New Game setup with class selection
  - Load Game functionality with save file detection
  - About section with game information and controls
  - GitHub repository integration

- **Enemy System** (`src/enemys.py`)
  - Multiple enemy types: Goblin, Orc, Skeleton, Slime, Bandit, Dark Mage, Ogre, Dragon Whelp
  - Dynamic enemy selection based on player level
  - Enemy phrases and loot drops

- **Combat System** (`src/combat.py`)
  - Turn-based combat with initiative system
  - Skill-based combat with multiple attack options
  - XP gain and loot from defeating enemies
  - Flee mechanics and item usage

- **Map System** (`src/map.py`)
  - Procedurally generated map with varied terrain
  - Player position tracking and movement
  - WASD movement controls with collision detection
  - Visual map display with player marker

- **Skills System** (`src/skillsys.py`)
  - Comprehensive skill database with multiple categories
  - Level-based skill unlocking system
  - Physical and magical skill types

- **Save/Load System** (`src/save_load.py`)
  - JSON-based save file system
  - Complete game state preservation
  - Automatic save file detection

### Game Mechanics
- Turn-based combat with strategic depth
- XP gain and leveling with stat improvements
- Random encounter system based on terrain
- Inventory management system
- Save/load functionality
- Multiple character classes with unique abilities
- Dynamic enemy scaling based on player level

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/danboy-lab/rpgtext.git
cd rpgtext
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Running the Game
```bash
python src/main.py
```

## 🎮 How to Play

### Game Controls
- **W/A/S/D** - Move around the map
- **I** - Open inventory
- **SV** - Save game
- **L** - Load game
- **Q** - Quit game

### Gameplay Flow
1. **Start**: Run `python src/main.py` to launch the game
2. **Menu**: Choose from New Game, Load Game, About, or GitHub
3. **Class Selection**: Pick Fighter, Mage, or Rogue for different playstyles
4. **Exploration**: Use WASD to move around the procedurally generated map
5. **Combat**: Random encounters trigger turn-based battles
6. **Progression**: Defeat enemies to gain XP and level up
7. **Survival**: Try to survive as many turns as possible!

### Character Classes
- **🏆 Fighter**: High strength and defense, balanced combat
- **🔮 Mage**: Powerful magic attacks, high intelligence
- **🗡️ Rogue**: High agility and dexterity, stealth-focused

## 📁 Project Structure

```
rpg-text-adventure/
├── src/                          # Source code directory
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Main entry point & game loop
│   ├── menu.py                  # Menu system & UI
│   ├── charactersys.py          # Character classes & stats
│   ├── combat.py                # Combat mechanics
│   ├── enemys.py                # Enemy definitions
│   ├── map.py                   # Map generation & navigation
│   ├── skillsys.py              # Skills & abilities system
│   ├── save_load.py             # Save/load functionality
│   ├── inventory.py             # Inventory management
│   ├── lvlsys.py                # Leveling system
│   ├── generate_player.py       # Character generation
│   ├── apis.py                  # External API integrations
│   └── showstats.py             # Statistics display
├── data/                        # Game data files
│   ├── skills.json              # Skills database
│   └── enemy_phrases.json       # Enemy dialogue
├── tests/                       # Test suite
│   ├── __init__.py
│   ├── conftest.py              # Test configuration
│   ├── test_charactersys.py     # Character system tests
│   ├── test_combat.py           # Combat system tests
│   ├── test_enemys.py           # Enemy system tests
│   ├── test_save_load.py        # Save/load tests
│   ├── test_lvlsys.py           # Leveling system tests
│   └── test_*.py                # Other test files
├── docs/                        # Documentation
│   ├── ROADMAP.md               # Development roadmap
│   └── TODO.md                  # Task tracking
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── savegame.json                # Auto-generated save file
└── README.md                    # This file
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

We welcome contributions from the community! Whether you're fixing bugs, adding features, improving documentation, or helping with testing, your help is appreciated.

### How to Contribute

0. Planned tasks are listed in `docs/TODO.md`, but don’t hesitate to explore and add your own ideas or improvements!

1. Fork the repository on GitHub:  
   https://github.com/danboy-lab/rpgtext

2. Clone your fork locally:  
```bash
git clone https://github.com/danboy-lab/rpgtext.git
cd rpgtext
```

3. Create a new branch for your feature or bugfix:  
```bash
git checkout -b feature/your-feature-name
# or for bug fixes:
git checkout -b fix/issue-description
```

4. Make your changes and commit them with clear messages.

5. Push your branch to your fork:  
```bash
git push origin feature/your-feature-name
```

6. Open a pull request on the original repository.

### Guidelines

- Follow PEP 8 style guidelines.
- Write clear, concise commit messages.
- Add tests for new features or bug fixes.
- Update documentation as needed.

Thank you for helping improve RPG Text Adventure! 🎮

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by classic text-based RPG games
- Built with Python standard library
