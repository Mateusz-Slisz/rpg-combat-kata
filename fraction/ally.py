from character.entity import Character
from fraction.entity import Fraction


def get_common_fractions(*fraction_lists: set[Fraction]) -> set[Fraction]:
    """Return common fractions among fraction lists."""
    return set.intersection(*fraction_lists)


def are_allies(*characters: Character) -> bool:
    """Check whether Characters are considered allies."""
    fraction_lists = [character.fractions for character in characters]

    return bool(get_common_fractions(*fraction_lists))
