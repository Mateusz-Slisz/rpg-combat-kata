import pytest

from character.entity import Character
from character.state import CharacterState
from character.type import CharacterType
from fighting.exceptions import DamagePowerTooSmall, DeadParticipant
from localization.exception import DistanceOutOfRange
from localization.position import Position2D
from vegetation.entity import Vegetation
from vegetation.state import VegetationState
from vegetation.type import VegetationType


@pytest.mark.parametrize("power", (-100, -10, 0))
def test_dealing_damage_with_power_below_minimum_raises_error(
    first_character, tree, power, vegetation_fighting
):
    # THEN
    with pytest.raises(DamagePowerTooSmall):
        # WHEN
        vegetation_fighting.deal_damage(first_character, tree, power=power)


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
def test_dealing_damage_when_character_and_vegetation_are_not_in_range_raises_error(
    attacker_position, defender_position, character_type, vegetation_fighting
):
    # GIVEN
    attacker = Character(character_type=character_type, position=attacker_position)
    defender = Vegetation(
        vegetation_type=VegetationType.TREE, max_health=100, position=defender_position
    )

    # THEN
    with pytest.raises(DistanceOutOfRange):
        # WHEN
        vegetation_fighting.deal_damage(attacker, defender, 30)


def test_dealing_damage_when_attacker_is_dead_raises_error(
    first_character, tree, vegetation_fighting
):
    # GIVEN
    first_character.health = 0
    assert first_character.state == CharacterState.DEAD

    # THEN
    with pytest.raises(DeadParticipant):
        # WHEN
        vegetation_fighting.deal_damage(first_character, tree, 30)


def test_dealing_damage_when_defender_is_destroyed_raises_error(
    first_character, tree, vegetation_fighting
):
    # GIVEN
    tree.health = 0
    assert tree.state == VegetationState.DESTROYED

    # THEN
    with pytest.raises(DeadParticipant):
        # WHEN
        vegetation_fighting.deal_damage(first_character, tree, 30)


def test_dealing_damage_subtracts_health(first_character, tree, vegetation_fighting):
    # GIVEN
    assert tree.health == tree._max_health

    # WHEN
    vegetation_fighting.deal_damage(first_character, tree, 30)

    # THEN
    assert tree.health < tree._max_health
