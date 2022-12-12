for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    input = [line.strip() for line in open(f"2017/day1/{fichier}.txt", "r")][0]
    cpt = 0
    for i in range(1,len(input)):
        if input[i] == input[(i-1)]:
            cpt += int(input[i])
    if input[0] == input[-1]:
        cpt += int(input[0])
   
    print(f"Part 1 : {cpt}")

    cpt = 0
    for i in range(len(input)):
        if input[i] == input[(i+len(input)//2)%len(input)]:
            cpt += int(input[i])
        
    print(f"Part 2 : {cpt}")