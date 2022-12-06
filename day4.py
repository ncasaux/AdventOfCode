import aocd as aocd

f = aocd.get_data(day=4, year=2022)

total = 0
for i in f.splitlines():
    left_min = int(i.rsplit(",")[0].rsplit("-")[0])
    left_max = int(i.rsplit(",")[0].rsplit("-")[1])
    right_min = int(i.rsplit(",")[1].rsplit("-")[0])
    right_max = int(i.rsplit(",")[1].rsplit("-")[1])

    if left_min <= right_min and left_max >= right_max or left_min >= right_min and left_max <= right_max:
        total += 1

print(f"Total Part One is: {total}")

noMatchingTotal = 0
for i in f.splitlines():
    left_min = int(i.rsplit(",")[0].rsplit("-")[0])
    left_max = int(i.rsplit(",")[0].rsplit("-")[1])
    right_min = int(i.rsplit(",")[1].rsplit("-")[0])
    right_max = int(i.rsplit(",")[1].rsplit("-")[1])

    if left_max < right_min or left_min > right_max:
        noMatchingTotal += 1

total = len(f.splitlines()) - noMatchingTotal

print(f"Total Part Two is: {total}")
