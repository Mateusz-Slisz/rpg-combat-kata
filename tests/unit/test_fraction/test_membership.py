import pytest

from fraction.exception import JoiningOwnFraction, LeavingNotOwnFraction
from fraction.entity import Fraction
from fraction.membership import leave_from_fraction, join_to_fraction


def test_joining_to_own_fraction_raises_error(first_character, example_fraction):
    # GIVEN
    first_character.fractions.add(example_fraction)
    assert example_fraction in first_character.fractions

    # WHEN & THEN
    with pytest.raises(JoiningOwnFraction):
        join_to_fraction(character=first_character, fraction=example_fraction)


def test_joining_to_not_own_fraction_adds_fraction_to_character(
    first_character, example_fraction
):
    # GIVEN
    assert example_fraction not in first_character.fractions

    # WHEN
    join_to_fraction(first_character, example_fraction)

    # THEN
    assert example_fraction in first_character.fractions


def test_leaving_not_own_fraction_raises_error(first_character, example_fraction):
    # GIVEN
    assert not first_character.fractions

    # WHEN & THEN
    with pytest.raises(LeavingNotOwnFraction):
        leave_from_fraction(character=first_character, fraction=example_fraction)


def test_leaving_from_own_fraction_removes_fraction_from_character(
    first_character, example_fraction
):
    # GIVEN
    first_character.fractions.add(example_fraction)
    assert first_character.fractions

    # WHEN
    leave_from_fraction(first_character, example_fraction)

    assert not first_character.fractions


def test_joining_to_many_fractions_adds_fractions_to_character(first_character):
    # GIVEN
    fractions = (Fraction("A"), Fraction("B"), Fraction("C"))
    assert not first_character.fractions

    # WHEN
    for fraction in fractions:
        join_to_fraction(first_character, fraction)

    # THEN
    assert len(first_character.fractions) == len(fractions)
