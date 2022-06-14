from vegetation.entity import Vegetation
from vegetation.state import VegetationState
from vegetation.type import VegetationType


def test_vegetation_has_correct_initial_settings(tree):
    # THEN
    assert tree.health == tree._max_health
    assert tree.state == VegetationState.ALIVE


def test_various_vegetation_are_not_the_same():
    # THEN
    assert Vegetation(vegetation_type=VegetationType.TREE, max_health=1) != Vegetation(
        vegetation_type=VegetationType.TREE, max_health=1
    )


def test_vegetation_is_destroyed_when_health_equals_0(tree):
    # GIVEN
    assert tree.health != 0
    assert tree.state == VegetationState.ALIVE

    # WHEN
    tree.health = 0

    # THEN
    assert tree.state == VegetationState.DESTROYED
