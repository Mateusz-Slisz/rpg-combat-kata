from character.entity import Character
from character.exception import (
    HealingPowerTooSmall,
    HealingEnemy,
    HealingDeadCharacter,
)
from character.state import CharacterState
from config import BaseConfig
from fraction.ally import are_allies


def validate_minimum_healing_power(power: int) -> None:
    if power <= 0:
        raise HealingPowerTooSmall("Minimum power of healing is 1.")


def validate_heal_target(caster: Character, target: Character) -> None:
    if caster != target and not are_allies(caster, target):
        raise HealingEnemy("You cannot heal enemy character.")

    if target.state == CharacterState.DEAD:
        raise HealingDeadCharacter("You cannot heal dead character.")


def heal(
    caster: Character, target: Character, power: int = BaseConfig.POWER_DEFAULT
) -> None:
    """Heal target for 'power' value."""
    validate_heal_target(caster, target)
    validate_minimum_healing_power(power)

    target.health += power
