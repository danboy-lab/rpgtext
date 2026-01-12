from rich import print
from rich.panel import Panel
from rich.table import Table

import charactersys
from enemys import *


def manage_status():
    def show_status(subject):
        table = Table.grid(padding=(0, 2))
        table.add_column(justify="left")
        table.add_column(justify="right")

        # BASIC INFO
        table.add_row("[bold]Name[/bold]", subject.name)
        table.add_row("Level", str(subject.lvl))
        table.add_row("XP", str(subject.xp))
        table.add_row("Gold", str(subject.gold))

        table.add_row("", "")
        table.add_row("[bold cyan]ATTRIBUTES[/bold cyan]", "")
        table.add_row("Agility", str(subject.agi))
        table.add_row("Attack", str(subject.atk))
        table.add_row("Defense", str(subject.defense))
        table.add_row("Dexterity", str(subject.dex))
        table.add_row("Intelligence", str(subject.int_))
        table.add_row("Luck", str(subject.luck))

        table.add_row("", "")
        table.add_row("[bold green]RESOURCES[/bold green]", "")
        table.add_row("Life Points", str(subject.life))
        table.add_row("Mana", str(subject.mana))

        table.add_row("", "")
        table.add_row("[bold yellow]EQUIPMENT[/bold yellow]", "")
        table.add_row("Inventory", str(subject.inventory))

        table.add_row("", "")
        table.add_row("[bold magenta]SKILLS[/bold magenta]", "")
        table.add_row("Skills", str(subject.skills))

        table.add_row("", "")
        table.add_row("[bold red]STATUS EFFECTS[/bold red]", "")
        table.add_row("Effects", str(subject.status_effects))

        print(
            Panel(
                table,
                title=f"[bold]{subject.__class__.__name__.upper()} STATUS[/bold]",
                border_style="blue"
            )
        )

    while True:
        try:
            which = int(input("You want see: My Status [1] Enemy Status [2] Back [3] "))
        except ValueError:
            print("[red]Please, enter a valid number (1, 2 or 3).[/red]")
            continue

        if which == 1:
            show_status(charactersys.Player)

        elif which == 2:
            enemies = [Goblin, Orc]
            for enemy in enemies:
                show_status(enemy)

        elif which == 3:
            print("[green]Ok, going back...[/green]")
            break

        else:
            print("[red]Invalid option. Try again.[/red]")
