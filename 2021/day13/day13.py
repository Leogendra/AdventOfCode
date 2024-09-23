import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *


input = ouvre_txt("2021/day13/input")
for i in range(len(input)):
    input[i] = input[i].split(",")


def plier(feuille, instr, mx, my):
    sens = instr[0]
    coord = int(instr[1])
    new_feuille = []
    new_x = mx
    new_y = my
    # pliage vers le haut
    if sens == "y":
        new_y = coord - 1
        for i in range(new_y + 1):
            new_feuille.append(feuille[i])
            for j in range(mx + 1):
                if feuille[my - i][j] == "#":
                    new_feuille[i][j] = "#"
    # pliage vers la gauche
    if sens == "x":
        new_x = coord - 1
        for i in range(my + 1):
            tmp = [feuille[i][j] for j in range(new_x + 1)]
            for j in range(new_x + 1):
                if feuille[i][new_x + 2 + j] == "#":
                    tmp[new_x - j] = "#"
            new_feuille.append(tmp)

    return [new_feuille, new_x, new_y]


def aff_feuille(g, x, y):
    for i in range(y + 1):
        for j in range(x + 1):
            if g[i][j] == "#":
                print("#", end="")
            else:
                print(" ", end="")
        print("")
    print("")


points = []
pliages = []
switch = False
max_x = 0
max_y = 0

for ligne in input:
    if ligne == [""]:
        switch = True
    elif switch:
        pliages.append([ligne[0].split("=")[0][-1], ligne[0].split("=")[-1]])
    else:
        x = int(ligne[0])
        y = int(ligne[1])
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        points.append([x, y])

# remplis une grille vide
grille = []
for i in range(max_y + 1):
    grille.append(["." for j in range(max_x + 1)])


# placement des points
for pt in points:
    grille[pt[1]][pt[0]] = "#"

infos_nouvelle_grille = plier(grille, pliages[0], max_x, max_y)
nouvelle_grille = infos_nouvelle_grille[0]
new_max_x = infos_nouvelle_grille[1]
new_max_y = infos_nouvelle_grille[2]

# comptage des points
cpt = 0
for i in range(new_max_y + 1):
    for j in range(new_max_x + 1):
        if nouvelle_grille[i][j] == "#":
            cpt += 1


print("points après 1 pliage :", cpt)


inputl = ouvre_txt("2021/day13/input")


def second_star():
    inputm = [x.split(",") for x in inputl if len(x.split(",")) == 2]
    d = set()
    for x in inputm:
        d.add((int(x[0]), int(x[1])))
    instr = []
    for x in inputl:
        y = x.split(" ")
        if len(y) == 3:
            z = y[2].split("=")
            instr.append((z[0], int(z[1])))
    for inst in instr:
        if inst[0] == "x":
            e = set()
            for x, y in d:
                if x < inst[1]:
                    e.add((x, y))
                elif x > inst[1]:
                    e.add((2 * inst[1] - x, y))
            d = e
        elif inst[0] == "y":
            e = set()
            for x, y in d:
                if y < inst[1]:
                    e.add((x, y))
                elif y > inst[1]:
                    e.add((x, 2 * inst[1] - y))
            d = e

    for i in range(6):
        st = ""
        for j in range(40):
            if (j, i) in d:
                st += "#"
            else:
                st += " "
        print(st)


print("après tous les pliage :")
second_star()