fichier = "input"
jeu = [line.split() for line in open(f"2022/day2/{fichier}.txt","r")]
cpt = 0
for j in jeu:
	if (j[0] == "A" and j[1] == "X"):
		cpt += 1 + 3
	elif (j[0] == "B" and j[1] == "X"):
		cpt += 1 + 0
	elif (j[0] == "C" and j[1] == "X"):
		cpt += 1 + 6
	elif (j[0] == "A" and j[1] == "Y"):
		cpt += 2 + 6
	elif (j[0] == "B" and j[1] == "Y"):
	    cpt += 2 + 3
	elif (j[0] == "C" and j[1] == "Y"):
	    cpt += 2 + 0
	elif (j[0] == "A" and j[1] == "Z"):
	    cpt += 3 + 0
	elif (j[0] == "B" and j[1] == "Z"):
	    cpt += 3 + 6
	elif (j[0] == "C" and j[1] == "Z"):
	    cpt += 3 + 3

print("partie 1 :", cpt)

cpt = 0
for j in jeu:
	if (j[0] == "A" and j[1] == "X"):
		cpt += 0 + 3
	elif (j[0] == "B" and j[1] == "X"):
		cpt += 0 + 1
	elif (j[0] == "C" and j[1] == "X"):
		cpt += 0 + 2
	elif (j[0] == "A" and j[1] == "Y"):
		cpt += 3 + 1
	elif (j[0] == "B" and j[1] == "Y"):
	    cpt += 3 + 2
	elif (j[0] == "C" and j[1] == "Y"):
	    cpt += 3 + 3
	elif (j[0] == "A" and j[1] == "Z"):
	    cpt += 6 + 2
	elif (j[0] == "B" and j[1] == "Z"):
	    cpt += 6 + 3
	elif (j[0] == "C" and j[1] == "Z"):
	    cpt += 6 + 1

print("partie 2 :", cpt)

