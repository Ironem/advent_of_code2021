def printL(L):
    print('-------------Start array-------------')
    for item in L:
        print(item)
    print('-------------End array-------------')


def check_side_top(L, i, isBassin):
    min = []
    for j in range(len(L[i])):
        if(j == 0):
            if L[i][j] < L[i][j+1] and L[i][j] < L[i+1][j+1] and L[i][j] < L[i+1][j]:
                if isBassin:
                    min.append([i, j])
                else:
                    min.append(L[i][j])
        elif j == len(L[i])-1:
            if L[i][j] < L[i][j-1] and L[i][j] < L[i+1][j-1] and L[i][j] < L[i+1][j]:
                if isBassin:
                    min.append([i, j])
                else:
                    min.append(L[i][j])
        else:
            if L[i][j] < L[i][j-1] and L[i][j] < L[i+1][j+1] and L[i][j] < L[i+1][j] and L[i][j] < L[i][j+1] and L[i][j] < L[i+1][j-1]:
                if isBassin:
                    min.append([i, j])
                else:
                    min.append(L[i][j])
    return min


def check_side_bottom(L, i, isBassin):
    min = []
    for j in range(len(L[i])):
        if(j == 0):
            if L[i][j] < L[i][j+1] and L[i][j] < L[i-1][j+1] and L[i][j] < L[i-1][j]:
                if isBassin:
                    min.append([i, j])
                else:
                    min.append(L[i][j])
        elif j == len(L[i])-1:
            if L[i][j] < L[i][j-1] and L[i][j] < L[i-1][j-1] and L[i][j] < L[i-1][j]:
                if isBassin:
                    min.append([i, j])
                else:
                    min.append(L[i][j])
        else:
            if L[i][j] < L[i][j-1] and L[i][j] < L[i-1][j+1] and L[i][j] < L[i-1][j] and L[i][j] < L[i][j+1] and L[i][j] < L[i-1][j-1]:
                if isBassin:
                    min.append([i, j])
                else:
                    min.append(L[i][j])
    return min


def check(L, i, j):
    if L[i][j] < L[i-1][j-1] and L[i][j] < L[i-1][j] and L[i][j] < L[i-1][j+1]:
        if L[i][j] < L[i][j-1] and L[i][j] < L[i][j+1]:
            if L[i][j] < L[i+1][j-1] and L[i][j] < L[i+1][j] and L[i][j] < L[i+1][j+1]:
                return True
    return False


def checkMin(L):
    mins = []
    for i in range(len(L)):
        if i == 0:
            min = check_side_top(L, i, False)
            for item in min:
                mins.append(item)
        elif i == len(L)-1:
            min = check_side_bottom(L, i, False)
            for item in min:
                mins.append(item)

        else:
            for j in range(len(L[i])):
                if(j == 0 or j == len(L[i])-1):
                    if L[i][j] < L[i-1][j] and L[i][j] < L[i+1][j]:
                        if j == 0 and L[i][j] < L[i-1][j+1] and L[i][j] < L[i][j+1] and L[i][j] < L[i+1][j+1]:
                            mins.append(L[i][j])
                        elif j == len(L[i])-1 and L[i][j] < L[i-1][j-1] and L[i][j] < L[i][j-1] and L[i][j] < L[i+1][j-1]:
                            mins.append(L[i][j])
                else:
                    if check(L, i, j):
                        mins.append(L[i][j])
    return mins


def findBassin(L, coordonnees):
    i = coordonnees[0]
    j = coordonnees[1]
    if(L[i][j] == 9):
        L[i][j] = 9
        return 0
    L[i][j] = 9
    size = 1
    if i-1 >= 0:
        if j >= 0 and j < len(L[i]):
            size += findBassin(L, [i-1, j])
    if i >= 0 and i < len(L):
        if j-1 >= 0:
            size += findBassin(L, [i, j-1])
        if j+1 < len(L[i]):
            size += findBassin(L, [i, j+1])
    if i+1 < len(L):
        if j >= 0 and j < len(L[i]):
            size += findBassin(L, [i+1, j])

    return size


def checkSizeBassin(L):

    coordonnees_array = []
    for i in range(len(L)):
        if i == 0:
            min = check_side_top(L, i, True)
            for coordonnees in min:
                coordonnees_array.append(coordonnees)

        elif i > 0 and i < len(L)-1:
            for j in range(len(L[i])):
                if(j == 0 or j == len(L[i])-1):
                    if L[i][j] < L[i-1][j] and L[i][j] < L[i+1][j]:
                        if j == 0 and L[i][j] < L[i-1][j+1] and L[i][j] < L[i][j+1] and L[i][j] < L[i+1][j+1]:
                            coordonnees_array.append([i, j])
                        elif j == len(L[i])-1 and L[i][j] < L[i-1][j-1] and L[i][j] < L[i][j-1] and L[i][j] < L[i+1][j-1]:
                            coordonnees_array.append([i, j])
                else:
                    if check(L, i, j):
                        coordonnees_array.append([i, j])

        else:
            min = check_side_bottom(L, i, True)
            for coordonnees in min:
                coordonnees_array.append(coordonnees)

    res = 1

    size_bassins = []

    for coordonnees in coordonnees_array:
        size_bassins.append(findBassin(L, coordonnees))
    size_bassins.sort(reverse=True)
    # 113 104 102
    for i in range(3):
        res *= size_bassins[i]

    return res


with open('./inputs/input_day9.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    L = []

    for line in lines:
        L_ = []
        for n in line.split("\n")[0]:
            L_.append(int(n))
        L.append(L_)

    mins = checkMin(L)

    result = checkSizeBassin(L)
    # printL(L)
    # part 1
    print(sum(mins)+len(mins))
    # part 2
    print(result)
    f.close()
