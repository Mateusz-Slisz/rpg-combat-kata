from localization.position import Position2D
from base import Thing
from vegetation.state import VegetationState
from vegetation.type import VegetationType


class Vegetation(Thing):
    def __init__(
        self,
        vegetation_type: VegetationType,
        max_health: int,
        position: Position2D = Position2D(0, 0),
    ):
        self._vegetation_type = vegetation_type
        super().__init__(max_health=max_health, position=position)

    @property
    def state(self) -> VegetationState:
        return VegetationState.ALIVE if self.health > 0 else VegetationState.DESTROYED
