def printL(L):
    print('-------------Start array-------------')
    for item in L:
        print(item)
    print('-------------End array-------------')


def flash(L, i, j):
    res = 1
    if i-1 >= 0:
        if j-1 >= 0:
            if L[i-1][j-1] == 9:
                L[i-1][j-1] += 1
                res += flash(L, i-1, j-1)
            else:
                L[i-1][j-1] += 1
        if j >= 0 and j < len(L[i]):
            if L[i-1][j] == 9:
                L[i-1][j] += 1
                res += flash(L, i-1, j)
            else:
                L[i-1][j] += 1
        if j+1 < len(L[i]):
            if L[i-1][j+1] == 9:
                L[i-1][j+1] += 1
                res += flash(L, i-1, j+1)
            else:
                L[i-1][j+1] += 1

    if i >= 0 and i < len(L):
        if j-1 >= 0:
            if L[i][j-1] == 9:
                L[i][j-1] += 1
                res += flash(L, i, j-1)
            else:
                L[i][j-1] += 1
        if j >= 0 and j < len(L[i]):
            if L[i][j] == 9:
                L[i][j] += 1
                res += flash(L, i, j)
            else:
                L[i][j] += 1
        if j+1 < len(L[i]):
            if L[i][j+1] == 9:
                L[i][j+1] += 1
                res += flash(L, i, j+1)
            else:
                L[i][j+1] += 1
    if i+1 < len(L):
        if j-1 >= 0:
            if L[i+1][j-1] == 9:
                L[i+1][j-1] += 1
                res += flash(L, i+1, j-1)
            else:
                L[i+1][j-1] += 1
        if j >= 0 and j < len(L[i]):
            if L[i+1][j] == 9:
                L[i+1][j] += 1
                res += flash(L, i+1, j)
            else:
                L[i+1][j] += 1
        if j+1 < len(L[i]):
            if L[i+1][j+1] == 9:
                L[i+1][j+1] += 1
                res += flash(L, i+1, j+1,)
            else:
                L[i+1][j+1] += 1
    return res


def check(L):
    item = L[0][0]
    for line in L:
        for fish in line:
            if fish != item:
                return False
    return True


with open('./inputs/input_day11.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    L = []

    for line in lines:
        L_ = []
        for n in line.split("\n")[0]:
            L_.append(int(n))
        L.append(L_)

    # step 1
    # n = 100
    res = 0

    # step 1
    # while n > 0:
    # n -= 1

    # step 2
    step = 0
    while not check(L):
        step += 1

        for i in range(len(L)):
            for j in range(len(L[i])):
                L[i][j] += 1
                if(L[i][j] == 10):
                    res += flash(L, i, j)
        for i in range(len(L)):
            for j in range(len(L[i])):
                if(L[i][j] >= 10):
                    L[i][j] = 0

    printL(L)
    # step 1
    print(res)
    # step 2
    print(step)
    f.close()
