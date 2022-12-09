def visual(q,v,dir):
    x = 14
    y = 15
    grille = [["." for _ in range(1+2*x)] for _ in range(1+2*y)]
    grille[y][x] = "s"
    print("\n",dir)
    for i in range(len(q)):
        pos = q[i]
        print(i,pos)
        if grille[y+pos[1]][x+pos[0]] == ".":
            grille[y+pos[1]][x+pos[0]] = str(i)
    for vis in v:
        if grille[y+vis[1]][x+vis[0]] == ".":
            grille[y+vis[1]][x+vis[0]] = "#"
    
    for line in grille:
        print("".join(line))
    



for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    cmd = [line.strip().split() for line in open(f"2022/day9/{fichier}.txt", "r")]

    T = [0,0] # tete
    Q = [0,0] # queue
    visitesQueue = [[0,0]]

    for dir, n in cmd: # U:haut, D:bas, R:droite, L:gauche
        n = int(n)
        if dir == "U":
            T[1] -= n
        elif dir == "D":
            T[1] += n
        elif dir == "R":
            T[0] += n
        elif dir == "L":
            T[0] -= n

        while (abs(T[0]-Q[0]) > 1) or (abs(T[1]-Q[1]) > 1): # si non adjacents
            if dir == "U":
                if T[0]-Q[0] > 0:
                    Q[0] += 1
                if Q[0]-T[0] > 0:
                    Q[0] -= 1
                Q[1] -= 1
            elif dir == "D":
                if T[0]-Q[0] > 0:
                    Q[0] += 1
                if Q[0]-T[0] > 0:
                    Q[0] -= 1
                Q[1] += 1
            elif dir == "R":
                if T[1]-Q[1] > 0:
                    Q[1] += 1
                if Q[1]-T[1] > 0:
                    Q[1] -= 1
                Q[0] += 1
            elif dir == "L":
                if T[1]-Q[1] > 0:
                    Q[1] += 1
                if Q[1]-T[1] > 0:
                    Q[1] -= 1
                Q[0] -= 1
            visitesQueue.append([Q[0],Q[1]])

    print("Part 1 :",len(set(tuple(i) for i in visitesQueue)))


    
    Q = [[0,0] for _ in range(10)] # queue
    T = Q[0]
    visitesQueue9 = [[0,0]]

    for dir, n in cmd: # U:haut, D:bas, R:droite, L:gauche
        for i in range(int(n)): # mouvements un par 1
            if dir == "U":
                T[1] -= 1
            elif dir == "D":
                T[1] += 1
            elif dir == "R":
                T[0] += 1
            elif dir == "L":
                T[0] -= 1

            for j in range(1,10): # on bouge toutes les cordes 1 par 1
                if (abs(Q[j][0]-Q[j-1][0]) > 1) or (abs(Q[j][1]-Q[j-1][1]) > 1):
                    if Q[j][0]-Q[j-1][0] > 0:
                        Q[j][0] -= 1
                    elif Q[j-1][0]-Q[j][0] > 0:
                        Q[j][0] += 1
                    if Q[j][1]-Q[j-1][1] > 0:
                        Q[j][1] -= 1
                    elif Q[j-1][1]-Q[j][1] > 0:
                        Q[j][1] += 1
            visitesQueue9.append([Q[9][0],Q[9][1]])
            if fichier == "test": visual(Q,visitesQueue9,dir)#print(visitesQueue9)
    
    print("Part 2 :",len(set(tuple(t) for t in visitesQueue9)))