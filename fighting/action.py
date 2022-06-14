from character.entity import Character
from config import BaseConfig
from fighting.factory import get_fighting_strategy
from base import Thing


def deal_damage(
    attacker: Character, defender: Thing, power: int = BaseConfig.POWER_DEFAULT
) -> None:
    """General function for getting fighting strategy and invoking `deal_damage`."""
    strategy = get_fighting_strategy(opponent=defender)
    strategy.deal_damage(attacker, defender, power)
