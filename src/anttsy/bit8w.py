"""
8-bit codes with term reset added on.

..  code-block:: python
    # Make text foreground pink
    from anttsy.bit8w import FG
    print("Example text" @ FG.c206)
"""

from anttsy.utils import Bit8Slots, StrWrap


def _populate[A](cls: A = None, pre: int = 3) -> A:
    def wrap(cls):
        for x in range(256):
            setattr(cls, 'c' + str(x), StrWrap(f'\033[{pre}8;5;{x}m'))
        return cls

    if cls is None:
        return wrap
    return wrap(cls)


@_populate(pre=3)
class FG(Bit8Slots):
    """Foreground wrapper"""


@_populate(pre=4)
class BG(Bit8Slots):
    """Background wrapper"""
