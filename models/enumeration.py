from enum import Enum, auto

class Sexe(Enum):
    HOMME = auto()
    FEMME = auto()

class Cadence(Enum):
    BULLET = auto()
    BLITZ = auto()
    RAPIDE = auto()