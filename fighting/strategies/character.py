from typing import Literal

from character.entity import Character
from character.state import CharacterState
from config import BaseConfig
from fighting.exceptions import DealingAllyDamage, DeadParticipant
from fighting.validators import validate_minimum_damage_power
from fraction.ally import are_allies
from localization.position import validate_reachability


def validate_characters_connection(attacker: Character, target: Character) -> None:
    if attacker == target or are_allies(attacker, target):
        raise DealingAllyDamage("You cannot deal damage to ally or yourself.")


def validate_states(attacker: Character, defender: Character) -> None:
    if attacker.state == CharacterState.DEAD:
        raise DeadParticipant("You cannot fight when you are dead.")

    if defender.state == CharacterState.DEAD:
        raise DeadParticipant("You cannot fight with dead character.")


def get_calculated_damage_power(levels_difference: int, power: int) -> int:
    """
    Calculate damage power based on difference in levels.

    * Damage power is increased by 50% when level gap is too high.
    * Damage power is decreased by 50% when level gap is too low.
    * Damage power stays the same when there is no level gap.
    """
    if levels_difference >= BaseConfig.POWER_INCREASED_LEVEL_SPAN:
        return int(power * 1.5)

    if levels_difference <= BaseConfig.POWER_REDUCED_LEVEL_SPAN:
        return int(power * 0.5)

    return power


class CharacterFighting:
    def deal_damage(self, attacker: Character, defender: Character, power: int) -> None:
        validate_reachability(
            attacker.position, defender.position, attacker.type_data.max_range
        )
        validate_minimum_damage_power(power)
        validate_characters_connection(attacker, defender)
        validate_states(attacker, defender)

        calculated_damage = get_calculated_damage_power(
            attacker.level - defender.level, power
        )
        defender.health -= calculated_damage
