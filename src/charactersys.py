from dataclasses import dataclass, field
from typing import List, Dict
from skillsys import data

skills_disponiveis = []

@dataclass
class Character:
    """
    Representa um personagem de RPG com atributos comuns.

    Atributos:
        name (str): Nome do personagem.
        class_ (str): Classe do personagem.
        life (int): Pontos de vida.
        mana (int): Pontos de magia.
        xp (int): Pontos de experiência.
        lvl (int): Nível do personagem.
        atk (int): Ataque.
        defense (int): Defesa.
        agi (int): Agilidade.
        int_ (int): Inteligência.
        str_ (int): Força.
        dex (int): Destreza.
        luck (int): Sorte.
        skills (List[str]): Lista de habilidades.
        inventory (List[str]): Inventário de itens.
        gold (int): Quantidade de ouro.
        status_effects (List[str]): Efeitos de status ativos.
    """
    name: str
    class_: str
    life: int
    mana: int
    xp: int
    lvl: int
    atk: int
    defense: int
    agi: int
    int_: int
    str_: int
    dex: int
    luck: int
    base_atk: int = field(init=False)
    base_defense: int = field(init=False)
    base_agi: int = field(init=False)
    base_int_: int = field(init=False)
    base_str_: int = field(init=False)
    base_dex: int = field(init=False)
    base_luck: int = field(init=False)
    skills: List[str] = field(default_factory=list)
    inventory: List[str] = field(default_factory=list)
    gold: int = 0
    status_effects: List[str] = field(default_factory=list)
    equipment: Dict[str, str] = field(default_factory=dict)  # slot: item_id

    def __post_init__(self):
        self.base_atk = self.atk
        self.base_defense = self.defense
        self.base_agi = self.agi
        self.base_int_ = self.int_
        self.base_str_ = self.str_
        self.base_dex = self.dex
        self.base_luck = self.luck

# Placeholder player, will be set in main.py
Player = None

