def printL(L):
    print('-------------Start of paper-------------')
    for item in L:
        print("".join(item))
    print('-------------End of paper-------------')


def fold(paper, fold_coord):
    if fold_coord[0] == "x":
        max_col = len(paper[0])
        col = int(fold_coord[1])
        for j in range(len(paper)):
            for i in range(col):
                if(paper[j][max_col-1-i]) == "#":
                    paper[j][i] = "#"
            for i in range(col+1):
                paper[j].pop()

    else:
        line = int(fold_coord[1])
        max_line = len(paper)
        for j in range(line):
            for i in range(len(paper[j])):
                if(paper[max_line-1-j][i]) == "#":
                    paper[j][i] = "#"
        for j in range(line+1):
            paper.pop()


def count(paper):
    res = 0
    for line in paper:
        for item in line:
            if item == "#":
                res += 1
    return res


with open('./inputs/input_day13.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    dots_Coordonnees = []
    isDots = True
    fold_Coordonnees = []

    for line in lines:
        if line == "\n":
            isDots = False
        elif isDots:
            coordonnee = line.split("\n")[0].split(",")
            dots_Coordonnees.append([int(coordonnee[0]), int(coordonnee[1])])
        else:
            fold_Coordonnees.append(line.split(
                "\n")[0].split(" ")[2].split("="))

    first_x = False
    first_y = False
    for fold_coor in fold_Coordonnees:
        if fold_coor[0] == "x" and not first_x:
            first_x = True
            max_coord_x = int(fold_coor[1])
        elif fold_coor[0] == "y" and not first_y:
            first_y = True
            max_coord_y = int(fold_coor[1])

    # we need the right size of the paper which is the double +1 of the fold position
    paper = [["." for i in range(max_coord_x*2+1)]
             for i in range(max_coord_y*2+1)]

    # draw # on paper
    for coordonnee in dots_Coordonnees:
        paper[coordonnee[1]][coordonnee[0]] = "#"

    first_time = True

    for fold_coor in fold_Coordonnees:
        fold(paper, fold_coor)
        if first_time:
            first_time = False
            res = count(paper)
            print("count # for part 1:", res)

    printL(paper)

    f.close()
