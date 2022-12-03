import string
fichier = "input"
jeu = [line.strip() for line in open(f"2022/day3/{fichier}.txt","r")]
#print(jeu)

letters = string.ascii_letters
cpt = 0
for line in jeu:
	compartment1 = line[len(line)//2:]
	compartment2 = line[:len(line)//2]
	for c in compartment1:
		if c in compartment2:
			cpt += 1 + letters.index(c)
			break

print("star 1 :",cpt)

cpt = 0
group = 0
group_compartment = []
for line in jeu:
	group += 1
	group_compartment.append(line)
	if group == 3:
		group = 0
		for c in group_compartment[0]:
			if c in group_compartment[1]:
				if c in group_compartment[2]:
					cpt += 1 + letters.index(c)
					group_compartment = []
					break

print("star 2 :",cpt)