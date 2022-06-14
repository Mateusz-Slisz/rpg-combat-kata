class CharacterException(Exception):
    pass


class HealingPowerTooSmall(CharacterException):
    pass


class HealingEnemy(CharacterException):
    pass


class HealingDeadCharacter(CharacterException):
    pass
