import heapq
from math import inf
import string


def dijsktra(tab, start):
    srcX, srcY = start
    ty = len(tab)
    tx = len(tab[0])
    letters = string.ascii_letters
    tabDist = [[inf]*tx for _ in range(ty)] # Tableau des distances
    queue = [(0,srcX,srcY)]
    while queue:
        cost, x, y = heapq.heappop(queue)
        if (tab[y][x] == "E"):
            return cost
        for v, w in [(-1,0),(1,0),(0,1),(0,-1)]:   # haut/bas/gauche/droite
            dx = x + v
            dy = y + w
            if (dx < 0) or (dy < 0) or (dx >= tx) or (dy >= ty) or ((tab[y][x] != "z") and (letters.index(tab[y][x]) < letters.index(tab[dy][dx]) - 1)):
                continue     # on évite de sortir du tableau
            coutActuel = cost + 1   # au augmente la distance de 1
            if tabDist[dy][dx] > coutActuel:
                tabDist[dy][dx] = coutActuel
                heapq.heappush(queue, (coutActuel,dx,dy))
    return inf



for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    carte = [line.strip() for line in open(f"2022/day12/{fichier}.txt", "r")]
    
    # find start
    start = [0, 0]
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if carte[i][j] == "S":
                start = [j, i]
                break

    cpt1 = dijsktra(carte, start)
    print(f"Part 1 : {cpt1} steps")

    
    # find all starts
    starts = []
    for i in range(len(carte)):
        for j in range(len(carte[i])):
            if (carte[i][j] == 'S') or (carte[i][j] == 'a'):
                starts.append([j, i])


    cpt2 = inf
    for start in starts:
        cpt2 = min(cpt2, dijsktra(carte, start))

    print(f"Part 2 : {cpt2} steps")
    if cpt2 != 29:
        break



