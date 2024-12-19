import heapq




def get_combo(register, value):
    combo = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: register["A"],
        5: register["B"],
        6: register["C"],
        7: 0
    }
    return combo[value]


def execute_program(registers, program, programString=False):
    outputString = ""
    i = 0

    while i < len(program):
        opcode, operand = program[i], program[i+1]
        # print(f"{i}: {opcode} {operand}")
        
        if (opcode == 0):
            # A / combo -> A (truncated)
            registers["A"] = registers["A"] // 2**get_combo(registers, operand)

        elif (opcode == 1):
            # B XOR literal -> B
            registers["B"] = registers["B"] ^ operand

        elif (opcode == 2):
            # combo % 8 -> B
            registers["B"] = get_combo(registers, operand) % 8

        elif (opcode == 3):
            # jump if A != 0
            if (registers["A"] != 0):
                i = operand
                continue

        elif (opcode == 4):
            # B XOR C -> B
            registers["B"] = registers["B"] ^ registers["C"]

        elif (opcode == 5):
            # combo % 8 -> print
            outputString += f"{get_combo(registers, operand) % 8},"

        elif (opcode == 6):
            # A / combo -> B (truncated)
            registers["B"] = registers["A"] // 2**get_combo(registers, operand)

        elif (opcode == 7):
            # A / combo -> C (truncated)
            registers["C"] = registers["A"] // 2**get_combo(registers, operand)

        if (programString and (outputString not in programString)):
            return outputString

        i += 2

    return outputString


def chain_input(A, B, C):
    if ((A % 8) ^ 1) == 0:
        return -1, -1, -1
    # C = A // ((A % 8) ^ 1)
    B = (((A%8) ^ 1) ^ (A // ((A%8) ^ 1))) ^ 4
    A = A // 8
    return A, B, C


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day17/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    registers = {}
    program = []
    
    for line in data:
        if ("Register" in line):
            _register, letter, value = line.split()
            registers[letter.strip(":")] = int(value)
        else:
            program = [int(nb) for nb in line.split()[1].split(",")]


    finalString = execute_program(registers, program)

    print(f"Program output: {finalString.strip(",")}")




    print("\n\033[93m--- Part Two ---\033[0m")

    # Test: 0(0) 3(3) 28(4) 229(5) 1_835(3) 14_680(0) 117_440

    # Start from the end: right approach
    if (fichier == "test"):
        queue = [(0, (0))]
        while queue:
            depth, (valueA) = heapq.heappop(queue)
            if (depth == len(program)):
                print(f"Found: {valueA}")
                break

            commandToMatch = program[-(depth+1)]
            if (valueA % 8 != commandToMatch):
                continue

            for i in range(8):
                heapq.heappush(queue, (depth+1, (valueA*8+i)))

    else:
        queue = [(0, (0))]
        while queue:
            depth, (valueA) = heapq.heappop(queue)
            if (depth == len(program)):
                print(f"Found: {valueA}")
                break

            for i in range(8):
                A = valueA*8 + i
                if (((A % 8) ^ 1) == 0):
                    continue
                valueB = ((((A%8) ^ 1) ^ (A // ((A%8) ^ 1))) ^ 4)
                if (valueB%8 == commandToMatch):
                    heapq.heappush(queue, (depth+1, (valueA*8+i)))

            print(queue)

    # break
    """
    # Start from the start: wrong approach
    programLenght = len(program)
    lowBoundA = 1
    highBoundA = 7
    for _ in range(programLenght-1):
        lowBoundA *= 8
        highBoundA = (8*highBoundA)+7

    print(f"Bounds: {lowBoundA=:_} -> {highBoundA=:_}")

    for startingA in range(lowBoundA, highBoundA+1):
        AllGoodForNow = True
        A = startingA
        for i in range(len(program)):
            if (((A % 8) ^ 1) == 0) or ((((A%8) ^ 1) ^ (A // ((A%8) ^ 1))) ^ 4) % 8 != program[i]:
                valid = False
                break
            A = A // 8

        if valid:
            print(f"Lowest A value: {startingA}")
            break
    """