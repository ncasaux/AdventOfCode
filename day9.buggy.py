import aocd as aocd
import math

f = aocd.get_data(day=9, year=2022)
knots = [0j for k in range(10)]
points = set()

for currentLine in f.splitlines():
    direction = currentLine[0]
    length = int(currentLine[2:])
    for i in range(length):
        match direction:
            case "R":
                knots[0] += 1
            case "L":
                knots[0] += -1
            case "U":
                knots[0] += 1j
            case "D":
                knots[0] += -1j

        for k in range(1, len(knots)):
            if abs(knots[k - 1] - knots[k]) > math.sqrt(2):
                match knots[k - 1] - knots[k]:
                    case 2:
                        knots[k] += 1
                    case -2:
                        knots[k] += -1
                    case 2j:
                        knots[k] += 1j
                    case -2j:
                        knots[k] += -1j
                    case 2 + 1j | 1 + 2j:
                        knots[k] += (1 + 1j)
                    case 2 - 1j | 1 - 2j:
                        knots[k] += (1 - 1j)
                    case -2 + 1j | -1 + 2j:
                        knots[k] += (-1 + 1j)
                    case -2 - 1j | -1 - 2j:
                        knots[k] += (-1 - 1j)

        points.add(knots[-1])

print(f"Tail visited {len(points)} points.")
