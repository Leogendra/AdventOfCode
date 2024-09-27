for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2017/day8/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    highest = 0
    registers = {}
    for line in data:
        register1, operation, value1, _if, register2, signe, value2 = line.split()
        condition = eval(f"{registers.get(register2, 0)}{signe}{value2}")
        if condition:
            if operation == "inc":
                registers[register1] = registers.get(register1, 0) + int(value1)

            elif operation == "dec":
                registers[register1] = registers.get(register1, 0) - int(value1)

            highest = max(highest, registers[register1])


    print(f"Max value in registers: {max(val for _, val in registers.items())}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    print(f"Highest value in registers: {highest}")
    

