def retourner_90(pattern):
    transposed_pattern = [''.join(row)[::-1] for row in zip(*pattern)]
    return transposed_pattern


def trouve_reflexion(pattern, already=0):
    for reflexion in range(1, len(pattern)):
        reflette = True  
        i = 0
        while (reflexion-(i+1) >= 0) and (reflexion + i < len(pattern)):
            # check si le pattern est le même avant et après la réflexion
            if pattern[reflexion-(i+1)] != pattern[reflexion + i]:
                reflette = False
            i += 1

        if reflette and (already != reflexion):
            return reflexion
        
    return 0


def add_smudge(pattern, tache):

    nouvelle_liste = [ligne[:] for ligne in pattern]  # Crée une copie de la liste d'origine

    i, j = divmod(tache, len(pattern[0]))
    ligne_modifiee = list(nouvelle_liste[i])
    ligne_modifiee[j] = "#" if ligne_modifiee[j] == "." else "."
    nouvelle_liste[i] = ''.join(ligne_modifiee)

    return nouvelle_liste



for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day13/{fichier}.txt", "r")]

    patterns = []
    pattern = []
    for line in data:
        if line.strip() == "":
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)

    print("\033[93m--- Part One ---\033[0m")

    sommeReflets = 0
    i = 0
    for pattern in patterns:
        # print(f"\n\033[93mPattern {i}\033[0m")
        i += 1

        # réflexions horizontalles
        valeurReflet = trouve_reflexion(pattern) * 100

        # réflexions verticales
        if valeurReflet == 0:
            pattern_turned = retourner_90(pattern)
            valeurReflet = trouve_reflexion(pattern_turned)

        sommeReflets += valeurReflet


    print(f"Somme des reflets : {sommeReflets}")
    




    print("\n\033[93m--- Part Two ---\033[0m")

    sommeReflets = 0
    i = 0
    for pattern in patterns:
        i += 1

        # réflexions horizontalles
        horizontal = True
        valeurReflet = trouve_reflexion(pattern)

        # réflexions verticales
        if valeurReflet == 0:
            pattern_turned = retourner_90(pattern)
            valeurReflet = trouve_reflexion(pattern_turned)
            horizontal = False

        # On a trouvé le reflet, on modifie le pattern pour trouver un nouveau reflet
        tache = 0
        nouvelleValeurReflet = 0
        while (nouvelleValeurReflet == 0) or ((horizontal == newHorizontal) and (nouvelleValeurReflet == valeurReflet)):
            pattern_smudged = add_smudge(pattern, tache)
            tache += 1

            newHorizontal = True

            if horizontal:
                # on commence par le vertical
                pattern_smudged_turned = retourner_90(pattern_smudged)
                nouvelleValeurReflet = trouve_reflexion(pattern_smudged_turned)
                newHorizontal = False

                if nouvelleValeurReflet == 0:
                    newHorizontal = True
                    nouvelleValeurReflet = trouve_reflexion(pattern_smudged, valeurReflet) * 100

            else:
                nouvelleValeurReflet = trouve_reflexion(pattern_smudged) * 100

                if nouvelleValeurReflet == 0:
                    newHorizontal = False
                    pattern_smudged_turned = retourner_90(pattern_smudged)
                    nouvelleValeurReflet = trouve_reflexion(pattern_smudged_turned, valeurReflet)


        sommeReflets += nouvelleValeurReflet
    
    print(f"Somme des nouveaux reflets : {sommeReflets}")