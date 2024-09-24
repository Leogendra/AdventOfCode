def get_prog_value(prog):
    progValue = programs[prog]
    for progOver, progUnder in isOver.items():
        if progUnder == prog:
            progValue += get_prog_value(progOver)
    return progValue




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2017/day7/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    programs = {}
    isOver = {}
    for line in data:
        infos = line.split(" -> ")
        if (len(infos) > 1):
            mainProgram, areOver = infos
            programName, programValue = mainProgram.split(" ")
            programs[programName.strip()] = int(programValue.strip(" ()"))
            for prog in areOver.split(", "):
                isOver[prog.strip()] = programName.strip()
        else:
            programName, programValue = infos[0].split(" ")
            programs[programName.strip()] = int(programValue.strip(" ()"))


    bottomProgram = [prog for prog in programs.keys() if (prog not in isOver.keys())][0]
    print(f"Bottom program: {bottomProgram}")

    


    print("\n\033[93m--- Part Two ---\033[0m")

    charges = {}
    for prog in programs.keys():
        charges[prog] = get_prog_value(prog)

    balancedWeight = 0
    ecart = 0
    found = False
    while not(found):
        weights = {}

        for progOver, progUnder in isOver.items():
            if progUnder == bottomProgram:
                weights[progOver] = charges[progOver]

        weightsValues = [value for _, value in weights.items()]
        minValue = min(weightsValues, key=weightsValues.count)
        maxValue = max(weightsValues, key=weightsValues.count)
        if minValue != maxValue:
            for progName, progValue in weights.items():
                if progValue == minValue:
                    bottomProgram = progName
                    ecart = maxValue - minValue
                    break
        else:
            balancedWeight = programs[bottomProgram] + ecart
            found = True
            
    print(f"Program balanced weight: {balancedWeight}")

