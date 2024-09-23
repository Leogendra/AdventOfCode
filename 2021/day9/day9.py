import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *


input = ouvre_txt("2021/day9/test")

# renvoie tous les voisins du point [i,j]
def voisins(i, j, mi, mj):
    V = []
    if i != 0:
        V.append([i - 1, j])
    if j != 0:
        V.append([i, j - 1])
    if i != mi:
        V.append([i + 1, j])
    if j != mj:
        V.append([i, j + 1])
    return V


# return True si le ptn [i,j] est le plus petit de ses voisins
def est_plus_petit(i, j, mi, mj):
    vois = voisins(i, j, mi, mj)
    for v in vois:
        if input[v[1]][v[0]] <= input[j][i]:
            return False
    return True


# calcul des minimum locaux
min_locaux = []
max_i = len(input[0])
max_j = len(input)
for j in range(max_j):
    for i in range(max_i):
        if est_plus_petit(i, j, max_i - 1, max_j - 1):
            min_locaux.append([i, j])

# calcul des niveaux de risques
cpt = 0
for p in min_locaux:
    cpt += int(input[p[1]][p[0]]) + 1

print("niveau de risque =", cpt)


# Partie 2 ***************************


def couvre_voisins(pt, b):
    x = pt[0]
    y = pt[1]
    # print("i=",b,",point:",pt,", input:",input[y][x],", data:",data9[y][x])
    if (input[y][x] != "9") and (data9[y][x] == 0):
        data9[y][x] = b
        vois = voisins(x, y, max_i - 1, max_j - 1)
        for v in vois:
            couvre_voisins(v, b)


# on créer une map avec que des 0
data9 = []
for i in range(max_j):
    data9.append([0 for i in range(max_i)])

# on créer la base des bassins aux minimum locaux
for i in range(len(min_locaux)):
    data9[min_locaux[i][1]][min_locaux[i][0]] = i + 1


# fonction pour calculer les bassins
for i in range(len(min_locaux)):
    x = min_locaux[i][0]
    y = min_locaux[i][1]
    vois = voisins(x, y, max_i - 1, max_j - 1)
    for v in vois:
        couvre_voisins(v, i + 1)


# compter la taille des bassins
b1 = 0
b2 = 0
b3 = 0
for i in range(len(min_locaux)):
    cpt = 0
    for ligne in data9:
        for pt in ligne:
            if (i + 1) == pt:
                cpt += 1
    if cpt > b1:
        b3 = b2
        b2 = b1
        b1 = cpt
    elif cpt > b2:
        b3 = b2
        b2 = cpt
    elif cpt > b3:
        b3 = cpt


print("Bassin 1 :", b1)
print("Bassin 2 :", b2)
print("Bassin 3 :", b3)
print("B1*B2*B3 :", b3 * b2 * b1)