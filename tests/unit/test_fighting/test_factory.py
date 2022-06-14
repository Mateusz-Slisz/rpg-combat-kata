import pytest

from character.entity import Character
from character.type import CharacterType
from fighting.factory import get_fighting_strategy
from fighting.strategies.character import CharacterFighting
from base import Thing


def test_get_fighting_strategy_return_strategy_when_exists():
    # GIVEN
    opponent = Character(character_type=CharacterType.RANGED)

    # WHEN
    strategy = get_fighting_strategy(opponent)

    # THEN
    assert isinstance(strategy, CharacterFighting)


def test_get_fighting_strategy_raises_error_when_does_not_exist():
    # GIVEN
    class DummyThing(Thing):
        pass

    opponent = DummyThing(max_health=100)

    # WHEN & THEN
    with pytest.raises(NotImplementedError):
        get_fighting_strategy(opponent)
