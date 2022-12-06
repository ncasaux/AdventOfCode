import aocd as aocd
f = aocd.get_data(day=2, year=2022)

total = 0

for i in f.splitlines():
    him = i[0:1]
    me = i[2:3]
    if me == 'X':
        total += 1
        if him == 'C':
            total += 6
        elif him == 'A':
            total += 3
    elif me == 'Y':
        total += 2
        if him == 'A':
            total += 6
        elif him == 'B':
            total += 3
    elif me == 'Z':
        total += 3
        if him == 'B':
            total += 6
        elif him == 'C':
            total += 3

print(total)


