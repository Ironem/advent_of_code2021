with open('./inputs/input_day1.txt', 'r') as f:
    line_1 = f.readline()
    line_2 = f.readline()
    line_3 = f.readline()
    count = 0
    for line in f:
        A = int(line_1)+int(line_2)+int(line_3)
        B = int(line)+int(line_2)+int(line_3)
        if (B > A):
            count += 1
        line_1 = line_2
        line_2 = line_3
        line_3 = line

    print(count)
    f.close()
