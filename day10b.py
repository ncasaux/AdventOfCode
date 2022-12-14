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
            # print(f"cycle: {cycle + 1} - value: {value}")

        value += int(currentLine.split()[1])

        history.append(value)
        cycle += 1

        if cycle+1 in iterations:
            total += (cycle+1)*value
            # print(f"cycle: {cycle + 1} - value: {value}")
    else:
        history.append(value)
        cycle += 1

        if cycle + 1 in iterations:
            total += (cycle + 1) * value
            # print(f"cycle: {cycle + 1} - value: {value}")

s = "#"
for k in range(1,len(history)):
    if k % 40 - 1 <= history[k-1]  <= k % 40 + 1:
        s+="#"
    else:
        s+="."

for l in range(0,6):
    print(s[l*40:l*40+39])