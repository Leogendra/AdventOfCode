import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = ouvre_txt("2021/day2/input.txt")

# comptage des incrementations
n = len(input)
print("Nombre d'inputs :", n)

horiz = 0
depth = 0
aim = 0

for i in range(n):
    nbr = int(input[i][-1])
    if input[i][0] == "f":
        horiz += nbr
        depth += aim * nbr
    elif input[i][0] == "d":
        aim += nbr
    else:
        aim -= nbr

print("profondeur =", depth)
print("horizontal =", horiz)
print("horizontal*profondeur =", depth * horiz)