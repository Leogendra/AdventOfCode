print('\n\n')
for fichier in ["input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    input = [line.strip() for line in open(f"2019/day4/{fichier}.txt", "r")]
    
    minValue, maxValue = list(map(int, input[0].split("-")))
    print(minValue, maxValue)

    print("\033[93m--- Part One ---\033[0m")

    numberOfValidCodes = 0

    for code in range(minValue, maxValue+1):
        double = False
        decroissant = False
        codeStr = str(code)
        for i in range(5):
            if codeStr[i] > codeStr[i+1]: 
                decroissant = True
                break
            if codeStr[i] == codeStr[i+1]:
                double = True

        numberOfValidCodes += (double and not(decroissant))

    print(f"Nombre de codes valides : {numberOfValidCodes}")



    print("\n\033[93m--- Part Two ---\033[0m")

    numberOfValidCodes = 0

    for code in range(minValue, maxValue+1):
        double = False
        decroissant = False
        codeStr = str(code)
        for i in range(5):
            if codeStr[i] > codeStr[i+1]: 
                decroissant = True
                break
            if (codeStr[i] == codeStr[i+1]) and (codeStr.count(codeStr[i]) == 2):
                double = True

        numberOfValidCodes += (double and not(decroissant))

    print(f"Nombre de codes valides : {numberOfValidCodes}")