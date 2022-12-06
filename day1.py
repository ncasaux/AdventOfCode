import aocd as aocd
f = aocd.get_data(day=1, year=2022)

sums = []
for e in f.split("\n\n"):
    sums.append(sum(list(map(int,e.splitlines()))))

sums.sort(reverse=True)
print(max(sums))
print(sum(sums[0:3]))