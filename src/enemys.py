from charactersys import Character

Goblin = Character(
    name="Goblin",
    class_="enemy",
    life=10,
    mana=0,
    xp=0,
    lvl=1,
    atk=4,
    defense=1,
    agi=2,
    int_=1,
    str_=3,
    dex=2,
    luck=1,
    skills=["Bite"],
    inventory=["tooth", "leather_helmet"],
    gold=2,
    status_effects=[]
)
Goblin.base_life = Goblin.life

Orc = Character(
    name="Orc",
    class_="enemy",
    life=50,
    mana=0,
    xp=0,
    lvl=2,
    atk=7,
    defense=3,
    agi=2,
    int_=1,
    str_=6,
    dex=2,
    luck=1,
    skills=["Smash"],
    inventory=["club"],
    gold=5,
    status_effects=[]
)
Orc.base_life = Orc.life

Skeleton = Character(
    name="Skeleton",
    class_="enemy",
    life=12,
    mana=0,
    xp=0,
    lvl=2,
    atk=5,
    defense=2,
    agi=3,
    int_=1,
    str_=4,
    dex=2,
    luck=1,
    skills=["Bone Throw"],
    inventory=["rusty_sword"],
    gold=3,
    status_effects=[]
)
Skeleton.base_life = Skeleton.life

Slime = Character(
    name="Slime",
    class_="enemy",
    life=8,
    mana=0,
    xp=0,
    lvl=1,
    atk=3,
    defense=1,
    agi=1,
    int_=1,
    str_=2,
    dex=1,
    luck=2,
    skills=["Dissolve"],
    inventory=["slime_core"],
    gold=1,
    status_effects=[]
)
Slime.base_life = Slime.life

Bandit = Character(
    name="Bandit",
    class_="enemy",
    life=14,
    mana=0,
    xp=0,
    lvl=3,
    atk=6,
    defense=2,
    agi=4,
    int_=2,
    str_=4,
    dex=3,
    luck=2,
    skills=["Quick Stab"],
    inventory=["dagger", "bandana"],
    gold=8,
    status_effects=[]
)
Bandit.base_life = Bandit.life

DarkMage = Character(
    name="Dark Mage",
    class_="enemy",
    life=16,
    mana=20,
    xp=0,
    lvl=4,
    atk=4,
    defense=2,
    agi=3,
    int_=7,
    str_=2,
    dex=3,
    luck=2,
    skills=["Dark Bolt", "Curse"],
    inventory=["magic_staff", "dark_robes"],
    gold=12,
    status_effects=[]
)
DarkMage.base_life = DarkMage.life

Ogre = Character(
    name="Ogre",
    class_="enemy",
    life=30,
    mana=0,
    xp=0,
    lvl=5,
    atk=10,
    defense=5,
    agi=1,
    int_=1,
    str_=9,
    dex=2,
    luck=1,
    skills=["Ground Slam"],
    inventory=["giant_club"],
    gold=15,
    status_effects=[]
)
Ogre.base_life = Ogre.life

DragonWhelp = Character(
    name="Dragon Whelp",
    class_="enemy",
    life=45,
    mana=30,
    xp=0,
    lvl=7,
    atk=14,
    defense=8,
    agi=4,
    int_=6,
    str_=10,
    dex=4,
    luck=3,
    skills=["Fire Breath", "Tail Whip"],
    inventory=["dragon_scale"],
    gold=25,
    status_effects=[]
)
DragonWhelp.base_life = DragonWhelp.life

# This will help for debug porpuses
enemies = [DragonWhelp, DarkMage, Ogre, Orc, Bandit, Slime, Skeleton, Goblin]