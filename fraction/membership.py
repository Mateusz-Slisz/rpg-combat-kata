from character.entity import Character
from fraction.exception import LeavingNotOwnFraction, JoiningOwnFraction
from fraction.entity import Fraction


def join_to_fraction(character: Character, fraction: Fraction) -> None:
    if fraction in character.fractions:
        raise JoiningOwnFraction("Character is already in a fraction.")

    character.fractions.add(fraction)


def leave_from_fraction(character: Character, fraction: Fraction) -> None:
    if fraction not in character.fractions:
        raise LeavingNotOwnFraction("Character is not in a fraction.")

    character.fractions.remove(fraction)
