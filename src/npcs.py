from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Npc:
    name: str                     # Nome do NPC
    role: str                     # Papel (vendedor, aldeão, guerreiro, etc.)
    description: str              # Pequena descrição
    phrases: List[str] = field(default_factory=list)  # Frases que pode falar
    items: List[str] = field(default_factory=list)    # Itens que possui ou vende
    quests: List[Dict] = field(default_factory=list)  # Quests que oferece
    hostility: bool = False       # Se pode atacar o jogador
    location: Optional[str] = None  # Local onde aparece (aldeia, floresta, etc.)
    does: Optional[str] = None    # O que costuma fazer (patrulhar, vender, rezar...)
