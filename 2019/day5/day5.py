
def run_instructions(data, inputInstructions):
    messages = []

    ptr, instr = 0, 0
    while True:

        # print(f"ptr: {ptr}, {data[:20]}")
        # input()

        instr = data[ptr]
        if instr == 99:
            return messages 

        opCode = instr % 100
        param1, param2, _ = ((int(str(instr)[-i]) if (len(str(instr)) >= i) else 0) for i in range(3,6))
        
        if (opCode == 1):
            result = (data[ptr+1] if param1 else data[data[ptr+1]]) + (data[ptr+2] if param2 else data[data[ptr+2]])
            data[data[ptr+3]] = result
            ptr += 4
        
        elif (opCode == 2):
            result = (data[ptr+1] if param1 else data[data[ptr+1]]) * (data[ptr+2] if param2 else data[data[ptr+2]])
            data[data[ptr+3]] = result
            ptr += 4
        
        elif (opCode == 3):
            result = inputInstructions
            data[data[ptr+1]] = result
            ptr += 2
        
        elif (opCode == 4):
            if param1:
                messages.append(data[ptr+1])
            else:
                messages.append(data[data[ptr+1]])
            ptr += 2
        
        elif (opCode == 5):
            if (data[ptr+1] if param1 else data[data[ptr+1]]):
                ptr = (data[ptr+2] if param2 else data[data[ptr+2]])
            else:
                ptr += 3
        
        elif (opCode == 6):
            if not(data[ptr+1] if param1 else data[data[ptr+1]]):
                ptr = (data[ptr+2] if param2 else data[data[ptr+2]])
            else:
                ptr += 3
        
        elif (opCode == 7):
            if (data[ptr+1] if param1 else data[data[ptr+1]]) < (data[ptr+2] if param2 else data[data[ptr+2]]):
                data[data[ptr+3]] = 1
            else:
                data[data[ptr+3]] = 0
            ptr += 4
        
        elif (opCode == 8):
            if (data[ptr+1] if param1 else data[data[ptr+1]]) == (data[ptr+2] if param2 else data[data[ptr+2]]):
                data[data[ptr+3]] = 1
            else:
                data[data[ptr+3]] = 0
            ptr += 4

        else:
            print(f"Wrong code: {instr}, {opCode}")
            return []



for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    data_raw = [line.strip() for line in open(f"2019/day5/{fichier}.txt", "r")][0]

    print("\033[93m--- Part One ---\033[0m")

    data = [int(x) for x in data_raw.split(",")]

    messages = run_instructions(data, 1)
    print(', '.join((str(mess) for mess in messages)))




    print("\n\033[93m--- Part Two ---\033[0m")

    data = [int(x) for x in data_raw.split(",")]

    messages = run_instructions(data, 5)
    print(', '.join((str(mess) for mess in messages)))
    