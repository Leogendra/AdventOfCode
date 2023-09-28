for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    input = [line.strip() for line in open(f"2017/day2/{fichier}.txt", "r")]

    print("--- Part One ---")

    data = []
    for line in input:
        data.append([int(num) for num in line.split('\t')])

    checksum = 0
    for line in data:
        max_value = max(line)
        min_value = min(line)
        checksum += int(max_value) - int(min_value)
    
    print(checksum)

    print("\n--- Part Two ---")

    checksum = 0
    for line in data:
        found = False
        for numA in line:
            for numB in line:
                if (numA != numB) and (numA % numB == 0):
                    checksum += numA // numB
                    found = True
                    break
            if found:
                break
    
    print(checksum)

    
    # break