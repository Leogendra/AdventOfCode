for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    carte = [line.strip() for line in open(f"2015/day1/{fichier}.txt", "r")]
    cpt1 = 0
    for c in carte[0]:
        if c == "(":
            cpt1 += 1
        if c == ")":
            cpt1 -= 1
   
    print(f"Part 1 : {cpt1} steps")


    cpt2 = 0
    for i in range(len(carte[0])):
        c = carte[0][i]
        if cpt2 == -1:
            print(f"Part 2 : {i}-ième char")
            break
        if c == "(":
            cpt2 += 1
        if c == ")":
            cpt2 -= 1