import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = ouvre_txt("2021/day12/test")
for i in range(len(input)):
    input[i] = input[i].split("-")
# print_tab(input)

chemins = []


def parcours_single(chemin):
    pos = chemin[-1]
    suivants = []
    if pos == "end":
        chemins.append(chemin)
        return True
    # calcul de toutes les grotes connectées
    for i in range(len(input)):
        if input[i][0] == pos:
            suivants.append(input[i][1])
        if input[i][1] == pos:
            suivants.append(input[i][0])
    # check sur tous les chemins suivants
    for v in suivants:
        if (v.lower() != v) or (v.lower() == v and not (v in chemin)):
            parcours_single(chemin + [v])


parcours_single(["start"])

print("chemins différents :", len(chemins))

# partie 2 ******************************


chemins = []


def parcours_twice(chemin):
    pos = chemin[-1]
    suivants = []
    if pos == "end":
        chemins.append(chemin)
        return True
    # calcul de toutes les grotes connectées
    for i in range(len(input)):
        if input[i][0] == pos:
            suivants.append(input[i][1])
        if input[i][1] == pos:
            suivants.append(input[i][0])
    # check sur tous les chemins suivants
    for v in suivants:
        if v != "start":
            if (v.lower() != v) or not (v in chemin):
                parcours_twice(chemin + [v])
            else:
                second_passage = True
                for grotte in chemin:
                    if (grotte.lower() == grotte) and (chemin.count(grotte) > 1):
                        second_passage = False
                if second_passage:
                    parcours_twice(chemin + [v])


parcours_twice(["start"])

print("chemins différents :", len(chemins))