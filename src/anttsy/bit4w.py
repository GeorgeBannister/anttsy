"""
4-bit codes with term reset added on.

..  code-block:: python
    # Make text foreground red
    from anttsy.bit4w import FG
    print("Example text" @ FG.red)
"""

from anttsy.utils import StrWrap


class FG:
    """Foreground wrapper"""

    black = StrWrap('\033[1;30m')
    red = StrWrap('\033[1;31m')
    green = StrWrap('\033[1;32m')
    yellow = StrWrap('\033[1;33m')
    blue = StrWrap('\033[1;34m')
    magenta = StrWrap('\033[1;35m')
    cyan = StrWrap('\033[1;36m')
    white = StrWrap('\033[1;37m')
    b_black = StrWrap('\033[1;90m')
    b_red = StrWrap('\033[1;91m')
    b_green = StrWrap('\033[1;92m')
    b_yellow = StrWrap('\033[1;93m')
    b_blue = StrWrap('\033[1;94m')
    b_magenta = StrWrap('\033[1;95m')
    b_cyan = StrWrap('\033[1;96m')
    b_white = StrWrap('\033[1;97m')


class BG:
    """Background wrapper"""

    black = StrWrap('\033[1;40m')
    red = StrWrap('\033[1;41m')
    green = StrWrap('\033[1;42m')
    yellow = StrWrap('\033[1;43m')
    blue = StrWrap('\033[1;44m')
    magenta = StrWrap('\033[1;45m')
    cyan = StrWrap('\033[1;46m')
    white = StrWrap('\033[1;47m')
    b_black = StrWrap('\033[1;100m')
    b_red = StrWrap('\033[1;101m')
    b_green = StrWrap('\033[1;102m')
    b_yellow = StrWrap('\033[1;103m')
    b_blue = StrWrap('\033[1;104m')
    b_magenta = StrWrap('\033[1;105m')
    b_cyan = StrWrap('\033[1;106m')
    b_white = StrWrap('\033[1;107m')
