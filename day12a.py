import aocd

f = aocd.get_data(day=12, year=2022)
table = []
startPoint = endPoint = ()
xSize = ySize = 0
itineraryWithPoints = {}

for y in range(len(f.splitlines())):
    ySize = len(f.splitlines())
    currentLine = f.splitlines()[y]
    currentRow = []
    for x in range(len(currentLine)):
        xSize = len(currentLine)
        currentChar = currentLine[x]
        currentRow.append(currentChar)
        if currentChar == "S":
            startPoint = (x, y)
        if currentChar == "E":
            endPoint = (x, y)
    table.append(currentRow)

table[startPoint[1]][startPoint[0]] = "a"
table[endPoint[1]][endPoint[0]] = "z"
minSteps = xSize * ySize


def findPathsToExitFromPoint(p):
    xx = p[0]
    yy = p[1]
    new_points = []
    height = ord(table[yy][xx])

    if xx > 0 and ord(table[yy][xx - 1]) <= height + 1:
        new_point = (xx - 1, yy)
        if new_point not in itineraryWithPoints:
            new_points.append(new_point)
            itineraryWithPoints[new_point] = itineraryWithPoints[p] + 1
    if xx < xSize - 1 and ord(table[yy][xx + 1]) <= height + 1:
        new_point = (xx + 1, yy)
        if new_point not in itineraryWithPoints:
            new_points.append(new_point)
            itineraryWithPoints[new_point] = itineraryWithPoints[p] + 1
    if yy > 0 and ord(table[yy - 1][xx]) <= height + 1:
        new_point = (xx, yy - 1)
        if new_point not in itineraryWithPoints:
            new_points.append(new_point)
            itineraryWithPoints[new_point] = itineraryWithPoints[p] + 1
    if yy < ySize - 1 and ord(table[yy + 1][xx]) <= height + 1:
        new_point = (xx, yy + 1)
        if new_point not in itineraryWithPoints:
            new_points.append(new_point)
            itineraryWithPoints[new_point] = itineraryWithPoints[p] + 1

    return new_points


itineraryWithPoints[startPoint] = 1
new_list = findPathsToExitFromPoint(startPoint)
found_or_stuck = False
while not found_or_stuck:
    if endPoint not in new_list:
        old_list = new_list
        new_list = []
        for i in old_list:
            new_list.extend(findPathsToExitFromPoint(i))
        if len(new_list) == 0:
            found_or_stuck = True
    else:
        print(f"Exit found in {itineraryWithPoints[endPoint] - 1} steps.")
        found_or_stuck = True
