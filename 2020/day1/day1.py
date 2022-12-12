for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    input = [int(line.strip()) for line in open(f"2020/day1/{fichier}.txt", "r")]
    cpt = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if input[i] + input[j] == 2020:
                cpt = input[i] * input[j]
                break
        if cpt != 0:
            break

   
    print(f"Part 1 : {cpt}")

    cpt = 0
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            for k in range(j+1, len(input)):
                if input[i] + input[j] + input[k] == 2020:
                    cpt = input[i] * input[j] * input[k]
                    break
            if cpt != 0:
                break
        if cpt != 0:
            break
        
    print(f"Part 2 : {cpt}")