for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day7/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")
    
    nbCalibration = 0
    for line in data:
        numbers = [int(nb) for nb in line.replace(":", "").split()]
        result = numbers[0]
        numbers = numbers[1:]

        signs = 0
        signsNumber = len(numbers)-1
        calculated = -1
        while (signs < (2**signsNumber)) and (calculated != result):
            calculated = numbers[0]
            signs_tab = [(signs >> bit) & (1 == 1) for bit in range(signsNumber)]
            for i in range(signsNumber):
                if signs_tab[i]:
                    calculated += numbers[i+1]
                else:
                    calculated *= numbers[i+1]

            signs += 1
            
        if (calculated == result):
            nbCalibration += calculated

    print(f"total calibration result: {nbCalibration}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    nbCalibration = 0
    for line in data:
        numbers = [int(nb) for nb in line.replace(":", "").split()]
        result = numbers[0]
        numbers = numbers[1:]

        signsNumber = len(numbers)-1
        signs_tab = [0 for _ in range(signsNumber)]
        calculated = -1
        while (calculated != result):
            calculated = numbers[0]
            for i in range(signsNumber):
                if (signs_tab[i] == 0):
                    calculated += numbers[i+1]
                elif (signs_tab[i] == 1):
                    calculated *= numbers[i+1]
                else:
                    calculated = int(f"{calculated}{numbers[i+1]}")

            if not(0 in signs_tab) and not(1 in signs_tab): # end of an array
                break
            for i in range(signsNumber):
                signs_tab[i] = (signs_tab[i] + 1) % 3
                if signs_tab[i] != 0:
                    break
            
        if (calculated == result):
            nbCalibration += calculated

    print(f"total calibration result: {nbCalibration}")