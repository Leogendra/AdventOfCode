import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *

input = to_int([line.split(",") for line in open("2021/day7/test")][0])

min_align = 0
nbr_carbu = 99999999
for j in range(max(input)):
    cpt = 0
    for i in range(len(input)):
        n = abs(input[i] - j)
        cpt += int((n * (n + 1)) / 2)
    if cpt < nbr_carbu:
        nbr_carbu = cpt
        min_align = j

print("alignement sur", min_align, ", cout :", nbr_carbu)