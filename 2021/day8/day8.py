import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = []
with open("2021/day8/test", "r") as fd:
    for ligne in fd:
        li = ligne.split("|")
        input.append([li[0].strip().split(" "), li[1].strip().split(" ")])

cpt = 0
for i in range(len(input)):
    for j in range(len(input[i][1])):
        n = len(input[i][1][j])
        if (n == 2) or (n == 3) or (n == 4) or (n == 7):
            cpt += 1

print("chiffres valeurs unique :", cpt)


def seule_lettre(mot1, mot2):
    for i in range(len(mot1)):
        trouve = False
        for j in range(len(mot2)):
            if mot1[i] == mot2[j]:
                trouve = True
        if not (trouve):
            return mot1[i]
    return "pas trouvé"


# renvoie le tableau [1, 4, 7, 8] avec leur code respectifs
def trouve_chiffres(c):
    C = [0 for i in range(4)]
    for i in range(10):
        if len(c[i]) == 2:
            C[0] = c[i]
        elif len(c[i]) == 3:
            C[2] = c[i]
        elif len(c[i]) == 4:
            C[1] = c[i]
        elif len(c[i]) == 7:
            C[3] = c[i]
    return C


# renvoie toutes les lettres de mot1 qui ne sont pas dans mot2
def mot_moins(mot1, mot2):
    L = []
    for i in range(len(mot1)):
        trouve = False
        for j in range(len(mot2)):
            if mot1[i] == mot2[j]:
                trouve = True
        if not (trouve):
            L.append(mot1[i])
    return L


# renvoie les lettres communes entre mot1 et mot2
def lettre_communs(mot1, mot2):
    L = []
    for i in range(len(mot1)):
        for j in range(len(mot2)):
            if mot1[i] == mot2[j]:
                L.append(mot1[i])
    return L


# renvoie le mot ayant toutes les lettres
def mot_avec(mots, lettres):
    for i in range(len(mots)):
        if len(mots[i]) == 5:
            tous = True
            for l in range(len(lettres)):
                y_est = False
                for k in range(len(mots[i])):
                    if lettres[l] == mots[i][k]:
                        y_est = True
                if not (y_est):
                    tous = False
            if tous:
                return mots[i]
    return "aucun"


cpt = 0
for i in range(len(input)):
    chfs = trouve_chiffres(input[i][0])
    chi = ["" for i in range(10)]
    let = ["" for i in range(7)]

    chi[1] = chfs[0]
    chi[4] = chfs[1]
    chi[7] = chfs[2]
    chi[8] = chfs[3]
    let[0] = seule_lettre(chi[7], chi[1])
    c_ou_f = [chi[1][0], chi[1][1]]
    b_ou_d = mot_moins(chi[4], chi[7])
    chi[3] = mot_avec(input[i][0], c_ou_f)

    # recherche du 6 (celui qui n'a que c OU f) et 0 (b OU d)
    for k in input[i][0]:
        if (len(k) == 6) and (mot_moins(c_ou_f, k) != []):
            chi[6] = k
            # lettre c
            let[2] = mot_moins(c_ou_f, k)[0]
        if (len(k) == 6) and (mot_moins(b_ou_d, k) != []):
            chi[0] = k

    deux_ou_5 = []
    for k in input[i][0]:
        if (len(k) == 6) and (k != chi[6]) and (k != chi[0]):
            chi[9] = k
        if (len(k) == 5) and (k != chi[3]):
            deux_ou_5.append(k)
    chi[2] = mot_avec(deux_ou_5, let[2])
    if deux_ou_5[0] == chi[2]:
        chi[5] = deux_ou_5[1]
    else:
        chi[5] = deux_ou_5[0]

    decode = 0
    for j in range(4):
        num = input[i][1][j]
        for k in range(len(chi)):
            if (len(num) == len(chi[k])) and (
                len(lettre_communs(num, chi[k])) == len(num)
            ):
                decode += k * (10 ** (3 - j))
    cpt += decode


print("valeur affichée :", cpt)