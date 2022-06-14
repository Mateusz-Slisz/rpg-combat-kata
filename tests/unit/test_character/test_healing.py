import pytest

from character.entity import Character
from character.exception import HealingPowerTooSmall, HealingDeadCharacter, HealingEnemy
from character.healing import heal
from character.state import CharacterState
from character.type import CharacterType
from fraction.membership import join_to_fraction


@pytest.mark.parametrize(
    "power, expected_health",
    ((1, 101), (50, 150), (9999999999, 1000)),
)
def test_healing_with_power_above_minimum_adds_correctly_health(power, expected_health):
    # GIVEN
    character = Character(
        character_type=CharacterType.RANGED,
        max_health=1000,
    )
    character.health = 100

    # WHEN
    heal(caster=character, target=character, power=power)

    # THEN
    assert character.health == expected_health


def test_healing_ally_adds_health(first_character, example_fraction):
    # GIVEN
    initial_health = 100
    ally = Character(
        character_type=CharacterType.RANGED,
        max_health=1000,
    )
    ally.health = initial_health
    join_to_fraction(first_character, example_fraction)
    join_to_fraction(ally, example_fraction)

    # WHEN
    heal(caster=first_character, target=ally)

    # THEN
    assert ally.health > initial_health


@pytest.mark.parametrize("power", (-100, -10, 0))
def test_healing_with_power_below_minimum_raises_error(first_character, power):
    # THEN
    with pytest.raises(HealingPowerTooSmall):
        # WHEN
        heal(caster=first_character, target=first_character, power=power)


def test_healing_dead_character_raises_error():
    # GIVEN
    character = Character(
        character_type=CharacterType.RANGED,
        max_health=0,
    )
    assert character.state == CharacterState.DEAD

    # THEN
    with pytest.raises(HealingDeadCharacter):
        # WHEN
        heal(caster=character, target=character)


def test_healing_enemy_character_raises_error(first_character, second_character):
    # THEN
    with pytest.raises(HealingEnemy):
        # WHEN
        heal(caster=first_character, target=second_character)
