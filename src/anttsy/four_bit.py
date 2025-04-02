"""
4-bit codes.

..  code-block:: python
    # Make text foreground red
    from anttsy.four_bit import FG
    print("Example text" @ FG.red)
"""

__all__ = ['BG', 'FG', 'RESET']


from anttsy.utils import RESET, StrWrap


class FG:
    """Foreground color codes"""

    black = StrWrap('\033[1;30m')
    red = StrWrap('\033[1;31m')
    green = StrWrap('\033[1;32m')
    yellow = StrWrap('\033[1;33m')
    blue = StrWrap('\033[1;34m')
    magenta = StrWrap('\033[1;35m')
    cyan = StrWrap('\033[1;36m')
    white = StrWrap('\033[1;37m')
    bright_black = StrWrap('\033[1;90m')
    bright_red = StrWrap('\033[1;91m')
    bright_green = StrWrap('\033[1;92m')
    bright_yellow = StrWrap('\033[1;93m')
    bright_blue = StrWrap('\033[1;94m')
    bright_magenta = StrWrap('\033[1;95m')
    bright_cyan = StrWrap('\033[1;96m')
    bright_white = StrWrap('\033[1;97m')


class BG:
    """Background color codes"""

    black = StrWrap('\033[1;40m')
    red = StrWrap('\033[1;41m')
    green = StrWrap('\033[1;42m')
    yellow = StrWrap('\033[1;43m')
    blue = StrWrap('\033[1;44m')
    magenta = StrWrap('\033[1;45m')
    cyan = StrWrap('\033[1;46m')
    white = StrWrap('\033[1;47m')
    bright_black = StrWrap('\033[1;100m')
    bright_red = StrWrap('\033[1;101m')
    bright_green = StrWrap('\033[1;102m')
    bright_yellow = StrWrap('\033[1;103m')
    bright_blue = StrWrap('\033[1;104m')
    bright_magenta = StrWrap('\033[1;105m')
    bright_cyan = StrWrap('\033[1;106m')
    bright_white = StrWrap('\033[1;107m')
