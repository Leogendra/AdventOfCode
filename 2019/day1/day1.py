for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    input = [int(line.strip()) for line in open(f"2019/day1/{fichier}.txt", "r")]
    cpt = 0
   
    print(f"Part 1 : {sum([x//3-2 for x in input])}")

    cpt = 0
    for x in input:
        while x > 0:
            x = x//3-2
            if x > 0:
                cpt += x
        
    print(f"Part 2 : {cpt}")