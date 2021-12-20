

def printL(L):
    print('-------------Start of array-------------')
    for item in L:
        print((item))
    print('-------------End of array-------------')


def find_x(x):
    array = []
    [x_min, x_max] = x
    cur = 1
    while somme_partiel(0, cur) < int(x_max):
        if somme_partiel(0, cur) > int(x_min):
            array.append(cur)
        cur += 1
    return array


def somme_partiel(min, max):
    return int((max+min)*(max-min+1)/2)


def find_step(x_array, x_):
    steps = []
    for x in x_array:
        for i in range(x):
            if somme_partiel(i, x) > int(x_[0]):
                tmp = (x-i)
        steps.append(tmp)
    return steps


def find_y(x_array, steps, y):
    y_array = []
    for i in range(len(x_array)):
        x = x_array[i]
        step = steps[i]
        for j in range(int(y[0]), int(y[1])+1):
            y_cur = max(abs(int(y[0])), abs(int(y[1])))
            while y_cur > int(y[0]):
                if y_cur % j == 0 and y_cur-(y_cur//j) > step:
                    cur_step = y_cur-(y_cur//j)
                    while somme_partiel(y_cur-cur_step+1, y_cur) >= int(y[0]):
                        if somme_partiel(y_cur-cur_step+1, y_cur) <= int(y[1]):
                            y_array.append(somme_partiel(0, y_cur))
                        cur_step += 1
                y_cur -= 1
    return y_array


def count_velocity(x, y):
    count = 0
    [x_min, x_max] = [int(x[0]), int(x[1])]
    [y_min, y_max] = [int(y[0]), int(y[1])]
    checked = []
    for x_val in range(0, x_min):
        for i in range(2, 2*x_max):
            x_end = somme_partiel(x_val-i+1, x_val)
            if x_val-i+1 < 0:
                x_end = somme_partiel(0, x_val)
            if x_end <= x_max and x_end >= x_min:
                y_max_ = max(abs(int(y[0])), abs(int(y[1])))
                for y_val in range(-y_max_, y_max_+1):
                    y_end = somme_partiel(y_val-i+1, y_val)
                    if y_end <= y_max and y_end >= y_min and not [x_val, y_val] in checked:
                        checked.append([x_val, y_val])
                        count += 1
    return count


with open('./inputs/input_day17.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    line = f.readline()
    [x_equal, y_equal] = line.split(": ")[1].split(", ")
    x = x_equal.split("=")[1].split("..")
    y = y_equal.split("=")[1].split("..")

    x_array = find_x(x)
    steps = find_step(x_array, x)
    y_array = find_y(x_array, steps, y)
    print("step 1: ", max(y_array))

    count = (int(x[1])-int(x[0])+1)*(int(y[1])-int(y[0])+1)

    # for i in range(2, max(int(x[0]), int(x[1]))+1):
    count += count_velocity(x, y)

    print(count)
    f.close()


def emulation(x, y, y_max):

    cur_x = 0
    cur_y = 0
    max_y = 0
    while cur_y >= y_max:
        cur_x += x
        cur_y += y
        if y > 0:
            max_y += y
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
        y -= 1
    print(cur_x, cur_y, max_y)


# emulation(6, 9, -5)
# emulation(6, 8, -5)
# emulation(6, 7, -5)
# emulation(6, 6, -5)
# emulation(7, 9, -5)
# emulation(7, 8, -5)
# emulation(7, 7, -5)
# emulation(7, 5, -5)
