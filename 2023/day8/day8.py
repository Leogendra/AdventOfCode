import math

for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day8/{fichier}.txt", "r") if line.strip() != ""]

    ordre = data[0]
    mapping = {}
    for line in data[1:]:
        _key, _equal, _left, _right = line.split()
        _left = _left.strip("(,)")
        _right = _right.strip("(,)")
        mapping[_key] = {"L": _left, "R": _right}

    print("\033[93m--- Part One ---\033[0m")

    iterations = 0
    current = 'AAA'

    while current != 'ZZZ':
        current = mapping[current][ordre[iterations % len(ordre)]]
        iterations += 1


    print(f"Nombre d'itérations : {iterations}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    currents = [node for node in mapping.keys() if node[-1] == 'A']
    currents.sort()

    iterations = []
    for current in currents:
        i = 0
        while current[-1] != 'Z':
            current = mapping[current][ordre[i % len(ordre)]]
            i += 1
        iterations.append(i)

    print(f"Nombre d'itérations : {math.lcm(*iterations)}")

