import sys

def rush(x, y):

    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):

        line = ""

        for col in range(x):

            # Special case: single row or single column
            if x == 1 or y == 1:
                line += "B"

            # Top row corners
            elif row == 0 and (col == 0 or col == x - 1):
                line += "A"

            # Bottom row corners
            elif row == y - 1 and (col == 0 or col == x - 1):
                line += "C"

            # Borders
            elif row == 0 or row == y - 1 or col == 0 or col == x - 1:
                line += "B"

            # Inside
            else:
                line += " "

        print(line)