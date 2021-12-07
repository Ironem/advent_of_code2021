import statistics


with open('./inputs/input_day7.txt', 'r') as f:
    # with open('test.txt', 'r') as f:
    line = f.readline().split(",")
    line_int = [int(i) for i in line]
    weight = []
    mediane = round(statistics.median(line_int))
    print(mediane)

    avg_1 = int(sum(line_int)/len(line_int))
    avg_2 = round(sum(line_int)/len(line_int))
    print(avg_1)
    print(avg_2)

    fluel_mediane = 0
    fluel_avg_1 = 0
    fluel_avg_2 = 0
    for n in line_int:
        fluel_mediane += abs(mediane-n)
        fluel_avg_1 += int((abs(avg_1-n)+1)*(abs(avg_1-n))/2)
        fluel_avg_2 += int((abs(avg_2-n)+1)*(abs(avg_2-n))/2)

    print(fluel_mediane)
    print(min(fluel_avg_1, fluel_avg_2))
    f.close()
