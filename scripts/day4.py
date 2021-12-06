def rayer(tab, n):
    tab_bis = tab.copy()
    for tableau in tab_bis:
        if tableau != "Finded":
            for line in tableau:
                for i in range(len(line)):
                    if(int(line[i]) == int(n)):
                        line[i] = True
    return tab_bis


def result(tab, k, i, number, string):
    if(string == "horizontal"):

        reste_s = 0
        for j in range(len(tab[k])):
            if j != i:
                for n in tab[k][j]:
                    if n != True:
                        reste_s += int(n)

        if reste_s == 0:
            print(tab, k)
        print("horizontal", int(number)*reste_s)
        tab[k] = "Finded"
    else:
        if tab[k] != "Finded":
            reste_s = 0

            longueur = len(tab[k][0])
            hauteur = len(tab[k])

            for i in range(longueur):
                for j in range(hauteur):
                    if tab[k][j][i] != True:
                        reste_s += int(tab[k][j][i])

            print("vertical", int(number)*reste_s)
            tab[k] = "Finded"


def check(tab, tab_copy, number):
    for k in range(len(tab)):
        tableau = tab[k]
        if tableau != "Finded":
            # Check rows
            for j in range(len(tableau)):
                line = tableau[j]
                lineCheck = True
                for i in range(len(line)):
                    if(line[i] != True):
                        lineCheck = False
                if lineCheck:
                    result(tab_copy, k, j, number, "horizontal")

            # Check cols
            longueur = len(tableau[0])
            hauteur = len(tableau)

            for i in range(longueur):
                lineCheck = True
                for j in range(hauteur):
                    if(tableau[j][i] != True):
                        lineCheck = False
                if lineCheck:
                    result(tab_copy, k, i, number, "vertical")


with open('./inputs/input_day4.txt', 'r') as f:
    # with open('test.txt', 'r') as f:

    first_line = f.readline()
    numbers = first_line.split('\n')[0].split(',')
    # print(numbers)

    f.readline()

    lines = f.readlines()
    i = 0
    tableaux = []
    tableaux_copy = []

    tableau = []
    tableau_copy = []
    for line in lines:
        if(i < 5):
            i += 1
            line_ = line.split("\n")[0].split(" ")
            indice = []
            for j in range(len(line_)):
                if line_[j] == "":
                    indice.append(j)
            for j in range(len(indice)):
                line_.pop(indice[len(indice)-j-1])

            tableau.append(line_)
        elif(i == 5):
            i = 0
            tableaux.append(tableau)
            tableau = []

    tableaux.append(tableau)
    tableaux_copy = tableaux

    for number in numbers:
        rayer(tableaux, number)
        if(check(tableaux, tableaux_copy, number)):
            print("Finded")
            # for the first part you need to decomment the break
            # break

    f.close()
