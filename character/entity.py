from character.state import CharacterState
from character.type import CharacterType, TypeSettings
from config import BaseConfig
from fraction.entity import Fraction
from localization.position import Position2D
from base import Thing


class Character(Thing):
    def __init__(
        self,
        character_type: CharacterType,
        position: Position2D = Position2D(0, 0),
        max_health: int = BaseConfig.MAX_HEALTH,
        level: int = BaseConfig.INITIAL_LEVEL,
    ) -> None:
        self._level = level
        self._type = character_type
        self._fractions: set[Fraction] = set()
        self.position = position
        super().__init__(max_health=max_health, position=position)

    @property
    def level(self) -> int:
        return self._level

    @property
    def type_data(self) -> TypeSettings:
        return self._type.value

    @property
    def state(self) -> CharacterState:
        return CharacterState.ALIVE if self.health > 0 else CharacterState.DEAD

    @property
    def fractions(self) -> set[Fraction]:
        return self._fractions
