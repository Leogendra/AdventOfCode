for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    input = [line.strip() for line in open(f"2018/day2/{fichier}.txt", "r")]

    print("--- Part One ---")

    two = 0
    three = 0

    for line in input:
        chars = {}
        for char in line:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        if 2 in chars.values():
            two += 1
        if 3 in chars.values():
            three += 1

    checksum = two * three    
    print(checksum)

    print("\n--- Part Two ---")

    for line1 in input:
        for line2 in input:
            if line1 == line2:
                continue
            diff = False
            for i in range(len(line1)):
                if line1[i] != line2[i]:
                    if diff:
                        diff = False
                        break
                    else:
                        diff = True
            if diff:
                print("".join([line1[i] for i in range(len(line1)) if line1[i] == line2[i]]))
                break
        if diff:
            break
    
    # break