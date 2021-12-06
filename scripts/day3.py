

def count_max(L, i):
    c = [0, 0]
    max = 1
    for j in range(len(L)):
        c[int(L[j][i])] += 1

    if c[0] > c[1]:
        max = 0
    L_new = []
    for j in range(len(L)):
        if int(L[j][i]) == max:
            L_new.append(L[j])
    return L_new


def count_min(L, i):
    c = [0, 0]
    min = 1
    for j in range(len(L)):
        c[int(L[j][i])] += 1

    if c[0] <= c[1]:
        min = 0
    L_new = []
    for j in range(len(L)):
        if int(L[j][i]) == min:
            L_new.append(L[j])
    return L_new


def binToDec(b):
    d = 0
    for i in range(len(b)):
        if(int(b[i]) == 1):
            d += pow(2, len(b)-i-1)
    return d


with open('./inputs/input_day3.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    # Comment part is the first part
    # for x in line:
    #     if x == "1":
    #         gamma.append([0, 0])
    #         gamma[i][1] += 1
    #     elif x == "0":
    #         gamma.append([0, 0])
    #         gamma[i][0] += 1
    #     i += 1

    # for line in f:
    #     i = 0
    #     for x in line:
    #         if x == "1":
    #             gamma[i][1] += 1
    #         elif x == "0":
    #             gamma[i][0] += 1
    #         i += 1

    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip("\n")
    L_O = lines
    L_CO2 = lines
    i = 0
    while(i < len(lines[0]) and len(L_O) > 1):
        L_O = count_max(L_O, i)
        i += 1
        oxygene = binToDec(L_O[0])

    i = 0
    while(i < len(lines[0]) and len(L_CO2) > 1):
        L_CO2 = count_min(L_CO2, i)
        i += 1

    CO2 = binToDec(L_CO2[0])

    print(oxygene*CO2)
    # gammaInBytes = ""
    # epsilonInBytes = ""
    # gammaInDecimal = 0
    # epsilonInDecimal = 0
    # for i in range(len(gamma)):
    #     if(gamma[i][0] > gamma[i][1]):
    #         gammaInBytes += str(0)
    #         epsilonInBytes += str(1)
    #         epsilonInDecimal += pow(2, len(gamma)-i-1)
    #     else:
    #         gammaInBytes += str(1)
    #         epsilonInBytes += str(0)
    #         gammaInDecimal += pow(2, len(gamma)-i-1)

    # print(gammaInBytes)
    # print(gammaInDecimal)
    # print(epsilonInBytes)
    # print(epsilonInDecimal)
    # print(epsilonInDecimal*gammaInDecimal)
    f.close()
