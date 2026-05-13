# cherrysms_python_project
Python technical test — character-based rectangle drawing in the terminal.

## Overview
Each assignment implements a `rush(x, y)` function inside a `rush.py` file. The function draws a rectangle of width `x` and height `y` using specific characters for corners and edges. All output goes to stdout; invalid input goes to stderr.

## Structure
```
rush-1-1/   # Rectangle outline using o (corners), - (top/bottom), | (sides)
rush-1-2/   # Rectangle outline using / (top-left, bottom-right), \ (top-right, bottom-left), * (edges)
rush-1-3/   # Rectangle using A (top corners), C (bottom corners), B (edges)
rush-1-4/   # Rectangle using A (left corners), C (right corners), B (edges) — top and bottom are symmetric
rush-1-5/   # Rectangle using A/C corners on top mirrored to C/A on bottom
```

## Usage
Each `rush(x, y)` function takes a width `x` and a height `y` and prints the pattern to stdout. If either value is ≤ 0, it prints `Invalid size` to stderr.

Run via the provided `main.py`:
```bash
python main.py 4 4
```

`main.py` imports and calls the `rush` function from the current assignment's `rush.py`:
```python
import sys
from rush import rush

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py x y")
    else:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        rush(x, y)
```

## Rules
- Language: **Python** only
- Only the `print()` function may be used to produce output
- Do not include a `main` function in your delivery — the evaluator provides its own
- No binary files, temp files, cache files, `__pycache__`, or `.pyc` files in the submission
- Runtime errors, exceptions, and crashes result in **disqualification**

## Delivery
Push all source `.py` files to a public GitHub or GitLab repository following the directory structure above (e.g. `rush-1-1/rush.py`, `rush-1-2/rush.py`, etc.), then share the repository link.

## Examples

**rush-1-1** — `rush(4, 4)`:
```
o--o
|  |
|  |
o--o
```

**rush-1-2** — `rush(4, 4)`:
```
/**\
*  *
*  *
\**/
```

**rush-1-3** — `rush(4, 4)`:
```
ABBA
B  B
B  B
CBBC
```

**rush-1-4** — `rush(4, 4)`:
```
ABBC
B  B
B  B
ABBC
```

**rush-1-5** — `rush(4, 4)`:
```
ABBC
B  B
B  B
CBBA
```