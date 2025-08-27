from dataclasses import dataclass, field
from typing import List, Dict
from src.skillsys import data

skills_disponiveis = []

@dataclass
class Character:
    """
    Representa um personagem de RPG com atributos comuns.

    Atributos:
        name (str): Nome do personagem.
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
    skills: List[str] = field(default_factory=list)
    inventory: List[str] = field(default_factory=list)
    gold: int = 0
    status_effects: List[str] = field(default_factory=list)
    
# Exemplo de player
Player = Character(
    name="Daniel",
    life=20,
    mana=10,
    xp=0,
    lvl=1,
    atk=5,
    defense=2,
    agi=3,
    int_=4,
    str_=5,
    dex=3,
    luck=2,
    skills=["Slash"],  # Only skills available at level 1
    inventory=["Potion", "Sword"],
    gold=10,
    status_effects=[]
)

for category in data["skills"]:
    for skill in data["skills"][category]:
        if skill["level_required"] <= Player.lvl:
            skills_disponiveis.append(skill)
