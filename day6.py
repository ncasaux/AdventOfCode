import aocd as aocd

f = aocd.get_data(day=6, year=2022)


def get_position_of_marker(length):
    i = 0
    while i <= len(f) - length:
        s = set(f[i:i + length])
        if len(s) == length:
            break
        i += 1
    return i + length


print(f"Matching string of part A is at position:", get_position_of_marker(4))
print(f"Matching string of part B is at position:", get_position_of_marker(14))
