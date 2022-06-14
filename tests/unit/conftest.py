import pytest

from character.entity import Character
from character.type import CharacterType
from fraction.entity import Fraction
from vegetation.entity import Vegetation
from vegetation.type import VegetationType


@pytest.fixture
def first_character() -> Character:
    return Character(character_type=CharacterType.MELEE)


@pytest.fixture
def second_character() -> Character:
    return Character(character_type=CharacterType.MELEE)


@pytest.fixture
def example_fraction() -> Fraction:
    return Fraction(name="Example fraction")


@pytest.fixture
def tree() -> Vegetation:
    return Vegetation(vegetation_type=VegetationType.TREE, max_health=1000)
