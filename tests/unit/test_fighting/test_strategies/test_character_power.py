import pytest

from config import BaseConfig
from fighting.strategies.character import get_calculated_damage_power


@pytest.mark.parametrize(
    "levels_difference, input_power, expected_power",
    (
        (BaseConfig.POWER_INCREASED_LEVEL_SPAN, 10, 15),
        (BaseConfig.POWER_INCREASED_LEVEL_SPAN + 1, 50, 75),
    ),
)
def test_dmg_power_is_increased_when_levels_difference_is_too_high(
    levels_difference, input_power, expected_power
):
    # WHEN & THEN
    assert get_calculated_damage_power(levels_difference, input_power) == expected_power


@pytest.mark.parametrize(
    "levels_difference, input_power, expected_power",
    (
        (BaseConfig.POWER_REDUCED_LEVEL_SPAN, 10, 5),
        (BaseConfig.POWER_REDUCED_LEVEL_SPAN - 1, 33, 16),
    ),
)
def test_dmg_power_is_reduced_when_levels_difference_is_too_low(
    levels_difference, input_power, expected_power
):
    # WHEN & THEN
    assert get_calculated_damage_power(levels_difference, input_power) == expected_power


@pytest.mark.parametrize(
    "levels_difference",
    range(
        BaseConfig.POWER_REDUCED_LEVEL_SPAN,
        BaseConfig.POWER_INCREASED_LEVEL_SPAN,
    )[1:],
)
def test_dmg_power_is_not_changed_when_there_is_no_levels_difference(levels_difference):
    # GIVEN
    input_power, expected_power = 100, 100

    # WHEN & THEN
    assert get_calculated_damage_power(levels_difference, input_power) == expected_power
