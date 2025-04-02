"""
8-bit codes.

..  code-block:: python
    # Make text foreground pink
    from anttsy.eight_bit import FG
    print("Example text" @ FG.c206)
"""

__all__ = ['BG', 'FG', 'RESET']

from anttsy.utils import RESET, Bit8Slots, StrWrap


def _populate(cls=None, pre: int = 3):
    def wrap(cls):
        for x in range(256):
            setattr(cls, 'c' + str(x), StrWrap(f'\033[{pre}8;5;{x}m'))
        return cls

    if cls is None:
        return wrap
    return wrap(cls)


@_populate(pre=3)
class FG(Bit8Slots):
    """Foreground color codes"""


@_populate(pre=4)
class BG(Bit8Slots):
    """Background color codes"""
