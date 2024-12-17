from math import trunc




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
            registers["A"] = trunc(registers["A"] / 2**get_combo(registers, operand))

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
            registers["B"] = trunc(registers["A"] / 2**get_combo(registers, operand))

        elif (opcode == 7):
            # A / combo -> C (truncated)
            registers["C"] = trunc(registers["A"] / 2**get_combo(registers, operand))

        if (programString and (outputString not in programString)):
            return outputString

        i += 2

    return outputString




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

    """
    # Bruteforce
    valueA = 91210000 if fichier == "input" else 0
    registers = {"A": -1, "B": 0, "C": 0}
    finalString = ""
    stringProgram = f"{','.join([str(nb) for nb in program])},"

    while (finalString != stringProgram):
        valueA += 1
        registers["A"] = valueA
        registers["B"] = 0
        registers["C"] = 0

        if (valueA % 10000 == 0): print(f"Value of register A: {valueA}...       ", end="\r")
        finalString = execute_program(registers, program, stringProgram)

    print(f"Value of register A: {valueA-1}   ")
    """