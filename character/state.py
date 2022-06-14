from enum import IntEnum, unique


@unique
class CharacterState(IntEnum):
    DEAD = 0
    ALIVE = 1
