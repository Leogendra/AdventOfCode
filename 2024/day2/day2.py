def is_safe(levels):
    if levels[0] == levels[1]:
        return False
    
    increase = levels[0] < levels[1]
    for i in range(1, len(levels)):
        if (levels[i-1] == levels[i]) or ((levels[i-1] < levels[i]) != increase) or (abs(levels[i-1] - levels[i]) > 3):
            return False
        
    return True



for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day2/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    cpt = 0
    for line in data:
        levels = [int(level) for level in line.split()]
        if is_safe(levels):
            cpt += 1

    print(cpt)
                    

    

    print("\n\033[93m--- Part Two ---\033[0m")
    
    cpt = 0
    for line in data:
        levels = [int(level) for level in line.split()]
       
        if is_safe(levels):
            cpt += 1

        else:
            safe = False
            for i in range(len(levels)):
                new_levels = [levels[j] for j in range(len(levels)) if j != i]
                if is_safe(new_levels):
                    safe = True
                    break

            if safe:
                cpt += 1

    print(cpt)