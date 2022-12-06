import aocd as aocd
f = aocd.get_data(day=3, year=2022)

total = 0

def alpha_order(letter):
    if "a" <= letter <= "z":
        return ord(letter) - 96
    elif "A" <= letter <= "Z":
        return ord(letter) - 38


l = f.splitlines()
for i in range(0, len(l) - 1, 3):
    s1 = l[i]
    s2 = l[i + 1]
    s3 = l[i + 2]
    dictionary = {}

    for j in range(len(s1)):
        i1 = alpha_order(s1[j])
        if not i1 in dictionary:
            dictionary[i1] = 1

    for j in range(len(s2)):
        i2 = alpha_order(s2[j])
        if i2 in dictionary and dictionary[i2] == 1:
            dictionary[i2] = 2

    for j in range(len(s3)):
        i3 = alpha_order(s3[j])
        if i3 in dictionary and dictionary[i3] == 2:
            dictionary[i3] = 3

    total += list(dictionary.keys())[list(dictionary.values()).index(3)]

print(total)
