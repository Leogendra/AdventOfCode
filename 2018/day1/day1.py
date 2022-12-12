for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    input = [line.split(",")[0].strip() for line in open(f"2018/day1/{fichier}.txt", "r")]
    cpt = 0
    for freq in input:
        if freq[0] == "+":
            cpt += int(freq[1:])
        else:
            cpt -= int(freq[1:])
   
    print(f"Part 1 : {cpt}")

    cpt = 0   
    freqs = [0]
    found = False
    while not(found):
        for freq in input:
            if freq[0] == "+":
                cpt += int(freq[1:])
            else:
                cpt -= int(freq[1:])
            if cpt in freqs:
                found = True
                break
            freqs.append(cpt)
        
    print(f"Part 2 : {cpt}")