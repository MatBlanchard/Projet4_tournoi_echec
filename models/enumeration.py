from enum import Enum, auto

class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.name, cls))

class Sexe(ExtendedEnum):
    HOMME = auto()
    FEMME = auto()

class Cadence(ExtendedEnum):
    BULLET = auto()
    BLITZ = auto()
    RAPIDE = auto()
    LONGUE = auto()