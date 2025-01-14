# anttsy

An opionated ANSI color code library.

```python
# Use 4-bit wrappers
from anttsy.bit4w import FG, BG
print("Example text" @ (FG.red | BG.white))

# Use 8-bit wrappers
from anttsy.bit8w import FG, BG
print("Example text" @ (FG.c101 | BG.c202))

# Use 4-bit literals
from anttsy.bit4 import FG, BG, RESET
print(FG.red + BG.white + "Example text" + RESET)

# Use 8-bit literals
from anttsy.bit8 import FG, BG, RESET
print(FG.c101 + BG.c202 + "Example text" + RESET)
```

> **Note**
> This library currently doesn't enable ANSI codes on Windows (Use colorama)
> This library doesn't check whether you are in a tty
