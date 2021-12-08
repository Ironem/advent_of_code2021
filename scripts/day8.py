
def count_alpha(mot):
    letters = 0
    for i in mot:
        if i.isalpha():
            letters += 1
    return letters


def check_common(output, motif):
    common = 0
    for x in output:
        if x in motif:
            common += 1
    return common


with open('./inputs/input_day8.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    number_of = [0 for i in range(10)]

    resultat = 0

    for line in lines:
        representation_of_numbers = ["" for i in range(10)]
        IO = line.split(" | ")

        input = IO[0]
        output = IO[1]

        for input in input.split(" "):
            if count_alpha(input) == 2:
                if representation_of_numbers[1] == "":
                    representation_of_numbers[1] = (input)
            elif count_alpha(input) == 4:
                if representation_of_numbers[4] == "":
                    representation_of_numbers[4] = (input)
            elif count_alpha(input) == 3:
                if representation_of_numbers[7] == "":
                    representation_of_numbers[7] = (input)
            elif count_alpha(input) == 7:
                if representation_of_numbers[8] == "":
                    representation_of_numbers[8] = (input)

        output_string = ""

        for output in output.split(" "):
            if count_alpha(output) == 2:
                if representation_of_numbers[1] == "":
                    representation_of_numbers[1] = (output)
                number_of[1] += 1
                output_string += "1"
            elif count_alpha(output) == 4:
                if representation_of_numbers[4] == "":
                    representation_of_numbers[4] = (output)
                number_of[4] += 1
                output_string += "4"
            elif count_alpha(output) == 3:
                if representation_of_numbers[7] == "":
                    representation_of_numbers[7] = (output)
                number_of[7] += 1
                output_string += "7"
            elif count_alpha(output) == 7:
                if representation_of_numbers[8] == "":
                    representation_of_numbers[8] = (output)
                number_of[8] += 1
                output_string += "8"

            # 5 traits avec 2 points commun avec 4 est 2
            # 5 traits qui ne sont pas 2 et qui ont 2 points commun avec 1 est 3
            # 5 traits le reste est 5
            elif count_alpha(output) == 5:
                if check_common(output, representation_of_numbers[4]) == 2:
                    output_string += "2"
                elif check_common(output, representation_of_numbers[1]) == 2:
                    output_string += "3"
                else:
                    output_string += "5"

            # 6 traits avec 4 points commun avec 4 est 9
            # 6 traits avec 2 points commun avec 1 est 0
            # le reste des 6 traints sont 6
            elif count_alpha(output) == 6:
                if check_common(output, representation_of_numbers[4]) == 4:
                    output_string += "9"
                elif check_common(output, representation_of_numbers[1]) == 2:
                    output_string += "0"
                else:
                    output_string += "6"

        resultat += int(output_string)

    # part 1
    print(sum(number_of))
    # part 2
    print(resultat)
    f.close()
