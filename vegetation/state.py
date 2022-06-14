from enum import IntEnum, unique


@unique
class VegetationState(IntEnum):
    DESTROYED = 0
    ALIVE = 1
