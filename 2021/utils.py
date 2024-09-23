import time

def ouvre(fichier):
    input = ouvre_txt(fichier)
    return to_int(input)


def ouvre_txt(fichier):
    input = []
    with open(fichier, "r") as fd:
        for ligne in fd:
            if ligne[-1] == "\n":
                input.append(ligne[:-1])
            else:
                input.append(ligne)
    return input


def binaire(nbr):
    cpt = 0
    n = len(nbr)
    for i in range(n):
        cpt += int(nbr[n - i - 1]) * (2**i)
    return cpt


def to_int(tab):
    for i in range(len(tab)):
        tab[i] = int(tab[i])
    return tab


def print_tab(T):
    print("[", end="")
    for i in range(len(T)):
        if i != 0:
            print("\n ", end="")
        print(T[i], end="")
    print("]\n")