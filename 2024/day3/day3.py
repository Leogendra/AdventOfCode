import re




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day3/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    pattern = r"mul\([0-9]*,[0-9]*\)"

    cpt = 0
    for line in data:
        matches = re.findall(pattern, line)
        for match in matches:
            a, b = match.split("(")[1].split(")")[0].split(",")
            cpt += int(a) * int(b)

    print(cpt)



    
    print("\n\033[93m--- Part Two ---\033[0m")

    cpt = 0
    activated = True
    for line in data:
        matches_items = [match.group() for match in re.finditer(pattern, line)]
        matches_ids = [match.start() for match in re.finditer(pattern, line)]
        do_ids = [match.start() for match in re.finditer(r"do\(\)", line)]
        dont_ids = [match.start() for match in re.finditer(r"don't\(\)", line)]

        i, j = 0, 0
        while i < len(line):
            if (i in do_ids):
                activated = True
                i += 4
            elif (i in dont_ids):
                activated = False
                i += 7
            elif (i in matches_ids):
                if (activated):
                    a, b = matches_items[j].split("(")[1].split(")")[0].split(",")
                    cpt += int(a) * int(b)
                j += 1
                i += 7
            else:
                i += 1
            
        
    print(cpt)