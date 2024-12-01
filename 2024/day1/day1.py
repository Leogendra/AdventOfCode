for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day1/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    liste1, liste2 = [], []
    for line in data:
        nbrs = [int(nbr.strip()) for nbr in line.split()]
        liste1.append(nbrs[0])
        liste2.append(nbrs[1])

    cpt = 0
    while len(liste1) > 0:
        cpt += abs(min(liste1) - min(liste2))
        liste1.pop(liste1.index(min(liste1)))
        liste2.pop(liste2.index(min(liste2)))

    print(cpt)
    
    print("\n\033[93m--- Part Two ---\033[0m")

    
    liste1, liste2 = [], []
    for line in data:
        nbrs = [int(nbr.strip()) for nbr in line.split()]
        liste1.append(nbrs[0])
        liste2.append(nbrs[1])

    cpt = 0
    for nbr in liste1:
        cpt += nbr * liste2.count(nbr)

    print(cpt)
    

