import sys

def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""

        for col in range(x):

            # Corners
            if (row == 0 or row == y - 1) and (col == 0 or col == x - 1):
                line += "o"
            
            # Top and bottom borders
            elif row == 0 or row == y - 1:
                line += "-"

            # Left and right borders
            elif col == 0 or col == x - 1:
                line += "|"

            # Inside space
            else:
                line += " "

        print(line)