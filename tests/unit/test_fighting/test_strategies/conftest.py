import pytest

from fighting.strategies.character import CharacterFighting
from fighting.strategies.vegetation import VegetationFighting


@pytest.fixture
def character_fighting() -> CharacterFighting:
    return CharacterFighting()


@pytest.fixture
def vegetation_fighting() -> VegetationFighting:
    return VegetationFighting()
