import aocd as aocd

f = aocd.get_data(day=10, year=2022)

iterations = [20, 60, 100, 140, 180, 220]

value = 1
cycle = 0
history = []
total = 0

for currentLine in f.splitlines():
    if currentLine.split()[0] == "addx":
        history.append(value)
        cycle += 1

        if cycle+1 in iterations:
            total += (cycle+1)*value
            print(f"cycle: {cycle + 1} - value: {value}")

        value += int(currentLine.split()[1])

        history.append(value)
        cycle += 1

        if cycle+1 in iterations:
            total += (cycle+1)*value
            print(f"cycle: {cycle + 1} - value: {value}")
    else:
        history.append(value)
        cycle += 1

        if cycle + 1 in iterations:
            total += (cycle + 1) * value
            print(f"cycle: {cycle + 1} - value: {value}")

print(f"Total value is: {total}")

