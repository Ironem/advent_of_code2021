def printL(L):
    print('-------------Start array-------------')
    for item in L:
        print(item)
    print('-------------End array-------------')


def compter(L):
    res = 0
    for line in L:
        for n in line:
            if n >= 2:
                res += 1
    print(res)
    return res


with open('./inputs/input_day5.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()
    L_ = [[0]*(1000)]*(1000)
    L = []
    for l in L_:
        L.append(l.copy())

    for line in lines:
        coordonnees = line.split(" ")
        start = coordonnees[0].split(',')
        end = coordonnees[2].split("\n")[0].split(',')
        if(start[0] == end[0]):
            min_ = min(int(start[1]), int(end[1]))
            max_ = max(int(start[1]), int(end[1]))
            for i in range(min_, max_+1):
                L[i][int(start[0], 10)] += 1

        elif(start[1] == end[1]):
            min_ = min(int(start[0]), int(end[0]))
            max_ = max(int(start[0]), int(end[0]))
            for i in range(min_, max_+1):
                L[int(start[1], 10)][i] += 1
        # Comment the else part for the first part
        else:
            min_x = min(int(start[0]), int(end[0]))
            max_x = max(int(start[0]), int(end[0]))
            diff_x = max_x-min_x
            min_y = min(int(start[1]), int(end[1]))
            max_y = max(int(start[1]), int(end[1]))
            diff_y = max_y-min_y
            if(diff_x == diff_y):
                if(int(start[0]) > int(end[0]) and int(start[1]) > int(end[1])):
                    for i in range(diff_x+1):
                        L[int(start[1])-i][int(start[0])-i] += 1
                elif(int(start[0]) < int(end[0]) and int(start[1]) < int(end[1])):
                    for i in range(diff_x+1):
                        L[int(start[1])+i][int(start[0])+i] += 1
                elif(int(start[0]) > int(end[0]) and int(start[1]) < int(end[1])):
                    for i in range(diff_x+1):
                        L[int(start[1])+i][int(start[0])-i] += 1
                elif(int(start[0]) < int(end[0]) and int(start[1]) > int(end[1])):
                    for i in range(diff_x+1):
                        L[int(start[1])-i][int(start[0])+i] += 1

    resultat = compter(L)
    f.close()
