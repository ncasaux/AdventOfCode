import aocd as aocd
import math

f = aocd.get_data(day=9, year=2022)
h = t = 0j
points = set()

for currentLine in f.splitlines():
    direction = currentLine[0]
    length = int(currentLine[2:])
    for i in range(length):
        match direction:
            case "R":
                h += 1
            case "L":
                h += -1
            case "U":
                h += 1j
            case "D":
                h += -1j

        if abs(h - t) > math.sqrt(2):
            match h - t:
                case 2:
                    t += 1
                case -2:
                    t += -1
                case 2j:
                    t += 1j
                case -2j:
                    t += -1j
                case 2 + 1j | 1 + 2j | 2 + 2j:
                    t += (1 + 1j)
                case 2 - 1j | 1 - 2j | 2 - 2j:
                    t += (1 - 1j)
                case -2 + 1j | -1 + 2j | -2 + 2j:
                    t += (-1 + 1j)
                case -2 - 1j | -1 - 2j | -2 - 2j:
                    t += (-1 - 1j)

        points.add(t)

print(f"Tail visited {len(points)} points.")
