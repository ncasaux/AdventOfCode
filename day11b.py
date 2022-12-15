import aocd as aocd
import math

f = aocd.get_data(day=11, year=2022)
monkeys = []

for currentBlock in f.split("\n\n"):
    id = int(currentBlock.splitlines()[0].replace(":", "")[-1])
    items = list(map(int, currentBlock.splitlines()[1].replace(",", "").strip().split(" ")[2:]))
    operation = currentBlock.splitlines()[2].strip().split(" ")[4:]
    divider = int(currentBlock.splitlines()[3].strip().split(" ")[-1])
    trueMonkey = int(currentBlock.splitlines()[4].strip().split(" ")[-1])
    falseMonkey = int(currentBlock.splitlines()[5].strip().split(" ")[-1])

    monkeys.append([id, items, operation, divider, trueMonkey, falseMonkey, 0])

for h in range(10000):
    for i in range(len(monkeys)):
        for j in monkeys[i][1]:
            if monkeys[i][2][0] == "+":
                val = j + int(monkeys[i][2][1])
            else:
                if monkeys[i][2][1] == "old":
                    val = j * j
                else:
                    val = j * int(monkeys[i][2][1])
            # val = math.trunc(val / 3)
            if val % monkeys[i][3] == 0:
                val = val % monkeys[monkeys[i][4]][3]
                monkeys[monkeys[i][4]][1].append(val)
            else:
                val = val % monkeys[monkeys[i][5]][3]
                monkeys[monkeys[i][5]][1].append(val)
            monkeys[i][6] += 1
        monkeys[i][1].clear()

level = []
for k in monkeys:
    level.append(k[-1])

# print(level)
# print(monkeys)
level.sort()
print(f"level is: {level[-1]*level[-2]}")
