import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = ouvre_txt("2021/day3/input.txt")
n = len(input)
m = len(input[0])
print("Nombre d'inputs :", n)

gamma = [0 for i in range(m)]
epsy = [1 for i in range(m)]

for i in range(m):
    cpt = 0
    for j in range(n):
        cpt += int(input[j][i])
    if cpt >= n / 2:
        gamma[i] = "1"
        epsy[i] = "0"

# print("gamma :",gamma)
# print("epsylon :",epsy)
print("gamma*epsylon =", binaire(gamma) * binaire(epsy))

gamma2 = [0 for i in range(m)]
epsy2 = [1 for i in range(m)]
input_gamma = input.copy()
input_epsy = input.copy()
cpt1 = 0
cpt2 = 0

# traitement du machin a oxygène
i = 0
while (i < m) and (len(input_gamma) > 1):
    n = len(input_gamma)
    cpt1 = 0
    for j in range(n):
        cpt1 += int(input_gamma[j][i])

    if cpt1 >= n / 2:
        j = 0
        while j < len(input_gamma):
            if input_gamma[j][i] == "0":
                del input_gamma[j]
            else:
                j += 1
    else:
        j = 0
        while j < len(input_gamma):
            if input_gamma[j][i] == "1":
                del input_gamma[j]
            else:
                j += 1

    i += 1


i = 0
while (i < m) and (len(input_epsy) > 1):
    n = len(input_epsy)
    cpt2 = 0
    for j in range(n):
        cpt2 += int(input_epsy[j][i])

    if cpt2 >= n / 2:
        j = 0
        while j < len(input_epsy):
            if input_epsy[j][i] == "1":
                del input_epsy[j]
            else:
                j += 1
    else:
        j = 0
        while j < len(input_epsy):
            if input_epsy[j][i] == "0":
                del input_epsy[j]
            else:
                j += 1
    i += 1


print("générateur d'O2 :", input_gamma)
print("épurateur CO2 :", input_epsy)
print("générateur*épurateur =", binaire(input_gamma[0]) * binaire(input_epsy[0]))