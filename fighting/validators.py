from fighting.exceptions import DamagePowerTooSmall


def validate_minimum_damage_power(power: int) -> None:
    if power <= 0:
        raise DamagePowerTooSmall("Minimum power of dealing damage is 1.")
