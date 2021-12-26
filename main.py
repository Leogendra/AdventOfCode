true = True
false = False
import time

def ouvre(fichier):
  input = ouvre_txt(fichier)
  return to_int(input)


def ouvre_txt(fichier):
  input = []
  with open(fichier, "r") as fd:
    for ligne in fd:
      if ligne[-1] == '\n':
        input.append(ligne[:-1])
      else:
        input.append(ligne)
  return input


def binaire(nbr):
  cpt = 0
  n = len(nbr)
  for i in range(n):
    cpt += int(nbr[n-i-1])*(2**i)
  return cpt


def to_int(tab):
  for i in range(len(tab)):
    tab[i] = int(tab[i])
  return tab


def print_tab(T):
  print("[",end="")
  for i in range(len(T)):
    if i != 0:
      print("\n ",end="")
    print(T[i],end="")
  print("]\n")





print("********** Day 1 **********")
#Ouverture du fichier input
input = ouvre("day1/input.txt")

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







print("\n********** Day 2 **********")
#Ouverture du fichier input

input = ouvre_txt("day2/input.txt")

#comptage des incrementations
n = len(input)
print("Nombre d'inputs :",n)

horiz = 0
depth = 0
aim = 0

for i in range(n):
  nbr = int(input[i][-1])
  if input[i][0] == 'f':
    horiz += nbr
    depth += aim*nbr
  elif input[i][0] == 'd':
    aim += nbr
  else:
    aim -= nbr

print("profondeur =",depth)
print("horizontal =",horiz)
print("horizontal*profondeur =",depth*horiz)





print("\n********** Day 3 **********")

input = ouvre_txt("day3/input.txt")
n = len(input)
m = len(input[0])
print("Nombre d'inputs :",n)

gamma = [0 for i in range(m)]
epsy = [1 for i in range(m)]

for i in range(m):
  cpt = 0
  for j in range(n):
    cpt += int(input[j][i])
  if cpt >= n/2:
    gamma[i] = '1'
    epsy[i] = '0'

#print("gamma :",gamma)
#print("epsylon :",epsy)
print("gamma*epsylon =",binaire(gamma)*binaire(epsy))

gamma2 = [0 for i in range(m)]
epsy2 = [1 for i in range(m)]
input_gamma = input.copy()
input_epsy = input.copy()
cpt1 = 0
cpt2 = 0

#traitement du machin a oxygène
i = 0
while (i < m) and (len(input_gamma) > 1):
  n = len(input_gamma)
  cpt1 = 0
  for j in range(n):
    cpt1 += int(input_gamma[j][i])

  if cpt1 >= n/2:
    j = 0
    while (j < len(input_gamma)):
      if input_gamma[j][i] == '0':
        del input_gamma[j]
      else:
        j += 1
  else:
    j = 0
    while (j < len(input_gamma)):
      if input_gamma[j][i] == '1':
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

  if cpt2 >= n/2:
    j = 0
    while (j < len(input_epsy)):
      if input_epsy[j][i] == '1':
        del input_epsy[j]
      else:
        j += 1
  else:
    j = 0
    while (j < len(input_epsy)):
      if input_epsy[j][i] == '0':
        del input_epsy[j]
      else:
        j += 1
  i += 1


print("générateur d'O2 :",input_gamma)
print("épurateur CO2 :",input_epsy)
print("générateur*épurateur =",binaire(input_gamma[0])*binaire(input_epsy[0]))









print("\n********** Day 4 **********")
input = ouvre_txt("day4/test.txt")

tirage = to_int(input[0].split(","))
#print(tirage)

def aff_grille(G):
  for i in range(5):
    for j in range(5):
      num = G[i][j]
      if j != 0:
        print(" ",end='')
      if num < 10:
        print(" ",end='')
      print(num,end='')
    print("")



def grilles(tab):
  T = []
  n = int(len(tab)/6)
  for i in range(n):
    grille = []
    for j in range(5):
      grille.append(tab[1+j+(6*i)])
    T.append(grille)
  return T

#transforme une grille de string en grille 5*5 de int (tableau dans tableau)
def grille_to_int(G):
  T = []
  for i in range(5):
    T.append([int(i) for i in G[i].split(" ") if i != ''])
  return T


#renvoie une grille 5*5 avec des 1 si le num est sorti, 0 sinon
def grille_tiree(G, L):
  T = []
  for i in range(5):
    t = []
    for j in range(5):
      if (G[i][j] in L):
        t.append(1)
      else:
        t.append(0)
    T.append(t)
  return T


def calcul_grille(G, L):
  cpt = 0
  for i in range(5):
    for j in range(5):
      if not(G[i][j] in L):
        cpt += G[i][j]
  return cpt


#renvoie true si la grille triée est valide
def check_grille(G, L):
  G1 = grille_tiree(G, L)
  score = calcul_grille(G, L) * L[-1]
  #check des lignes
  for i in range(5):
    if G1[i][0] == G1[i][1] == G1[i][2] == G1[i][3] == G1[i][4] == 1:
      return score
  #check des colonnes
  for i in range(5):
    if G1[0][i] == G1[1][i] == G1[2][i] == G1[3][i] == G1[4][i] == 1:
      return score
  return 0

'''
grille1 = grilles_string[0]
print("\ngrille 1 :",grille1)
grille1_int = grille_to_int(grille1)
print("\ngrille 1 en int :")
aff_grille(grille1_int)
grille1_tiree = grille_tiree(grille1_int,[22,2,3,14,18,19,7])
print("\ngrille tirée :")
aff_grille(grille1_tiree)
grille1_valide = check_grille(grille1_int,[22,2,3,14,18,19,7])
print("\ngrille 1 valide ? ",grille1_valide)
'''

grilles_raw = input[1:]
grilles_string = grilles(grilles_raw)


print("gagnant le plus rapide :")
gagnant = false
id_gagnant = -1
score_gagnant = 0

nombre_tires = 0
while not(gagnant):
  nombre_tires += 1
  for i in range(len(grilles_string)):
    grille = grilles_string[i]
    grille_int = grille_to_int(grille)
    score = check_grille(grille_int,tirage[:nombre_tires+1])
    if (score != 0):
      gagnant = true
      print("gagnant :",i)
      print("score du gagnant :",score)
      #print("tirage gagnant :",tirage[:nombre_tires+1])
      #print("grille gagnante :")
      #aff_grille(grille_int)
      break


print("\ngagnant le plus lent :")
all_gagnant = false
id_gagnant = -1
score_gagnant = 0
liste_gagnants = []

nombre_tires = 0
while not(all_gagnant):
  nombre_tires += 1
  for i in range(len(grilles_string)):
    grille = grilles_string[i]
    grille_int = grille_to_int(grille)
    score = check_grille(grille_int,tirage[:nombre_tires+1])
    if (score != 0):
      if not(i in liste_gagnants):
        liste_gagnants.append(i)
        if len(liste_gagnants) >= len(grilles_string):
          all_gagnant = true
          print("gagnant :",i)
          print("score du gagnant :",score)
          #print("tirage gagnant :",tirage[:nombre_tires+1])
          #print("grille gagnante :")
          #aff_grille(grille_int)
          break












print("\n********** Day 5 **********")
input = ouvre_txt("day5/test.txt")

def txt_to_coord(T):
  T2 = [x.split(" -> ") for x in T]
  C = []
  for x in T2:
    x1 = int(x[0].split(",")[0])
    y1 = int(x[0].split(",")[1])
    x2 = int(x[1].split(",")[0])
    y2 = int(x[1].split(",")[1])
    C.append([x1,y1,x2,y2])
  return C

data5 = txt_to_coord(input)
#print_tab(data5)

max_value_x = 0
max_value_y = 0
for i in range(len(data5)):
  for j in range(4):
    if (j%2 == 0):
      max_value_x = max(max_value_x,data5[i][j])
    else:
      max_value_y = max(max_value_y,data5[i][j])

max_value_x += 1
max_value_y += 1

hydro = [[0 for i in range(max_value_x)] for j in range(max_value_y)]

cpt = 0
#parcourt des coordonées
for pos in data5:
  cpt += 1
  x1 = pos[0]
  y1 = pos[1]
  x2 = pos[2]
  y2 = pos[3]
  if (x1 == x2) or (y1 == y2):
    if x1 == x2:
      if y1 > y2:
        y1, y2 = y2, y1
      for i in range(y1,y2+1):
        hydro[i][x1] += 1
    else:
      if x1 > x2:
        x1, x2 = x2, x1
      for i in range(x1,x2+1):
        hydro[y1][i] += 1

#print_tab(hydro)

chevauchements = 0
for i in range(max_value_y):
  for j in range(max_value_x):
    if hydro[i][j] > 1:
      chevauchements += 1

print("chevauchements linéaires :",chevauchements)


#Partie 2 ****************************************

hydro = [[0 for i in range(max_value_x)] for j in range(max_value_y)]
cpt = 0
#parcourt des coordonées
for pos in data5:
  cpt += 1
  x1 = pos[0]
  y1 = pos[1]
  x2 = pos[2]
  y2 = pos[3]
  if (x1 == x2) or (y1 == y2):
    if x1 == x2:
      if y1 > y2:
        y1, y2 = y2, y1
      for i in range(y1,y2+1):
        hydro[i][x1] += 1
    else:
      if x1 > x2:
        x1, x2 = x2, x1
      for i in range(x1,x2+1):
        hydro[y1][i] += 1
  else:
    if x1 < x2:
      if y1 < y2:
        for i in range(x1,x2+1):
          hydro[y1][i] += 1
          y1 += 1
      else:
        for i in range(x1,x2+1):
          hydro[y1][i] += 1
          y1 -= 1
    else:
      if y1 < y2:
        for i in range(x2,x1+1):
          hydro[y2][i] += 1
          y2 -= 1
      else:
        for i in range(x2,x1+1):
          hydro[y2][i] += 1
          y2 += 1


#print_tab(hydro)



chevauchements = 0
for i in range(max_value_y):
  for j in range(max_value_x):
    if hydro[i][j] > 1:
      chevauchements += 1


print("chevauchements + diagonales :",chevauchements)













print("\n********** Day 6 **********")
input = [line.split(",") for line in open("day6/test.txt")][0]
for i in range(len(input)):
  input[i] = int(input[i])

data6 = input.copy()

def poisson(j):
  D = [0 for i in range(9)]
  D[0] = 1
  for i in range(j):
    nb_ovul = D[0]
    for j in range(1, 9):
      D[j-1] = D[j]
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
  cpt += poisson(jours-x)

print(jours,"jours,",cpt,"poissons.")


jours = 256
cpt = 0
temps = time.time()
for x in data6:
  cpt += poisson(jours-x)

print(jours,"jours,",cpt,"poissons.")















print("\n********** Day 7 **********")
input = to_int([line.split(",") for line in open("day7/test")][0])

min_align = 0
nbr_carbu = 99999999
for j in range(max(input)):
  cpt = 0
  for i in range(len(input)):
    n = abs(input[i]-j)
    cpt += int((n*(n+1))/2)
  if cpt < nbr_carbu:
    nbr_carbu = cpt
    min_align = j

print("alignement sur",min_align,", cout :",nbr_carbu)
















print("\n********** Day 8 **********")
input = []
with open("day8/test", "r") as fd:
  for ligne in fd:
    li = ligne.split("|")
    input.append([li[0].strip().split(" "),li[1].strip().split(" ")])

#print_tab(input)

cpt = 0
for i in range(len(input)):
  for j in range(len(input[i][1])):
    n = len(input[i][1][j])
    if (n == 2) or (n == 3) or (n == 4) or (n == 7):
      cpt += 1

print("chiffres valeurs unique :",cpt)


def seule_lettre(mot1,mot2):
  for i in range(len(mot1)):
    trouve = false
    for j in range(len(mot2)):
      if mot1[i] == mot2[j]:
        trouve = true
    if not(trouve):
      return mot1[i]
  return "pas trouvé"


#renvoie le tableau [1, 4, 7, 8] avec leur code respectifs
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
      

#renvoie toutes les lettres de mot1 qui ne sont pas dans mot2
def mot_moins(mot1,mot2):
  L = []
  for i in range(len(mot1)):
    trouve = false
    for j in range(len(mot2)):
      if mot1[i] == mot2[j]:
        trouve = true
    if not(trouve):
      L.append(mot1[i])
  return L


#renvoie les lettres communes entre mot1 et mot2
def lettre_communs(mot1,mot2):
  L = []
  for i in range(len(mot1)):
    for j in range(len(mot2)):
      if mot1[i] == mot2[j]:
        L.append(mot1[i])
  return L


#renvoie le mot ayant toutes les lettres
def mot_avec(mots,lettres):
  for i in range(len(mots)):
    if len(mots[i]) == 5:
      tous = true
      for l in range(len(lettres)):
        y_est = false
        for k in range(len(mots[i])):
          if lettres[l] == mots[i][k]:
            y_est = true
        if not(y_est):
          tous = false
      if tous:
        return mots[i]
  return "aucun"



cpt = 0
for i in range(len(input)):
  chfs = trouve_chiffres(input[i][0])
  chi = ['' for i in range(10)]
  let = ['' for i in range(7)]

  chi[1] = chfs[0]
  chi[4] = chfs[1]
  chi[7] = chfs[2]
  chi[8] = chfs[3]
  let[0] = seule_lettre(chi[7],chi[1])
  c_ou_f = [chi[1][0],chi[1][1]]
  b_ou_d = mot_moins(chi[4],chi[7])
  chi[3] = mot_avec(input[i][0],c_ou_f)

  #recherche du 6 (celui qui n'a que c OU f) et 0 (b OU d)
  for k in input[i][0]:
    if (len(k) == 6) and (mot_moins(c_ou_f,k) != []):
      chi[6] = k
      #lettre c
      let[2] = mot_moins(c_ou_f,k)[0]
    if (len(k) == 6) and (mot_moins(b_ou_d,k) != []):
      chi[0] = k
  
  deux_ou_5 = []
  for k in input[i][0]:
    if (len(k) == 6) and (k != chi[6]) and (k != chi[0]):
      chi[9] = k
    if (len(k) == 5) and (k != chi[3]):
      deux_ou_5.append(k)
  chi[2] = mot_avec(deux_ou_5,let[2])
  if deux_ou_5[0] == chi[2]:
    chi[5] = deux_ou_5[1]
  else:
    chi[5] = deux_ou_5[0]

  decode = 0
  for j in range(4):
    num = input[i][1][j]
    for k in range(len(chi)):
      if (len(num) == len(chi[k])) and (len(lettre_communs(num,chi[k])) == len(num)):
        decode += k * (10**(3-j))
  cpt += decode



print("valeur affichée :",cpt)













print("\n********** Day 9 **********")
input = ouvre_txt("day9/test")


#renvoie tous les voisins du point [i,j]
def voisins(i,j,mi,mj):
  V = []
  if i != 0:
    V.append([i-1,j])
  if j != 0:
    V.append([i,j-1])
  if i != mi:
    V.append([i+1,j])
  if j != mj:
    V.append([i,j+1])
  return V

#return true si le ptn [i,j] est le plus petit de ses voisins
def est_plus_petit(i,j,mi,mj):
  vois = voisins(i,j,mi,mj)
  for v in vois:
    if input[v[1]][v[0]] <= input[j][i]:
      return false
  return true


#calcul des minimum locaux
min_locaux = []
max_i = len(input[0])
max_j = len(input)
for j in range(max_j):
  for i in range(max_i):
    if est_plus_petit(i,j,max_i-1,max_j-1):
      min_locaux.append([i,j])

#calcul des niveaux de risques
cpt = 0
for p in min_locaux:
  cpt += int(input[p[1]][p[0]]) + 1

print("niveau de risque =",cpt)



#Partie 2 ***************************


def couvre_voisins(pt,b):
  x = pt[0]
  y = pt[1]
  #print("i=",b,",point:",pt,", input:",input[y][x],", data:",data9[y][x])
  if (input[y][x] != '9') and (data9[y][x] == 0):
    data9[y][x] = b
    vois = voisins(x,y,max_i-1,max_j-1)
    for v in vois:
      couvre_voisins(v,b)




#on créer une map avec que des 0
data9 = []
for i in range(max_j):
  data9.append([0 for i in range(max_i)])

#on créer la base des bassins aux minimum locaux
for i in range(len(min_locaux)):
  data9[min_locaux[i][1]][min_locaux[i][0]] = i+1


#fonction pour calculer les bassins
for i in range(len(min_locaux)):
  x = min_locaux[i][0]
  y = min_locaux[i][1]
  vois = voisins(x,y,max_i-1,max_j-1)
  for v in vois:
    couvre_voisins(v,i+1)


#compter la taille des bassins
b1 = 0
b2 = 0
b3 = 0
for i in range(len(min_locaux)):
  cpt = 0
  for ligne in data9:
    for pt in ligne:
      if (i+1) == pt:
        cpt += 1
  if cpt > b1:
    b3 = b2
    b2 = b1
    b1 = cpt
  elif cpt > b2:
    b3 = b2
    b2 = cpt
  elif cpt > b3:
    b3 = cpt
  

print("Bassin 1 :",b1)
print("Bassin 2 :",b2)
print("Bassin 3 :",b3)
print("B1*B2*B3 :",b3*b2*b1)













print("\n********** Day 10 **********")
input = ouvre_txt("day10/test")


def val_char(c):
  if c == '>':
    return 25137
  if c == '}':
    return 1197
  if c == ']':
    return 57
  if c == ')':
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
      if (trace[-1] == '<') and (ligne[i] != '>'):
        invalides.append(ligne)
        cpt += val_char(ligne[i])
        break
      elif (trace[-1] == '{') and (ligne[i] != '}'):
        invalides.append(ligne)
        cpt += val_char(ligne[i])
        break
      elif (trace[-1] == '(') and (ligne[i] != ')'): 
        invalides.append(ligne)
        cpt += val_char(ligne[i])
        break
      elif (trace[-1] == '[') and (ligne[i] != ']'):
        invalides.append(ligne)
        cpt += val_char(ligne[i])
        break
      else:
        del trace[-1]
  if not(ligne in invalides):
    incompletes.append(trace)


print("score erreur :",cpt)




score_lignes = []
for ligne in incompletes:
  cpt = 0
  for i in range(len(ligne)):
    c = ligne.pop()
    if c == '<':
      cpt = cpt*5 + 4
    elif c == '{':
      cpt = cpt*5 + 3
    elif c == '[':
      cpt = cpt*5 + 2
    else:
      cpt = cpt*5 + 1
  score_lignes.append(cpt)


score_lignes.sort()
print("gagnant incomplet :",score_lignes[len(score_lignes)//2])



















print("\n********** Day 11 **********")
input = []
data11 = ouvre_txt("day11/test")
for i in range(10):
    input.append([int(data11[i][j]) for j in range(10)])

partie_2 = input.copy()


def voisin_diag(pt, max_x, max_y):
  x = pt[0]
  y = pt[1]
  vois = voisins(x,y,max_x,max_y)
  if x != 0:
    if y != 0:
      vois.append([x-1,y-1])
    if y != max_y:
      vois.append([x-1,y+1])
  if x != max_x:
    if y != 0:
      vois.append([x+1,y-1])
    if y != max_y:
      vois.append([x+1,y+1])
  return vois


def octoplus(oc):
  global cpt, input
  x = oc[0]
  y = oc[1]
  if input[y][x] != 0:
    input[y][x] += 1
    if input[y][x] > 9:
      cpt += 1
      input[y][x] = 0
      vois = voisin_diag(oc, 9, 9)
      for v in vois:
        octoplus(v)




cpt = 0
for caca in range(100):
  #incrément des poulpes
  for j in range(10):
    for i in range(10):
      input[j][i] += 1
  #check des luminéscences
  for j in range(10):
    for i in range(10):
      if input[j][i] > 9:
        octoplus([i,j])


print("nombre de flashs :",cpt)


#reset de l'input
input = []
for i in range(10):
    input.append([int(data11[i][j]) for j in range(10)])

jours = 0
all_flash = false
while not(all_flash):
  jours += 1
  #incrément des poulpes
  for j in range(10):
    for i in range(10):
      input[j][i] += 1

  #check des luminéscences
  for j in range(10):
    for i in range(10):
      if input[j][i] > 9:
        octoplus([i,j])

  #check si tous les poulpes ont slashés en même temps
  all_flash = true
  for j in range(10):
    for i in range(10):
      if input[j][i] != 0:
        all_flash = false



print("tous flashés : étape",jours)













print("\n********** Day 12 **********")
input = ouvre_txt("day12/test")
for i in range(len(input)):
  input[i] = input[i].split("-")
#print_tab(input)

chemins = []

def parcours_single(chemin):
  pos = chemin[-1]
  suivants = []
  if pos == 'end':
    chemins.append(chemin)
    return true
  #calcul de toutes les grotes connectées
  for i in range(len(input)):
    if input[i][0] == pos:
      suivants.append(input[i][1])
    if input[i][1] == pos:
      suivants.append(input[i][0])
  #check sur tous les chemins suivants
  for v in suivants:
      if (v.lower() != v) or (v.lower() == v and not(v in chemin)):
        parcours_single(chemin+[v])


parcours_single(['start'])

print("chemins différents :",len(chemins))

# partie 2 ******************************





chemins = []

def parcours_twice(chemin):
  pos = chemin[-1]
  suivants = []
  if pos == 'end':
    chemins.append(chemin)
    return true
  #calcul de toutes les grotes connectées
  for i in range(len(input)):
    if input[i][0] == pos:
      suivants.append(input[i][1])
    if input[i][1] == pos:
      suivants.append(input[i][0])
  #check sur tous les chemins suivants
  for v in suivants:
    if v != 'start':
      if (v.lower() != v) or not(v in chemin):
        parcours_twice(chemin+[v])
      else:
        second_passage = true
        for grotte in chemin:
          if (grotte.lower() == grotte) and (chemin.count(grotte) > 1):
            second_passage = false
        if second_passage:
          parcours_twice(chemin+[v])



parcours_twice(['start'])

print("chemins différents :",len(chemins))

















print("\n********** Day 13 **********")

input = ouvre_txt("day13/input")
for i in range(len(input)):
  input[i] = input[i].split(",")


def plier(feuille,instr,mx,my):
  sens = instr[0]
  coord = int(instr[1])
  new_feuille = []
  new_x = mx
  new_y = my
  #pliage vers le haut
  if sens == 'y':
    new_y = coord-1
    for i in range(new_y+1):
      new_feuille.append(feuille[i])
      for j in range(mx+1):
        if feuille[my-i][j] == '#':
          new_feuille[i][j] = '#'
  #pliage vers la gauche
  if sens == 'x':
    new_x = coord-1
    for i in range(my+1):
      tmp = [feuille[i][j] for j in range(new_x+1)]
      for j in range(new_x+1):
        if feuille[i][new_x+2+j] == '#':
          tmp[new_x-j] = '#'
      new_feuille.append(tmp)

  return [new_feuille, new_x, new_y]
  


def aff_feuille(g,x,y):
  for i in range(y+1):
    for j in range(x+1):
      if g[i][j] == '#':
        print('#',end='')
      else:
        print(' ',end='')
    print("")
  print("")



points = []
pliages = []
switch = false
max_x = 0
max_y = 0

for ligne in input:
  if ligne == ['']:
    switch = true
  elif switch:
    pliages.append([ligne[0].split("=")[0][-1],ligne[0].split("=")[-1]])
  else:
    x = int(ligne[0])
    y = int(ligne[1])
    max_x = max(x, max_x)
    max_y = max(y, max_y)
    points.append([x, y])

#remplis une grille vide
grille = []
for i in range(max_y+1):
  grille.append(['.' for j in range(max_x+1)])


#placement des points
for pt in points:
  grille[pt[1]][pt[0]] = '#'

infos_nouvelle_grille = plier(grille,pliages[0],max_x,max_y)
nouvelle_grille = infos_nouvelle_grille[0]
new_max_x = infos_nouvelle_grille[1]
new_max_y = infos_nouvelle_grille[2]

#comptage des points
cpt = 0
for i in range(new_max_y+1):
  for j in range(new_max_x+1):
    if nouvelle_grille[i][j] == '#':
      cpt += 1


print("points après 1 pliage :",cpt)


inputl = ouvre_txt("day13/input")

def second_star():
    inputm = [x.split(",") for x in inputl if len(x.split(",")) == 2]
    d = set()
    for x in inputm:
        d.add((int(x[0]), int(x[1])))
    instr = []
    for x in inputl:
        y = x.split(" ")
        if len(y) == 3:
            z = y[2].split("=")
            instr.append((z[0], int(z[1])))
    for inst in instr:
        if inst[0] == "x":
            e = set()
            for x, y in d:
                if x < inst[1]:
                    e.add((x, y))
                elif x > inst[1]:
                    e.add((2 * inst[1] - x, y))
            d = e
        elif inst[0] == "y":
            e = set()
            for x, y in d:
                if y < inst[1]:
                    e.add((x, y))
                elif y > inst[1]:
                    e.add((x, 2 * inst[1] - y))
            d = e

    for i in range(6):
        st = ""
        for j in range(40):
            if (j, i) in d:
                st += "#"
            else:
                st += " "
        print(st)


print("après tous les pliage :")
second_star()

























print("\n********** Day 14 **********")


























