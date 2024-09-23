import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import *


#Ouverture du fichier input
input = ouvre("2021/day1/input.txt")

#comptage des incrementations
cpt = 0
n = len(input)
print("Nombre d'inputs :",n)
for i in range(1, n-2):
  som1 = input[i-1] + input[i] + input[i+1]
  som2 = input[i] + input[i+1] + input[i+2]
  if som1 < som2:
    cpt += 1
    
print("Nombre d'incréments :",cpt)
