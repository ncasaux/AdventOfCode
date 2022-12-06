import aocd as aocd

f = aocd.get_data(day=5, year=2022)
setup, instructions = f.split("\n\n")
crateSize: int = 3
crateSeparatorSize: int = 1
crateTotalSize: int = crateSize + crateSeparatorSize
nbCrateColumn = len(setup.splitlines()[-1]) // (crateSize + crateSeparatorSize) + 1


def populate_table():
    for i in range(len(setup.splitlines()) - 2, -1, -1):
        current_setup_line = setup.splitlines()[i]
        for j in range(nbCrateColumn):
            current_crate = current_setup_line[j * crateTotalSize:j * crateTotalSize + crateSize + 1].strip()
            if current_crate != '': table[j].append(current_crate)


table = {k: [] for k in range(nbCrateColumn)}
print(table)

populate_table()
for currentInstruction in instructions.splitlines():
    currentMove = currentInstruction.split(" ")
    for j in range(0, int(currentMove[1])):
        table[int(currentMove[5]) - 1].append(table[int(currentMove[3]) - 1].pop())

print("part A:")
for x in table.values(): print(x[-1][1], end='')

print("\n")

table = {k: [] for k in range(nbCrateColumn)}
populate_table()
for currentInstruction in instructions.splitlines():
    currentMove = currentInstruction.split(" ")
    for j in range(int(currentMove[1]), 0, -1):
        table[int(currentMove[5]) - 1].append(table[int(currentMove[3]) - 1].pop(-j))

print("part B:")
for x in table.values(): print(x[-1][1], end='')
