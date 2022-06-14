class FightingException(Exception):
    pass


class DealingAllyDamage(FightingException):
    pass


class DamagePowerTooSmall(FightingException):
    pass


class DeadParticipant(FightingException):
    pass
