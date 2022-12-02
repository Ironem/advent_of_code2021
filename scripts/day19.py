
import math

sum_version = 0


def printL(L):
    print('-------------Start of array-------------')
    for item in L:
        print((item))
    print('-------------End of array-------------')


def decode_4(binary, i, data):
    start_byte = binary[i:i+1]
    i += 1
    data_type = binary[i:i+4]
    i = i+4
    if int(start_byte) == 0:
        data += data_type
        return (i, int(data, 2))
    else:
        data += data_type
        return decode_4(binary, i, data)


def decode_else(binary, i, type_id):
    length_id = binary[i:i+1]
    i += 1
    res_array = []
    if int(length_id) == 1:
        number_of_packets = int(binary[i:i+11], 2)
        i += 11
        for k in range(number_of_packets):
            res = decode(binary, i)
            res_array.append(res[1])
            i = res[0]

    else:
        total_length = int(binary[i:i+15], 2)
        i += 15
        current_i = i
        while i-current_i < total_length:
            res = decode(binary, i)
            res_array.append(res[1])
            i = res[0]
    if type_id == 0:
        res = 0
        for data in res_array:
            res += data
        return (i, res)
    elif type_id == 1:
        res = 1
        for data in res_array:
            res *= data
        return (i, res)
    elif type_id == 2:
        return (i, min(res_array))
    elif type_id == 3:
        return (i, max(res_array))
    elif type_id == 5:
        return (i, int(res_array[0] > res_array[1]))
    elif type_id == 6:
        return (i, int(res_array[0] < res_array[1]))
    elif type_id == 7:
        return (i, int(res_array[0] == res_array[1]))


def decode(binary, i):
    global sum_version
    version = int(binary[i:i+3], 2)
    i += 3
    sum_version += version
    type_id = int(binary[i:i+3], 2)
    i += 3

    if type_id == 4:
        return decode_4(binary, i, "")
    else:
        result = decode_else(binary, i, type_id)
        return result


with open('./inputs/input_day16.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    line = f.readline()

    scale = 16  # equals to hexadecimal

    binary = bin(int(line, scale))[2:].zfill(len(line) * int(math.log2(scale)))

    res = decode(binary, 0)
    print("part 1: ", sum_version)
    print("part 2: ", res[1])
    f.close()
