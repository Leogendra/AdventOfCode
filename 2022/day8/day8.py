for fichier in ["test", "input"]:
    # PARSING
    print(f"\nFICHIER {fichier}.txt")
    foret = [line.strip() for line in open(f"2022/day8/{fichier}.txt", "r")]
    x_max = len(foret[0])
    y_max = len(foret)

    # PART 1
    cpt1 = 0
    for i in range(x_max):
        for j in range(y_max):
            valArbre = int(foret[j][i])
            for a, b in [[1,0],[0,1],[-1,0],[0,-1]]:
                x, y = 1, 1
                voir = True
                while (i+x*a < x_max) and (i+x*a >= 0) and (j+y*b < y_max) and (j+y*b >= 0):
                    if valArbre <= int(foret[j+y*b][i+x*a]):
                        voir = False
                        break
                    x += 1
                    y += 1
                if voir:
                    cpt1 += 1
                    break


    print("* Part 1 :",cpt1)

    # PART 2
    max_score = 0
    for i in range(x_max):
        for j in range(y_max):
            scoreArbre = 1
            valArbre = int(foret[j][i])
            for a, b in [[1,0],[0,1],[-1,0],[0,-1]]:
                x, y = 1, 1
                voisinVus = 1
                while (i+x*a < x_max-1) and (i+x*a > 0) and (j+y*b < y_max-1) and (j+y*b > 0) and (valArbre > int(foret[j+y*b][i+x*a])):
                        voisinVus += 1
                        x += 1
                        y += 1
                scoreArbre *= voisinVus
            if scoreArbre > max_score:
                max_score = scoreArbre

    print("* Part 2 :",max_score) # O(4*n^3) lol