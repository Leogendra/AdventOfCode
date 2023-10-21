for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    jumps = [int(line.strip()) for line in open(f"2017/day5/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")
    
    tailleListe = len(jumps)
    position = 0
    etapes = 0

    while (position >= 0) and (position < tailleListe):
        jump = jumps[position]
        jumps[position] += 1
        
        position += jump
        etapes += 1

    print(etapes)


    print("\n\033[93m--- Part Two ---\033[0m")

    jumps = [int(line.strip()) for line in open(f"2017/day5/{fichier}.txt", "r")]
    position = 0
    etapes = 0

    while (position >= 0) and (position < tailleListe):
        jump = jumps[position]
        if jump > 2:
            jumps[position] -= 1
        else:
            jumps[position] += 1
        
        position += jump
        etapes += 1

    print(etapes)