from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.widgets import Header, Footer, Static, Button, Log
from textual.containers import Container
from textual import on
from copy import deepcopy

# Imports do seu código original
import charactersys
from charactersys import Player  # Player global
from enemys import ENEMIES  # Lista de inimigos
from combat import (
    select_random_enemy,
    get_available_skill_names,
    find_skill_by_name,
    calculate_damage,
    get_random_enemy_name,
)

class MainMenuScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("🗡️ RPG Text Based - Textual Edition 🗡️", id="title"),
            Button("New Game", id="new_game", variant="primary"),
            Button("Load Game", id="load_game", variant="warning"),  # Ainda não implementado
            Button("Exit", id="exit", variant="error"),
            id="menu"
        )
        yield Footer()

    @on(Button.Pressed)
    def on_button_pressed(self, event):
        if event.button.id == "new_game":
            self.app.push_screen(CharacterCreationScreen())
        elif event.button.id == "exit":
            self.app.quit()

class CharacterCreationScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Escolha sua classe:")
        yield Button("Fighter (alto ataque/defesa)", id="fighter")
        yield Button("Mage (magias fortes)", id="mage")
        yield Button("Rogue (ágil, crítico)", id="rogue")
        yield Footer()

    @on(Button.Pressed)
    def on_button_pressed(self, event):
        # Reseta player
        Player.name = "Hero"
        Player.lvl = 1
        Player.xp = 0
        Player.gold = 10
        Player.inventory = []

        if event.button.id == "fighter":
            Player.life = Player.base_life = 50
            Player.mana = Player.base_mana = 20
            Player.atk = 10
            Player.defense = 8
            Player.agi = 5
            Player.int_ = 3
        elif event.button.id == "mage":
            Player.life = Player.base_life = 30
            Player.mana = Player.base_mana = 50
            Player.atk = 4
            Player.defense = 3
            Player.agi = 4
            Player.int_ = 12
        elif event.button.id == "rogue":
            Player.life = Player.base_life = 40
            Player.mana = Player.base_mana = 30
            Player.atk = 8
            Player.defense = 5
            Player.agi = 10
            Player.int_ = 6

        # Vai direto pro combate pra testar
        self.app.push_screen(CombatScreen())

class SkillsModal(ModalScreen):
    def __init__(self, combat_screen):
        super().__init__()
        self.combat_screen = combat_screen

    def compose(self) -> ComposeResult:
        yield Static("Escolha uma skill:")
        available = get_available_skill_names()
        for name in available:
            yield Button(name, id=name)
        yield Button("Cancelar", id="cancel", variant="error")

    @on(Button.Pressed)
    def on_button_pressed(self, event):
        if event.button.id == "cancel":
            self.dismiss()
        else:
            skill = find_skill_by_name(event.button.id)
            if skill:
                self.dismiss(skill)

class CombatScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static(id="player_stats"),
            Static(id="enemy_stats"),
            Log(id="combat_log"),
            Container(
                Button("Attack", id="attack", variant="success"),
                Button("Skills", id="skills"),
                Button("Item", id="item"),
                Button("Run", id="run", variant="warning"),
                id="actions"
            ),
            id="combat_area"
        )
        yield Footer()

    def on_mount(self):
        self.player = Player
        self.enemy = deepcopy(select_random_enemy())
        self.enemy.name = get_random_enemy_name()
        if hasattr(self.enemy, "base_life"):
            self.enemy.life = self.enemy.base_life
        self.update_stats()
        self.log = self.query_one(Log)
        self.log.write(f"Você encontrou {self.enemy.name} the {self.enemy.__class__.__name__}!")

    def update_stats(self):
        self.query_one("#player_stats").update(
            f"Você: LV {self.player.lvl} | HP {self.player.life}/{self.player.base_life} | Mana {self.player.mana}/{self.player.base_mana}"
        )
        self.query_one("#enemy_stats").update(
            f"Inimigo: {self.enemy.name} | HP {self.enemy.life}"
        )

    @on(Button.Pressed, "#attack")
    def basic_attack(self):
        skill = {"name": "Basic Attack", "damage": 0, "mana_cost": 0, "type": "physical"}
        self.execute_player_action(skill)

    @on(Button.Pressed, "#skills")
    def choose_skill(self):
        self.app.push_screen(SkillsModal(self))

    def on_skills_modal_dismissed(self, message):
        if message:
            self.execute_player_action(message)

    def execute_player_action(self, skill):
        if self.player.mana < skill["mana_cost"]:
            self.log.write("Mana insuficiente!")
            return
        self.player.mana -= skill["mana_cost"]
        damage = calculate_damage(self.player, self.enemy, skill)
        self.enemy.life -= damage
        self.log.write(f"Você usou {skill['name']} e causou {damage} de dano!")
        self.update_stats()
        self.check_victory()
        if self.enemy.life > 0:
            self.enemy_turn()

    def enemy_turn(self):
        damage = max(1, self.enemy.atk - self.player.defense)
        self.player.life -= damage
        self.log.write(f"{self.enemy.name} atacou e causou {damage} de dano!")
        self.update_stats()
        self.check_defeat()

    @on(Button.Pressed, "#run")
    def try_run(self):
        if self.player.agi > self.enemy.agi:
            self.log.write("Você fugiu com sucesso!")
            self.app.pop_screen()
        else:
            self.log.write("Fuga falhou!")
            self.enemy_turn()

    @on(Button.Pressed, "#item")
    def use_item(self):
        self.log.write("Inventário ainda não implementado no combate Textual (em breve!)")

    def check_victory(self):
        if self.enemy.life <= 0:
            xp_gain = self.enemy.lvl * 5
            self.player.xp += xp_gain
            self.player.gold += self.enemy.gold
            self.log.write(f"Vitória! +{xp_gain} XP e +{self.enemy.gold} ouro")
            # Aqui você pode chamar level up se quiser
            self.notify("Vitória! Pressione ESC para continuar", severity="information")

    def check_defeat(self):
        if self.player.life <= 0:
            self.log.write("Você foi derrotado...")
            self.notify("Game Over", severity="error")

class RPGApp(App):
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        yield MainMenuScreen()

if __name__ == "__main__":
    RPGApp().run()