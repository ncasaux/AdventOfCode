import aocd as aocd
f = aocd.get_data(day=3, year=2022)

total = 0

def alpha_order(letter):
    if "a" <= letter <= "z":
        return ord(letter) - 96
    elif "A" <= letter <= "Z":
        return ord(letter) - 38


for i in f.splitlines():

    dictionary = {}
    left = i[:len(i) // 2]
    right = i[len(i) // 2:]

    for j in range(len(left)):
        dictionary[alpha_order(left[j])] = "LEFT"

    for j in range(len(right)):
        if alpha_order(right[j]) in dictionary:
            if dictionary[alpha_order(right[j])] == "LEFT":
                dictionary[alpha_order(right[j])] = "BOTH"

    total += list(dictionary.keys())[list(dictionary.values()).index("BOTH")]

print(total)
