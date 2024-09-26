import itertools
from math import factorial




def run_instructions(data, inputs, ptr=0):
    messages = []

    instr = 0
    while True:

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
            if inputs:
                result = inputs.pop(0)  
            else:
                return {"messages":messages, "data":data, "ptr":ptr}
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
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data_raw = [line.strip() for line in open(f"2019/day7/{fichier}.txt", "r") if line.strip() != ""][0]

    print("\033[93m--- Part One ---\033[0m")

    data_cleaned = [int(x) for x in data_raw.split(",")]

    numberAplifiers = 5
    totalPhases = factorial(numberAplifiers)
    maxThruster = 0

    for j, sequence_order in enumerate(itertools.permutations(range(numberAplifiers))):
        lastSignal = [0]
        for i in range(numberAplifiers):
            lastSignal = run_instructions(data_cleaned, [sequence_order[i], lastSignal[-1]])
        maxThruster = max(maxThruster, lastSignal[0])

    print(f"Max thruster signal: {maxThruster}")
    



    print("\n\033[93m--- Part Two ---\033[0m")

    # not threads shit
    """
    maxThruster = 0
    aplifiers_states = [{} for _ in range(numberAplifiers)]

    for j, sequence_order in enumerate(itertools.permutations(range(5, 10))):
        print(f"Testing sequence {sequence_order} ({j+1}/{totalPhases})")
        
        lastSignal = [0]
        i = 0
        while i < 2*numberAplifiers:
            print(f"i: {i}, lastSignal: {([sequence_order[i]] + lastSignal) if (i<numberAplifiers) else lastSignal}")

            lastSignal = run_instructions(data_cleaned, ([sequence_order[i]] + lastSignal) if (i<numberAplifiers) else lastSignal)

            if type(lastSignal) == dict:
                aplifiers_states[i % numberAplifiers] = lastSignal


            
        maxThruster = max(maxThruster, lastSignal[0])

    print(f"Max thruster signal: {maxThruster}")
    """
    

