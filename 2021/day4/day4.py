import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *
input = ouvre_txt("2021/day4/test.txt")

tirage = to_int(input[0].split(","))
# print(tirage)


def aff_grille(G):
    for i in range(5):
        for j in range(5):
            num = G[i][j]
            if j != 0:
                print(" ", end="")
            if num < 10:
                print(" ", end="")
            print(num, end="")
        print("")


def grilles(tab):
    T = []
    n = int(len(tab) / 6)
    for i in range(n):
        grille = []
        for j in range(5):
            grille.append(tab[1 + j + (6 * i)])
        T.append(grille)
    return T


# transforme une grille de string en grille 5*5 de int (tableau dans tableau)
def grille_to_int(G):
    T = []
    for i in range(5):
        T.append([int(i) for i in G[i].split(" ") if i != ""])
    return T


# renvoie une grille 5*5 avec des 1 si le num est sorti, 0 sinon
def grille_tiree(G, L):
    T = []
    for i in range(5):
        t = []
        for j in range(5):
            if G[i][j] in L:
                t.append(1)
            else:
                t.append(0)
        T.append(t)
    return T


def calcul_grille(G, L):
    cpt = 0
    for i in range(5):
        for j in range(5):
            if not (G[i][j] in L):
                cpt += G[i][j]
    return cpt


# renvoie True si la grille triée est valide
def check_grille(G, L):
    G1 = grille_tiree(G, L)
    score = calcul_grille(G, L) * L[-1]
    # check des lignes
    for i in range(5):
        if G1[i][0] == G1[i][1] == G1[i][2] == G1[i][3] == G1[i][4] == 1:
            return score
    # check des colonnes
    for i in range(5):
        if G1[0][i] == G1[1][i] == G1[2][i] == G1[3][i] == G1[4][i] == 1:
            return score
    return 0


grilles_raw = input[1:]
grilles_string = grilles(grilles_raw)


print("gagnant le plus rapide :")
gagnant = False
id_gagnant = -1
score_gagnant = 0

nombre_tires = 0
while not (gagnant):
    nombre_tires += 1
    for i in range(len(grilles_string)):
        grille = grilles_string[i]
        grille_int = grille_to_int(grille)
        score = check_grille(grille_int, tirage[: nombre_tires + 1])
        if score != 0:
            gagnant = True
            print("gagnant :", i)
            print("score du gagnant :", score)
            break


print("\ngagnant le plus lent :")
all_gagnant = False
id_gagnant = -1
score_gagnant = 0
liste_gagnants = []

nombre_tires = 0
while not (all_gagnant):
    nombre_tires += 1
    for i in range(len(grilles_string)):
        grille = grilles_string[i]
        grille_int = grille_to_int(grille)
        score = check_grille(grille_int, tirage[: nombre_tires + 1])
        if score != 0:
            if not (i in liste_gagnants):
                liste_gagnants.append(i)
                if len(liste_gagnants) >= len(grilles_string):
                    all_gagnant = True
                    print("gagnant :", i)
                    print("score du gagnant :", score)
                    break