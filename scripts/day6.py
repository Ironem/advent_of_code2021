

with open('./inputs/input_day6.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    line = f.readline().split(",")

    # Version 1
    # n = len(line)
    # Fish = []
    # for item in line:
    #     Fish.append(int(item))
    # print(Fish)

    # days = 80

    # while days > 0:
    #     for i in range(len(Fish)):
    #         if(Fish[i] > 0):
    #             Fish[i] -= 1
    #         else:
    #             Fish[i] = 6
    #             Fish.append(8)
    #     days -= 1

    # print(len(Fish))

    # Version 2
    Fish = [0]*9

    for fish in line:
        Fish[int(fish)] += 1

    days = 256

    while days > 0:
        tmp = Fish[0]
        for i in range(len(Fish)-1):
            if(i == 6):
                Fish[i] = Fish[i+1]+tmp
            else:
                Fish[i] = Fish[i+1]
        Fish[8] = tmp
        days -= 1

    res = 0
    for fishes in Fish:
        res += fishes
    print(res)

    f.close()
