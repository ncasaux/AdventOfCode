import aocd as aocd
f = aocd.get_data(day=2, year=2022)

total = 0

for i in f.splitlines():
    him = i[0:1]
    me = i[2:3]

    if me == 'X':
        total +=0
        if him == 'C':
            total += 2
        elif him == 'B':
            total += 1
        elif him == 'A':
            total += 3
    elif me == 'Y':
        total += 3
        if him == 'A':
            total += 1
        elif him == 'B':
            total += 2
        elif him == 'C':
            total += 3
    elif me == 'Z':
        total += 6
        if him == 'B':
            total += 3
        elif him == 'C':
            total += 1
        elif him == 'A':
            total += 2

print(total)


