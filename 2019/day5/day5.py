for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    data = [line.strip() for line in open(f"2019/day5/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    output = ""
    for line in data:
        output += line
    data = [int(x) for x in output.split(",")]

    ptr = 0
    while ptr < len(data):
        if data[ptr] == 99:
            break
        else:
            opcode = data[ptr] % 100
            modes = [int(x) for x in str(data[ptr] // 100)]
            modes.reverse()
            while len(modes) < 3:
                modes.append(0)
            if opcode == 1:
                if modes[0] == 0:
                    param1 = data[data[ptr+1]]
                else:
                    param1 = data[ptr+1]
                if modes[1] == 0:
                    param2 = data[data[ptr+2]]
                else:
                    param2 = data[ptr+2]
                data[data[ptr+3]] = param1 + param2
                ptr += 4
            elif opcode == 2:
                if modes[0] == 0:
                    param1 = data[data[ptr+1]]
                else:
                    param1 = data[ptr+1]
                if modes[1] == 0:
                    param2 = data[data[ptr+2]]
                else:
                    param2 = data[ptr+2]
                data[data[ptr+3]] = param1 * param2
                ptr += 4
            elif opcode == 3:
                data[data[ptr+1]] = int(input("Input: "))
                ptr += 2
            elif opcode == 4:
                if modes[0] == 0:
                    param1 = data[data[ptr+1]]
                else:
                    param1 = data[ptr+1]
                print("Output:", param1)
                ptr += 2
            else:
                print("Unknown opcode:", opcode)
                break


    print("\n\033[93m--- Part Two ---\033[0m")
    