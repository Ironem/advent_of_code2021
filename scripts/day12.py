def printObj(O):
    print('-------------Start object-------------')
    print('Key    Velues...')
    for item in O:
        print(item, "   ", O.get(item))
    print('-------------End object-------------')


def printL(L):
    print('-------------Start array-------------')
    for item in L:
        print(item)
    print('-------------End array-------------')


def findNextStep1(L, current, paths, currentPath):
    for step in L[current]:
        nextPath = currentPath.copy()
        if step == "end":
            paths.append(nextPath)
        elif step.islower():
            if currentPath.count(step) < 1:
                nextPath.append(step)
                findNextStep1(L, step, paths, nextPath)
        elif step.isupper():
            nextPath.append(step)
            findNextStep1(L, step, paths, nextPath)


def findNextStep2(L, current, paths, currentPath, twice):
    for step in L[current]:
        nextPath = currentPath.copy()
        if step == "end":
            paths.append(nextPath)
        elif step.islower():
            if currentPath.count(step) == 0:
                nextPath.append(step)
                findNextStep2(L, step, paths, nextPath, twice)
            elif currentPath.count(step) == 1 and not twice:
                nextPath.append(step)
                findNextStep2(L, step, paths, nextPath, True)
        elif step.isupper():
            nextPath.append(step)
            findNextStep2(L, step, paths, nextPath, twice)


with open('./inputs/input_day12.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    L = {}
    # Orgnize the input as an object
    for line in lines:
        relationship = line.split("\n")[0].split("-")
        if relationship[1] != "start" and relationship[0] != "end":
            if not L.get(relationship[0]):
                L[relationship[0]] = [relationship[1]]
            elif not relationship[1] in L.get(relationship[0]):
                if relationship[1] != "start":
                    L.get(relationship[0]).append(relationship[1])
        if relationship[0] != "start" and relationship[1] != "end":
            if not L.get(relationship[1]):
                L[relationship[1]] = [relationship[0]]
            elif not relationship[0] in L.get(relationship[1]):
                L.get(relationship[1]).append(relationship[0])

    printObj(L)

    paths_1 = []
    paths_2 = []
    for start in L["start"]:
        currentPath = [start]
        findNextStep1(L, start, paths_1, currentPath)
        findNextStep2(L, start, paths_2, currentPath, False)

    # printL(paths_1)
    print("setp 1", len(paths_1))
    # printL(paths_2)
    print("setp 2", len(paths_2))
    f.close()
