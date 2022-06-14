from typing import Final


class BaseConfig:
    # character base settings
    MAX_HEALTH: Final[int] = 1000
    INITIAL_LEVEL: Final[int] = 1

    # character damage's power settings
    POWER_INCREASED_LEVEL_SPAN: Final[int] = 5
    POWER_REDUCED_LEVEL_SPAN: Final[int] = -5

    POWER_DEFAULT: Final[int] = 30
