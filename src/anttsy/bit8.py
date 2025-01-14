"""
8-bit code literals

..  code-block:: python
    # Make text foreground pink
    from anttsy.bit8 import FG, RESET
    print(FG.c206 + "Example text" + RESET)
"""

from anttsy.utils import Bit8Slots


def _populate[A](cls: A = None, pre: int = 3) -> A:
    def wrap(cls):
        for x in range(256):
            setattr(cls, 'c' + str(x), f'\033[{pre}8;5;{x}m')
        return cls

    if cls is None:
        return wrap
    return wrap(cls)


@_populate(pre=3)
class FG(Bit8Slots):
    """Foreground literals"""


@_populate(pre=4)
class BG(Bit8Slots):
    """Background literals"""
