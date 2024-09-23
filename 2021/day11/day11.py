import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *


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



input = []
data11 = ouvre_txt("2021/day11/test")
for i in range(10):
    input.append([int(data11[i][j]) for j in range(10)])

partie_2 = input.copy()


def voisin_diag(pt, max_x, max_y):
    x = pt[0]
    y = pt[1]
    vois = voisins(x, y, max_x, max_y)
    if x != 0:
        if y != 0:
            vois.append([x - 1, y - 1])
        if y != max_y:
            vois.append([x - 1, y + 1])
    if x != max_x:
        if y != 0:
            vois.append([x + 1, y - 1])
        if y != max_y:
            vois.append([x + 1, y + 1])
    return vois


def octoplus(oc):
    global cpt, input
    x = oc[0]
    y = oc[1]
    if input[y][x] != 0:
        input[y][x] += 1
        if input[y][x] > 9:
            cpt += 1
            input[y][x] = 0
            vois = voisin_diag(oc, 9, 9)
            for v in vois:
                octoplus(v)


cpt = 0
for caca in range(100):
    # incrément des poulpes
    for j in range(10):
        for i in range(10):
            input[j][i] += 1
    # check des luminéscences
    for j in range(10):
        for i in range(10):
            if input[j][i] > 9:
                octoplus([i, j])


print("nombre de flashs :", cpt)


# reset de l'input
input = []
for i in range(10):
    input.append([int(data11[i][j]) for j in range(10)])

jours = 0
all_flash = False
while not (all_flash):
    jours += 1
    # incrément des poulpes
    for j in range(10):
        for i in range(10):
            input[j][i] += 1

    # check des luminéscences
    for j in range(10):
        for i in range(10):
            if input[j][i] > 9:
                octoplus([i, j])

    # check si tous les poulpes ont slashés en même temps
    all_flash = True
    for j in range(10):
        for i in range(10):
            if input[j][i] != 0:
                all_flash = False


print("tous flashés : étape", jours)