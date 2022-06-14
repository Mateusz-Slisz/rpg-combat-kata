from dataclasses import dataclass
from math import sqrt

from localization.exception import DistanceOutOfRange


@dataclass(frozen=True)
class Position2D:
    x: int
    y: int


def get_distance_between(from_: Position2D, to: Position2D) -> float:
    distance_between = sqrt((to.y - from_.y) ** 2 + (to.x - from_.x) ** 2)

    return round(distance_between, 2)


def validate_reachability(
    first: Position2D, second: Position2D, max_range: int
) -> None:
    distance_between: float = get_distance_between(first, second)

    if distance_between > max_range:
        raise DistanceOutOfRange(f"Distance out of max range: '{max_range}'.")
