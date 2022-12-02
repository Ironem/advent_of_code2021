

snailfish_number = []


def printL(L):
    print('-------------Start of array-------------')
    for item in L:
        print((item))
    print('-------------End of array-------------')


def addition(snailfish_number, new_number):
    open = 0
    L = []
    for i in range(len(new_number)):
        if new_number[i] == ",":
            pass
        elif new_number[i] == "[":
            open += 1
        elif new_number[i] == "]":
            open -= 1
            t1 = L.pop()
            t2 = L.pop()
            L.append([t2, t1])

        elif int(new_number[i]) >= 0 or int(new_number[i]) <= 9:
            L.append(int(new_number[i]))

    if snailfish_number == []:
        return L[0]
    return [snailfish_number, L[0]]


def add(i, j, k, l, value):
    global snailfish_number
    tmp = snailfish_number[i][j][k][l]
    t = 0
    while type(tmp) == list:
        tmp = tmp[0]
        t += 1
    if t == 1:
        snailfish_number[i][j][k][l][0] += value
    elif t == 2:
        snailfish_number[i][j][k][l][0][0] += value
    elif t == 0:
        snailfish_number[i][j][k][l] += value


def change_val_left(i, j, k, l, val):
    global snailfish_number
    first = True
    cur_i = i
    cur_j = j
    cur_k = k
    cur_l = l
    while cur_i >= 0:
        if not first:
            if type(snailfish_number[cur_i]) == list:
                cur_j = len(snailfish_number[cur_i])-1
            else:
                snailfish_number[cur_i] += val
                return
        while cur_j >= 0:
            if not first:
                if type(snailfish_number[cur_i][cur_j]) == list:
                    cur_k = len(snailfish_number[cur_i][cur_j])-1
                else:
                    snailfish_number[cur_i][cur_j] += val
                    return
            while cur_k >= 0:
                if not first:
                    if type(snailfish_number[cur_i][cur_j][cur_k]) == list:
                        cur_l = len(snailfish_number[cur_i][cur_j][cur_k])
                    else:
                        snailfish_number[cur_i][cur_j][cur_k] += val
                        return
                first = False
                while cur_l-1 >= 0:
                    if type(snailfish_number[cur_i][cur_j][cur_k][cur_l-1]) == int:
                        snailfish_number[cur_i][cur_j][cur_k][cur_l-1] += val
                        return
                    cur_l -= 1
                cur_k -= 1
            cur_j -= 1
        cur_i -= 1


def change_val_right(i, j, k, l, val):
    global snailfish_number
    first = True
    cur_i = i
    cur_j = j
    cur_k = k
    cur_l = l+1
    while cur_i < len(snailfish_number):
        if not first:
            if type(snailfish_number[cur_i]) == list:
                cur_j = 0
            else:
                snailfish_number[cur_i] += val
                # print("droite: ", snailfish_number)
                return
        while cur_j < len(snailfish_number[cur_i]):
            if not first:
                if type(snailfish_number[cur_i][cur_j]) == list:
                    cur_k = 0
                else:
                    snailfish_number[cur_i][cur_j] += val
                    # print("droite: ", snailfish_number)
                    return
            while cur_k < len(snailfish_number[cur_i][cur_j]):
                if not first:
                    if type(snailfish_number[cur_i][cur_j][cur_k]) == list:
                        cur_l = 0
                    else:
                        snailfish_number[cur_i][cur_j][cur_k] += val
                        # print("droite: ", snailfish_number)
                        return
                first = False
                while cur_l < len(snailfish_number[cur_i][cur_j][cur_k]):
                    if type(snailfish_number[cur_i][cur_j][cur_k][cur_l]) == int:
                        # print("return", snailfish_number,
                            #   snailfish_number[cur_i][cur_j][cur_k][cur_l])
                        snailfish_number[cur_i][cur_j][cur_k][cur_l] += val
                        # print("return", snailfish_number,
                        #   snailfish_number[cur_i][cur_j][cur_k][cur_l])
                        return
                    else:
                        add(cur_i, cur_j, cur_k, cur_l, val)
                        return
                cur_k += 1
            cur_j += 1
        cur_i += 1


def expode(i, j, k, l):
    global snailfish_number
    array = snailfish_number[i][j]
    if l-1 < 0:
        # print("if gauche", array[k])
        change_val_left(i, j, k, l, array[k][l][0])
        change_val_right(i, j, k, l, array[k][l][1])
        array[k][l] = 0
        # print(snailfish_number)
    elif l+1 >= len(array[k]):
        # print("if droite", array)
        change_val_right(i, j, k, l, array[k][l][1])
        change_val_left(i, j, k, l, array[k][l][0])

        array[k][l] = 0
        # print(snailfish_number)
    elif l+1 < len(array[k]) and l-1 >= 0:
        # print("elif tout", array[k])
        if type(array[k][l+1]) == list:
            array[k][l+1][0] += array[k][l][1]
        else:
            array[k][l+1] += array[k][l][1]
        if type(array[k][l-1]) == list:
            array[k][l-1][0] += array[k][l][0]
        else:
            array[k][l-1] += array[k][l][0]
        array[k][l] = 0
    else:
        print("else", array[k])


def reduce():
    global snailfish_number
    for i in range(len(snailfish_number)):
        array1 = snailfish_number[i]
        if type(array1) == list:
            for j in range(len(array1)):
                array2 = array1[j]
                if type(array2) == list:
                    for k in range(len(array2)):
                        array3 = array2[k]
                        if type(array3) == list:
                            for l in range(len(array3)):
                                array4 = array3[l]
                                if type(array4) == list:
                                    expode(
                                        i, j, k, l)
                                    return reduce()
                                else:
                                    if array4 >= 10:
                                        # print("array4:", array4)
                                        array3[l] = [
                                            array4//2, array4-array4//2]
                                        return reduce()
                        else:
                            if array3 >= 10:
                                # print("array3:", array3)
                                array2[k] = [array3//2, array3-array3//2]
                                return reduce()
                else:
                    if array2 >= 10:
                        # print("array2:", array2)
                        array1[j] = [array2//2, array2-array2//2]
                        return reduce()
        else:
            if array1 >= 10:
                # print("array1:", array1)
                snailfish_number[i] = [array1//2, array1-array1//2]
                return reduce()
    return


# with open('./inputs/input_day18.txt', 'r') as f:
with open('test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        snailfish_number = addition(snailfish_number, line.split("\n")[0])
        reduce()
    print(snailfish_number)

    f.close()
