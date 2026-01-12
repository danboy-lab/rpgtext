<h1 align="center">Text-based RPG</h1>

<p align="center">
  Built in Python with character progression, turn-based combat, map exploration,
  NPC interactions, and a menu-driven interface.
</p>

<p align="center">
  <strong>Technologies Used:</strong><br>
  🐍 Python 3.6+ &nbsp;&nbsp;|&nbsp;&nbsp;
  🖥️ Textual 7.0.0 &nbsp;&nbsp;|&nbsp;&nbsp;
  🌐 requests 2.32.5 &nbsp;&nbsp;|&nbsp;&nbsp;
  📄 JSON &nbsp;&nbsp;|&nbsp;&nbsp;
  ⚙️ Python Standard Library
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
3. Installing the requirements

```bash
pip -r requirements.txt

``` 

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
rpgtext/
├── README.md
├── data
│   ├── enemy_phrases.json
│   ├── enemy_skills.json
│   ├── locations.json
│   ├── maps.json
│   └── skills.json
├── docs
│   ├── ROADMAP.MD
│   └── TODO.md
├── features
│   └── atribute_tree.py
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── src
    ├── __init__.py
    ├── __pycache__
    │   ├── apis.cpython-314.pyc
    │   ├── charactersys.cpython-314.pyc
    │   ├── combat.cpython-314.pyc
    │   ├── enemys.cpython-314.pyc
    │   ├── generate_player.cpython-314.pyc
    │   ├── inventory.cpython-314.pyc
    │   ├── lvlsys.cpython-314.pyc
    │   ├── map.cpython-314.pyc
    │   ├── menu.cpython-314.pyc
    │   ├── save_load.cpython-314.pyc
    │   ├── showstats.cpython-314.pyc
    │   └── skillsys.cpython-314.pyc
    ├── apis.py
    ├── app.py
    ├── charactersys.py
    ├── combat.py
    ├── enemys.py
    ├── generate_items.py
    ├── generate_maps.py
    ├── generate_player.py
    ├── inventory.py
    ├── lvlsys.py
    ├── main.py
    ├── map.py
    ├── menu.py
    ├── npcs.py
    ├── save_load.py
    ├── showstats.py
    ├── skillsys.py
    └── styles.tcss
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

# Credits

https://github.com/Textualize/textual

## 🙏 Acknowledgments
- Wish to make a cool isekai vibe in the future ;D
- Inspired by classic text-based RPG games
