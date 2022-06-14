from typing import Literal

from character.entity import Character
from character.state import CharacterState
from fighting.exceptions import DeadParticipant
from fighting.validators import validate_minimum_damage_power
from localization.position import validate_reachability
from vegetation.entity import Vegetation
from vegetation.state import VegetationState


def validate_states(attacker: Character, defender: Vegetation) -> None:
    if attacker.state == CharacterState.DEAD:
        raise DeadParticipant("You cannot fight when you are dead.")

    if defender.state == VegetationState.DESTROYED:
        raise DeadParticipant("You cannot fight with destroyed vegetation.")


class VegetationFighting:
    def deal_damage(
        self, attacker: Character, defender: Vegetation, power: int
    ) -> None:
        validate_minimum_damage_power(power)
        validate_reachability(
            attacker.position, defender.position, attacker.type_data.max_range
        )
        validate_states(attacker, defender)

        defender.health -= power
