import pytest

from character.entity import Character
from character.state import CharacterState
from character.type import CharacterType
from config import BaseConfig
from fighting.exceptions import DamagePowerTooSmall, DealingAllyDamage, DeadParticipant
from fraction.membership import join_to_fraction
from localization.exception import DistanceOutOfRange
from localization.position import Position2D


@pytest.mark.parametrize(
    "power, expected_health",
    ((1, 999), (50, 950), (9999999999, 0)),
)
def test_dealing_damage_with_power_above_minimum_subtracts_health(
    first_character, power, expected_health, character_fighting
):
    # GIVEN
    initial_health = 1000
    second_character = Character(
        character_type=CharacterType.RANGED,
        max_health=initial_health,
    )

    # WHEN
    character_fighting.deal_damage(first_character, second_character, power=power)

    # THEN
    assert second_character.health == expected_health


@pytest.mark.parametrize(
    "attacker_level, expected_health",
    (
        (10 + BaseConfig.POWER_INCREASED_LEVEL_SPAN, 850),
        (10 + BaseConfig.POWER_REDUCED_LEVEL_SPAN, 950),
    ),
)
def test_dealing_damage_when_power_is_increased_or_reduced(
    attacker_level, expected_health, character_fighting
):
    # GIVEN
    attacker = Character(
        character_type=CharacterType.RANGED,
        level=attacker_level,
    )
    defender = Character(
        character_type=CharacterType.RANGED,
        max_health=1000,
        level=10,
    )

    # WHEN
    character_fighting.deal_damage(attacker, defender, power=100)

    # THEN
    assert defender.health == expected_health


@pytest.mark.parametrize("power", (-100, -10, 0))
def test_dealing_damage_with_power_below_minimum_raises_error(
    first_character, second_character, power, character_fighting
):
    # THEN
    with pytest.raises(DamagePowerTooSmall):
        # WHEN
        character_fighting.deal_damage(first_character, second_character, power=power)


def test_dealing_damage_to_ally_raises_error(
    first_character, second_character, example_fraction, character_fighting
):
    # GIVEN
    join_to_fraction(first_character, example_fraction)
    join_to_fraction(second_character, example_fraction)

    # THEN
    with pytest.raises(DealingAllyDamage):
        # WHEN
        character_fighting.deal_damage(first_character, second_character, 30)


def test_dealing_damage_to_yourself_raises_error(first_character, character_fighting):
    # THEN
    with pytest.raises(DealingAllyDamage):
        # WHEN
        character_fighting.deal_damage(first_character, first_character, 30)


@pytest.mark.parametrize(
    "attacker_position, defender_position, character_type",
    (
        (
            Position2D(0, 0),
            Position2D(0, CharacterType.MELEE.value.max_range + 1),
            CharacterType.MELEE,
        ),
        (
            Position2D(0, 0),
            Position2D(0, CharacterType.RANGED.value.max_range + 1),
            CharacterType.RANGED,
        ),
    ),
)
def test_dealing_damage_when_characters_are_not_in_range_raises_error(
    attacker_position, defender_position, character_type, character_fighting
):
    # GIVEN
    attacker = Character(character_type=character_type, position=attacker_position)
    defender = Character(
        character_type=CharacterType.RANGED, position=defender_position
    )

    # THEN
    with pytest.raises(DistanceOutOfRange):
        # WHEN
        character_fighting.deal_damage(attacker, defender, 30)


@pytest.mark.parametrize(
    "attacker_position, defender_position, character_type",
    (
        (
            Position2D(0, 0),
            Position2D(0, CharacterType.MELEE.value.max_range),
            CharacterType.MELEE,
        ),
        (
            Position2D(0, 0),
            Position2D(0, CharacterType.RANGED.value.max_range),
            CharacterType.RANGED,
        ),
    ),
)
def test_dealing_damage_when_characters_are_in_range_subtracts_health(
    attacker_position, defender_position, character_type, character_fighting
):
    # GIVEN
    attacker = Character(character_type=character_type, position=attacker_position)
    max_health = 1000
    defender = Character(
        character_type=CharacterType.RANGED,
        position=defender_position,
        max_health=max_health,
    )

    # WHEN
    character_fighting.deal_damage(attacker, defender, 30)

    # THEN
    assert defender.health != max_health


def test_dealing_damage_when_attacker_is_dead_raises_error(
    first_character, second_character, character_fighting
):
    # GIVEN
    first_character.health = 0
    assert first_character.state == CharacterState.DEAD

    # THEN
    with pytest.raises(DeadParticipant):
        # WHEN
        character_fighting.deal_damage(first_character, second_character, 30)


def test_dealing_damage_when_defender_is_dead_raises_error(
    first_character, second_character, character_fighting
):
    # GIVEN
    second_character.health = 0
    assert second_character.state == CharacterState.DEAD

    # THEN
    with pytest.raises(DeadParticipant):
        # WHEN
        character_fighting.deal_damage(first_character, second_character, 30)
