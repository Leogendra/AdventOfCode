for fichier in ["test", "input"]:
	jeu = [line.strip().split(",") for line in open(f"2022/day4/{fichier}.txt","r")]
	cpt = 0
	for line in jeu:
		sector1 = [int(sec) for sec in line[0].split("-")]
		sector2 = [int(sec) for sec in line[1].split("-")]
		if (sector1[0] <= sector2[0] and sector1[1] >= sector2[1]) or (sector2[0] <= sector1[0] and sector2[1] >= sector1[1]):
			cpt += 1
		
	print(f"star 1 {fichier} :",cpt)
	
	cpt = 0
	for line in jeu:
		sector1 = [int(sec) for sec in line[0].split("-")]
		sector2 = [int(sec) for sec in line[1].split("-")]
		if (sector1[1] == sector2[0]) or (sector2[1] == sector1[0]):
			cpt += 1
		elif sector1[1] > sector2[0]:
			if sector2[1] > sector1[0]:
				cpt += 1
	
	print(f"star 2 {fichier} :",cpt,"\n")