import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = [line.split(",") for line in open("2021/day6/test.txt")][0]
for i in range(len(input)):
    input[i] = int(input[i])

data6 = input.copy()


def poisson(j):
    D = [0 for i in range(9)]
    D[0] = 1
    for i in range(j):
        nb_ovul = D[0]
        for j in range(1, 9):
            D[j - 1] = D[j]
        D[8] = nb_ovul
        D[6] += nb_ovul
    cpt = 0
    for i in range(9):
        cpt += D[i]
    return cpt


jours = 80
cpt = 0
temps = time.time()
for x in data6:
    cpt += poisson(jours - x)

print(jours, "jours,", cpt, "poissons.")


jours = 256
cpt = 0
temps = time.time()
for x in data6:
    cpt += poisson(jours - x)

print(jours, "jours,", cpt, "poissons.")