from dataclasses import dataclass
from enum import Enum, unique


@dataclass(frozen=True)
class TypeSettings:
    name: str
    max_range: int


@unique
class CharacterType(Enum):
    MELEE = TypeSettings("Melee", 2)
    RANGED = TypeSettings("Ranged", 20)
