def printL(L):
    print('-------------Start of array-------------')
    for item in L:
        print("".join(item))
    print('-------------End of array-------------')


def insert(template, i, element):
    left_part = template[:i+1]
    right_part = template[i+1:]
    template = left_part + element + right_part
    return template


def next_step(template, rules, counter):
    tmp = template
    j = 0
    for i in range(len(template)-1):
        pair = (template[i]+template[i+1])
        for rule in rules:
            if rule[0] == pair:
                tmp = insert(tmp, i+j, rule[1])
                j += 1
                break
    return tmp


with open('./inputs/input_day14.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    lines = f.readlines()

    firstLine = True

    template = ""
    template_part2 = ""

    rules = []

    counter = {}

    for line in lines:
        if firstLine:
            firstLine = False
            template = line.split("\n")[0]
            template_part2 = line.split("\n")[0]
        elif line != "\n":
            rules.append(line.split("\n")[0].split(" -> "))

    # part 1 lazy mode
    step = 10
    for i in range(step):
        template = next_step(template, rules, counter)

    for letter in template:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    most_element = max(counter.values())
    least_element = min(counter.values())

    print("part1", most_element-least_element)

    # part 2 : we don't calculate the template but only pairs
    temp2 = {}

    for i in range(len(template_part2)-1):
        pair = template_part2[i]+template_part2[i+1]
        if pair in temp2:
            temp2[pair] += 1
        else:
            temp2[pair] = 1

    step_part2 = 40
    for i in range(step_part2):
        new_temp2 = temp2.copy()
        for pair in temp2.keys():
            for rule in rules:
                if rule[0] == pair:
                    new_pair_1 = pair[0] + rule[1]
                    new_pair_2 = rule[1] + pair[1]
                    if new_pair_1 in new_temp2:
                        new_temp2[new_pair_1] += temp2[pair]
                    else:
                        new_temp2[new_pair_1] = temp2[pair]
                    if new_pair_2 in new_temp2:
                        new_temp2[new_pair_2] += temp2[pair]
                    else:
                        new_temp2[new_pair_2] = temp2[pair]

                    new_temp2[pair] -= temp2[pair]
                    if(new_temp2[pair] == 0):
                        new_temp2.pop(pair)
                    break
        temp2 = new_temp2

    counter2 = {}
    for key in temp2.keys():
        if key[0] in counter2:
            counter2[key[0]] += temp2[key]
        else:
            counter2[key[0]] = temp2[key]

    last_letter = template_part2[len(template_part2)-1]
    if last_letter in counter2:
        counter2[last_letter] += 1
    else:
        counter2[last_letter] = 1

    most_element_part2 = max(counter2.values())
    least_element_part2 = min(counter2.values())

    print("part2", most_element_part2-least_element_part2)

    f.close()
