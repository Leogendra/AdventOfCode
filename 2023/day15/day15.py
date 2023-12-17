def get_hash_value(value):
    hash_value = 0
    for char in value:
        ascii_code = ord(char)
        hash_value += ascii_code
        hash_value *= 17
        hash_value %= 256

    return hash_value



for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day15/{fichier}.txt", "r") if line.strip() != ""]
    
    instructions = data[0].split(',')

    print("\033[93m--- Part One ---\033[0m")

    totalHash = 0
    for instruction in instructions:
        totalHash += get_hash_value(instruction)


    print(f"Valeur totale des hash: {totalHash}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    boites = {num: [] for num in range(256)}
    lentilles = {num: [] for num in range(256)}

    # Placement des lentilles
    for instruction in instructions:
        if '-' in instruction:
            label = instruction.split('-')[0]
            box = get_hash_value(label)
            if label in boites[box]:
                position = boites[box].index(label)
                boites[box].remove(label)
                lentilles[box].pop(position)
            
        if '=' in instruction:
            label, focal = instruction.split('=')
            box = get_hash_value(label)

            if label in boites[box]:
                position = boites[box].index(label)
                lentilles[box][position] = focal
            else:
                boites[box].append(label)
                lentilles[box].append(focal)

    focusPower = 0
    for box, lenses in lentilles.items():
        for i, focal in enumerate(lenses):
            focusPower += (box+1) * (i+1) * int(focal)

    print(f"Valeur totale des hash: {focusPower}")
    
    # break
