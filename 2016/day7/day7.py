for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2016/day7/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    validIps = 0

    for line in data:
        valid = False
        brackets = False
        pile = []
        for i in range(len(line)):
            char = line[i]

            if (char == "["):
                brackets = True
                pile = []

            elif (char == "]"):
                brackets = False
                pile = []

            else:
                pile.append(char)
                if (len(pile) > 3) and (pile[-1] == pile[-4]) and (pile[-2] == pile[-3]) and (pile[-1] != pile[-2]):
                    if brackets:
                        valid = False
                        break
                    else:
                        valid = True
        
        if valid:
            validIps += 1

    print(f"Nombre d'IPs valides : {validIps}")




    print("\n\033[93m--- Part Two ---\033[0m")

    validIps = 0

    for line in data:
        brackets = False
        pile = []
        pileOutside = []
        pileInside = []
        for i in range(len(line)):
            char = line[i]

            if (char == "["):
                brackets = True
                pile = []

            elif (char == "]"):
                brackets = False
                pile = []

            else:
                pile.append(char)
                if (len(pile) > 2) and (pile[-1] == pile[-3]) and (pile[-1] != pile[-2]):
                    if brackets:
                        pileInside.append(''.join(pile[-3:]))
                    else:
                        pileOutside.append(''.join(pile[-3:]))

                        
        for aba in pileOutside:
            bab = f"{aba[1]}{aba[0]}{aba[1]}"
            if bab in pileInside:
                validIps += 1
                break


    print(f"Nombre d'IPs valides : {validIps}")
