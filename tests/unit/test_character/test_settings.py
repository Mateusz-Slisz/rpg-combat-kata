from character.state import CharacterState
from config import BaseConfig


def test_character_has_correct_initial_settings(first_character):
    # THEN
    assert first_character.health == BaseConfig.MAX_HEALTH
    assert first_character._max_health == BaseConfig.MAX_HEALTH
    assert first_character.level == BaseConfig.INITIAL_LEVEL
    assert first_character.state == CharacterState.ALIVE


def test_characters_are_not_the_same(first_character, second_character):
    # THEN
    assert first_character != second_character


def test_character_is_dead_when_health_equals_0(first_character):
    # GIVEN
    assert first_character.health != 0
    assert first_character.state == CharacterState.ALIVE

    # WHEN
    first_character.health = 0

    # THEN
    assert first_character.state == CharacterState.DEAD
