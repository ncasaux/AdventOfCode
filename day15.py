import aocd
import re

mapping = dict()
listing = []
f = aocd.get_data(day=15, year=2022)
target_row = 2000000
xMin = xMax = None

for currentLine in f.splitlines():
    r = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", currentLine)
    Sx, Sy = int(r.group(1)), int(r.group(2))
    Bx, By = int(r.group(3)), int(r.group(4))
    mapping[(Sx, Sy)] = "S"
    mapping[(Bx, By)] = "B"

    dist = abs(Bx - Sx) + abs(By - Sy)

    dist_to_target_row = dist - abs(target_row - Sy)
    for k in range(Sx - dist_to_target_row, Sx + dist_to_target_row + 1):
        if (k, target_row) not in mapping.keys():
            mapping[(k, target_row)] = "#"

nbNoBeacon = len(list(filter(lambda p: p[1] == target_row and mapping[p] == "#", mapping)))
print(f"Beacon cannot be present at {nbNoBeacon} positions at row {target_row}.")