from typing import Protocol, Any

from character.entity import Character
from fighting.strategies.character import CharacterFighting
from fighting.strategies.vegetation import VegetationFighting
from base import Thing
from vegetation.entity import Vegetation


class FightingStrategy(Protocol):
    def deal_damage(self, attacker: Character, defender: Any, power: int) -> None:
        ...


STRATEGIES: dict[type[Thing], type[FightingStrategy]] = {
    Character: CharacterFighting,
    Vegetation: VegetationFighting,
}


def get_fighting_strategy(opponent: Thing) -> FightingStrategy:
    """Select proper fighting strategy based on `opponent`."""
    try:
        strategy = STRATEGIES[type(opponent)]
        return strategy()
    except KeyError:
        raise NotImplementedError(
            f"Fighting strategy for opponent's type "
            f"'{opponent.__class__.__name__}' is not implemented!"
        )
