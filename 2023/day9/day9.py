def calculer_suivant(donnes):
    somme = 0
    for line in donnes:

        lignes_derivees = [line]
        valeurs_derivees = line

        while any(val != 0 for val in valeurs_derivees):
            valeurs_derivees = []
            # calculer la différence entre chaque terme
            for i in range(len(lignes_derivees[-1])-1):
                valeurs_derivees.append(lignes_derivees[-1][i+1] - lignes_derivees[-1][i])
            lignes_derivees.append(valeurs_derivees)

        # rajouter un 0
        lignes_derivees[-1].append(0)

        # remonter en calculant la nouvelle différence
        for i in range(len(lignes_derivees)-1, 0, -1):
            lignes_derivees[i-1].append(lignes_derivees[i-1][-1] + lignes_derivees[i][-1])
            
        # retourner la valeur ajoutée à la première liste
        somme += lignes_derivees[0][-1]
    
    return somme


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [list(map(int, line.strip().split())) for line in open(f"2023/day9/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    
    print(f"Somme {calculer_suivant(data)}")


    print("\n\033[93m--- Part Two ---\033[0m")    
    

    reversed_data = [line[::-1] for line in data]

    print(f"Somme {calculer_suivant(reversed_data)}")