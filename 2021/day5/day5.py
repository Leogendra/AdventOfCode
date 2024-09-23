import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *
input = ouvre_txt("2021/day5/test.txt")


def txt_to_coord(T):
    T2 = [x.split(" -> ") for x in T]
    C = []
    for x in T2:
        x1 = int(x[0].split(",")[0])
        y1 = int(x[0].split(",")[1])
        x2 = int(x[1].split(",")[0])
        y2 = int(x[1].split(",")[1])
        C.append([x1, y1, x2, y2])
    return C


data5 = txt_to_coord(input)
# print_tab(data5)

max_value_x = 0
max_value_y = 0
for i in range(len(data5)):
    for j in range(4):
        if j % 2 == 0:
            max_value_x = max(max_value_x, data5[i][j])
        else:
            max_value_y = max(max_value_y, data5[i][j])

max_value_x += 1
max_value_y += 1

hydro = [[0 for i in range(max_value_x)] for j in range(max_value_y)]

cpt = 0
# parcourt des coordonées
for pos in data5:
    cpt += 1
    x1 = pos[0]
    y1 = pos[1]
    x2 = pos[2]
    y2 = pos[3]
    if (x1 == x2) or (y1 == y2):
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                hydro[i][x1] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2 + 1):
                hydro[y1][i] += 1


chevauchements = 0
for i in range(max_value_y):
    for j in range(max_value_x):
        if hydro[i][j] > 1:
            chevauchements += 1

print("chevauchements linéaires :", chevauchements)


# Partie 2 ****************************************

hydro = [[0 for i in range(max_value_x)] for j in range(max_value_y)]
cpt = 0
# parcourt des coordonées
for pos in data5:
    cpt += 1
    x1 = pos[0]
    y1 = pos[1]
    x2 = pos[2]
    y2 = pos[3]
    if (x1 == x2) or (y1 == y2):
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2 + 1):
                hydro[i][x1] += 1
        else:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2 + 1):
                hydro[y1][i] += 1
    else:
        if x1 < x2:
            if y1 < y2:
                for i in range(x1, x2 + 1):
                    hydro[y1][i] += 1
                    y1 += 1
            else:
                for i in range(x1, x2 + 1):
                    hydro[y1][i] += 1
                    y1 -= 1
        else:
            if y1 < y2:
                for i in range(x2, x1 + 1):
                    hydro[y2][i] += 1
                    y2 -= 1
            else:
                for i in range(x2, x1 + 1):
                    hydro[y2][i] += 1
                    y2 += 1



chevauchements = 0
for i in range(max_value_y):
    for j in range(max_value_x):
        if hydro[i][j] > 1:
            chevauchements += 1


print("chevauchements + diagonales :", chevauchements)