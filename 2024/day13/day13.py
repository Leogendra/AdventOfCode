def is_int(x):
    return (x == int(x))





for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day13/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    machines_list = []
    current_machine = []
    for line in data:
        if line.startswith("Button"):
            _button, _, xPlus, yPlus = line.split(" ")
            xPlus = xPlus.strip(" X+,")
            yPlus = yPlus.strip(" Y+,")
            current_machine.append((int(xPlus), int(yPlus)))
        if line.startswith("Prize"):
            _prize, xPlus, yPlus = line.split(" ")
            xPlus = xPlus.strip(" X=,")
            yPlus = yPlus.strip(" Y=,")
            current_machine.append((int(xPlus), int(yPlus)))
            machines_list.append(current_machine)
            current_machine = []


    priceA, priceB = 3, 1
    
    tokenUsed = 0
    for [(a1, a2), (b1, b2), (p1, p2)] in machines_list:
        determinant = a1*b2 - a2*b1
        
        if (determinant == 0):
            continue
        
        tokensA = (p1*b2 - p2*b1) // determinant
        tokensB = (a1*p2 - a2*p1) // determinant
        
        if (a1*tokensA + b1*tokensB, a2*tokensA + b2*tokensB) == (p1, p2):
            if (tokensA <= 100) and (tokensB <= 100):
                tokenUsed += priceA*tokensA + priceB*tokensB


    print(f"Total tokens used : {tokenUsed}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    tokenUsed = 0
    for [(a1, a2), (b1, b2), (p1, p2)] in machines_list:
        p1, p2 = p1+10000000000000, p2+10000000000000

        determinant = a1*b2 - a2*b1
        
        if (determinant == 0):
            continue
        
        tokensA = (p1*b2 - p2*b1) // determinant
        tokensB = (a1*p2 - a2*p1) // determinant
        
        if (a1*tokensA + b1*tokensB, a2*tokensA + b2*tokensB) == (p1, p2):
            tokenUsed += priceA*tokensA + priceB*tokensB


    print(f"Total tokens used : {tokenUsed}")