import aocd

f = aocd.get_data(day=14, year=2022)

mapping = dict()

for currentLine in f.splitlines():
    points = currentLine.split(" -> ")
    for i in range(0, len(points) - 1):
        f = complex(int(points[i].split(",")[0]), int(points[i].split(",")[1]))
        t = complex(int(points[i + 1].split(",")[0]), int(points[i + 1].split(",")[1]))
        for k in range(0, int((t - f).real)):
            mapping[f + k] = "#"
        for k in range(0, int((t - f).real), -1):
            mapping[f + k] = "#"
        for k in range(0, int((t - f).imag)):
            mapping[f + k * 1j] = "#"
        for k in range(0, int((t - f).imag), -1):
            mapping[f + k * 1j] = "#"
        mapping[t] = "#"

max_depth = max(list(map(lambda x: int(x.imag), mapping)))
sand_qty = 0
sand_outside = False
while not sand_outside:
    sand_qty += 1
    s = complex(500, 0)
    sand_at_rest = False
    while not sand_at_rest:
        if int((s + 1j).imag) > max_depth:
            sand_outside = True
            break
        elif (s + 1j) not in mapping.keys():
            s = s + 1j
        elif (s - 1 + 1j) not in mapping.keys():
            s = s - 1 + 1j
        elif (s + 1 + 1j) not in mapping.keys():
            s = s + 1 + 1j
        else:
            mapping[s] = "o"
            sand_at_rest = True

print(f"Max number of sand unit at rest: {sand_qty-1}")