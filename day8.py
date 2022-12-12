import aocd as aocd

f = aocd.get_data(day=8, year=2022)
mapping = []
scores = []

for i in range(len(f.splitlines())):
    mapping.append(list(f.splitlines()[i]))

sideLength = len(mapping)
visibleTrees = 4 * (sideLength - 1)

print(mapping)
for y in range(1, sideLength - 1):
    for x in range(1, sideLength - 1):
        currentTreeHeight = int(mapping[y][x])
        visible = False
        score = 1

        visibleSoFarInCurrentLine = True
        scoreSoFarInCurrentLine = 0
        for xx in range(x-1, -1, -1):
            scoreSoFarInCurrentLine += 1
            if int(mapping[y][xx]) >= currentTreeHeight:
                visibleSoFarInCurrentLine = False
                break
        if visibleSoFarInCurrentLine:
            visible = True

        score *= scoreSoFarInCurrentLine

        visibleSoFarInCurrentLine = True
        scoreSoFarInCurrentLine = 0
        for xx in range(x + 1, sideLength):
            scoreSoFarInCurrentLine += 1
            if int(mapping[y][xx]) >= currentTreeHeight:
                visibleSoFarInCurrentLine = False
                break
        if visibleSoFarInCurrentLine:
            visible = True

        score *= scoreSoFarInCurrentLine

        visibleSoFarInCurrentLine = True
        scoreSoFarInCurrentLine = 0
        for yy in range(y-1, -1, -1):
            scoreSoFarInCurrentLine += 1
            if int(mapping[yy][x]) >= currentTreeHeight:
                visibleSoFarInCurrentLine = False
                break
        if visibleSoFarInCurrentLine:
            visible = True

        score *= scoreSoFarInCurrentLine

        visibleSoFarInCurrentLine = True
        scoreSoFarInCurrentLine = 0

        for yy in range(y + 1, sideLength):
            scoreSoFarInCurrentLine += 1
            if int(mapping[yy][x]) >= currentTreeHeight:
                visibleSoFarInCurrentLine = False
                break
        if visibleSoFarInCurrentLine:
            visible = True

        score *= scoreSoFarInCurrentLine
        scores.append(score)
        if visible:
            visibleTrees += 1

print(f"There are {visibleTrees} visible trees")

print(f"Max score is: {max(scores)}")
