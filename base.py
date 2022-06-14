from abc import ABC

from localization.position import Position2D


class Thing(ABC):
    """Base class for all beings in the RPG game."""

    def __init__(self, max_health: int, position: Position2D = Position2D(0, 0)):
        self._health = self._max_health = max_health
        self.position = position

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set health to zero or below."""
        if value > self._max_health:
            value = self._max_health
        if value < 0:
            value = 0

        self._health = value
