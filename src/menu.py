"""
Menu system for RPG Text Adventure
Handles main menu, game setup, and user interface
"""
import charactersys
from generate_player import generate_player
from skillsys import data
from save_load import save_game, load_game, has_save_file
import webbrowser
import sys

def display_main_menu():
    """Display the main menu and handle user choices"""
    while True:
        print("\n" + "="*50)
        print("           🌟 RPG TEXT ADVENTURE 🌟")
        print("="*50)
        print("1. 🎮 New Game")
        print("2. 📁 Load Game")
        print("3. ℹ️  About")
        print("4. 🔗 GitHub Repository")
        print("5. ❌ Exit")
        print("="*50)

        try:
            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                return start_new_game()
            elif choice == "2":
                return load_existing_game()
            elif choice == "3":
                show_about()
            elif choice == "4":
                open_github()
            elif choice == "5":
                print("Thanks for playing! Goodbye! 👋")
                sys.exit(0)
            else:
                print("❌ Invalid choice. Please select 1-5.")
        except KeyboardInterrupt:
            print("\n\nThanks for playing! Goodbye! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"❌ An error occurred: {e}")

def start_new_game():
    """Start a new game with class selection"""
    print("\n" + "="*40)
    print("        🎯 NEW GAME")
    print("="*40)
    print("Choose your class:")
    print("1. ⚔️  Fighter - High strength and defense")
    print("2. 🧙 Mage - Powerful magic and intelligence")
    print("3. 🗡️  Rogue - High agility and dexterity")
    print("="*40)

    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            charactersys.Player = generate_player("fighter")
            name = input("Enter your character's name: ").strip()
            if name:
                charactersys.Player.name = name
            print(f"🏆 You are {charactersys.Player.name} the Fighter!")
            break
        elif choice == "2":
            charactersys.Player = generate_player("mage")
            name = input("Enter your character's name: ").strip()
            if name:
                charactersys.Player.name = name
            print(f"🔮 You are {charactersys.Player.name} the Mage!")
            break
        elif choice == "3":
            charactersys.Player = generate_player("rogue")
            name = input("Enter your character's name: ").strip()
            if name:
                charactersys.Player.name = name
            print(f"🗡️  You are {charactersys.Player.name} the Rogue!")
            break
        else:
            print("❌ Invalid choice. Please select 1-3.")

    return True

def load_existing_game():
    """Load an existing game"""
    print("\n" + "="*40)
    print("        📁 LOAD GAME")
    print("="*40)

    if has_save_file():
        print("Save file found!")
        choice = input("Load saved game? (y/n): ").strip().lower()
        if choice == 'y':
            # Initialize Player before loading
            charactersys.Player = generate_player("fighter")  # temporary, will be overwritten by load
            if load_game():
                print("✅ Game loaded successfully!")
                # Update skills_disponiveis based on loaded player level
                for category in data["skills"]:
                    for skill in data["skills"][category]:
                        if skill["level_required"] <= charactersys.Player.lvl:
                            charactersys.skills_disponiveis.append(skill)
                return True
            else:
                print("❌ Failed to load save file.")
                return start_new_game()
        else:
            print("Starting new game instead...")
            return start_new_game()
    else:
        print("❌ No save file found.")
        choice = input("Start a new game instead? (y/n): ").strip().lower()
        if choice == 'y':
            return start_new_game()
        else:
            return False

def show_about():
    """Show information about the game"""
    print("\n" + "="*50)
    print("              📖 ABOUT THE GAME")
    print("="*50)
    print("🌟 RPG Text Adventure 🌟")
    print("")
    print("A classic text-based RPG adventure where you:")
    print("• 🗺️  Explore a randomly generated world")
    print("• ⚔️  Battle various enemies")
    print("• 📈 Level up and learn new skills")
    print("• 🎒 Manage your inventory")
    print("• 💾 Save and load your progress")
    print("")
    print("🎮 Controls:")
    print("• W/A/S/D - Move around the map")
    print("• I - Open inventory")
    print("• SV - Save game")
    print("• L - Load game")
    print("• Q - Quit game")
    print("")
    print("🎯 Objective:")
    print("Explore the world, defeat enemies, and become stronger!")
    print("="*50)
    input("Press Enter to return to main menu...")

def open_github():
    """Open the GitHub repository in the default browser"""
    github_url = "https://github.com/danboy-lab/rpgtext"
    print(f"\n🔗 Opening GitHub repository: {github_url}")
    try:
        webbrowser.open(github_url)
        print("✅ GitHub page opened in your default browser!")
    except Exception as e:
        print(f"❌ Could not open browser: {e}")
        print(f"Please visit: {github_url}")

    input("Press Enter to return to main menu...")

def help():
    print("W/A/S/D - Move around the map")
    print("SV  - Save game")
    print("I - Open inventory")
    print("L - Load game")
    print("Q - Quit game")
    print("O - Open status")