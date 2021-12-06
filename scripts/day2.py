with open('./inputs/input_day2.txt', 'r') as f:
    forward = 0
    depth = 0
    aim = 0
    for line in f:
        words = line.split(" ")
        if(words[0] == "forward"):
            forward += int(words[1])*aim
            depth += int(words[1])
        elif(words[0] == "up"):
            aim -= int(words[1])
        elif(words[0] == "down"):
            aim += int(words[1])
    print(forward*depth)
    f.close()
