def printL(L):
    print('-------------Start array-------------')
    for item in L:
        print(item)
    print('-------------End array-------------')


with open('./inputs/input_day10.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    L = []

    error = {"}": 0, ">": 0, "]": 0, ")": 0}

    first_part_scores = {"}": 1197, ">": 25137, "]": 57, ")": 3}

    second_part_scores = {"}": 3, ">": 4, "]": 2, ")": 1}

    open_chunk = {"(": 1, "[": 2, "{": 3, "<": 4}

    close_chunk = {")": 9, "]": 8, "}": 7, ">": 6}

    for line in lines:
        L_ = []
        for n in line.split("\n")[0]:
            L_.append(n)
        L.append(L_)

    part2_res = []

    for line in L:
        prev_chunks = []
        isIncomplete = True
        for chunk in line:
            if chunk in open_chunk:
                prev_chunks.append(chunk)
            else:
                last_open_chunk = prev_chunks.pop()
                if(open_chunk[last_open_chunk]+close_chunk[chunk] != 10):
                    error[chunk] += 1
                    isIncomplete = False
                    break
        if isIncomplete:
            tmp = 0
            for i in range(len(prev_chunks)):
                tmp = tmp*5+open_chunk[prev_chunks[len(prev_chunks) - i-1]]
            part2_res.append(tmp)

    res = 0

    for key in error:
        res += first_part_scores[key]*error[key]

    print(res)
    print(part2_res)
    part2_res.sort()
    ind = len(part2_res) // 2
    print(part2_res[ind])

    f.close()
