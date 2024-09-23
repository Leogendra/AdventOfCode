import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = ouvre_txt("2021/day10/test")


def val_char(c):
    if c == ">":
        return 25137
    if c == "}":
        return 1197
    if c == "]":
        return 57
    if c == ")":
        return 3


invalides = []
incompletes = []
cpt = 0
for ligne in input:
    trace = []
    for i in range(len(ligne)):
        if ligne[i] in ["(", "[", "{", "<"]:
            trace.append(ligne[i])
        else:
            if (trace[-1] == "<") and (ligne[i] != ">"):
                invalides.append(ligne)
                cpt += val_char(ligne[i])
                break
            elif (trace[-1] == "{") and (ligne[i] != "}"):
                invalides.append(ligne)
                cpt += val_char(ligne[i])
                break
            elif (trace[-1] == "(") and (ligne[i] != ")"):
                invalides.append(ligne)
                cpt += val_char(ligne[i])
                break
            elif (trace[-1] == "[") and (ligne[i] != "]"):
                invalides.append(ligne)
                cpt += val_char(ligne[i])
                break
            else:
                del trace[-1]
    if not (ligne in invalides):
        incompletes.append(trace)


print("score erreur :", cpt)


score_lignes = []
for ligne in incompletes:
    cpt = 0
    for i in range(len(ligne)):
        c = ligne.pop()
        if c == "<":
            cpt = cpt * 5 + 4
        elif c == "{":
            cpt = cpt * 5 + 3
        elif c == "[":
            cpt = cpt * 5 + 2
        else:
            cpt = cpt * 5 + 1
    score_lignes.append(cpt)


score_lignes.sort()
print("gagnant incomplet :", score_lignes[len(score_lignes) // 2])