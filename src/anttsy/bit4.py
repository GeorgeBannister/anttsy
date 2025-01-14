"""
4-bit code literals

..  code-block:: python
    # Make text foreground red
    from anttsy.bit4 import FG, RESET
    print(FG.red + "Example text" + RESET)
"""


class FG:
    """Foreground literals"""

    black = '\033[1;30m'
    red = '\033[1;31m'
    green = '\033[1;32m'
    yellow = '\033[1;33m'
    blue = '\033[1;34m'
    magenta = '\033[1;35m'
    cyan = '\033[1;36m'
    white = '\033[1;37m'
    b_black = '\033[1;90m'
    b_red = '\033[1;91m'
    b_green = '\033[1;92m'
    b_yellow = '\033[1;93m'
    b_blue = '\033[1;94m'
    b_magenta = '\033[1;95m'
    b_cyan = '\033[1;96m'
    b_white = '\033[1;97m'


class BG:
    """Background literals"""

    black = '\033[1;40m'
    red = '\033[1;41m'
    green = '\033[1;42m'
    yellow = '\033[1;43m'
    blue = '\033[1;44m'
    magenta = '\033[1;45m'
    cyan = '\033[1;46m'
    white = '\033[1;47m'
    b_black = '\033[1;100m'
    b_red = '\033[1;101m'
    b_green = '\033[1;102m'
    b_yellow = '\033[1;103m'
    b_blue = '\033[1;104m'
    b_magenta = '\033[1;105m'
    b_cyan = '\033[1;106m'
    b_white = '\033[1;107m'
