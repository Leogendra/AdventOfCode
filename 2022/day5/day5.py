def deplacer(p, n, deb, fin):
	for _ in range(n):
		if p[deb] != []:
			bloc = p[deb].pop()
			p[fin].append(bloc)
	return p


def deplacerBloc(p, n, deb, fin):
	blocs = []
	taille = min(len(p[deb]),n)
	
	for _ in range(taille):
		blocs.append(p[deb].pop())
	
	blocs.reverse()
	for bloc in blocs:
		p[fin].append(bloc)
		
	return p



for fichier in ["test", "input"]:
	input = [line for line in open(f"2022/day5/{fichier}.txt","r")]
	jeu = []
	instructions = []
	jeu_fini = False
	for line in input:
		if line.strip() == "":
			jeu_fini = True
			continue
		if jeu_fini:
			instructions.append([x for x in line.split() if x.isnumeric()])
		else:
			jeu.append(line)

	# préparation pour parser l'entrée
	jeu.reverse()
	nbPiles = int(jeu[0].strip()[-1])
	piles = [[] for _ in range(nbPiles)]
	
	# Parsing de l'entrée
	for i in range(1,len(jeu)):
		for j in range(nbPiles):
			lettre = jeu[i][1+4*j]
			if lettre != " ":
				piles[j].append(lettre)

	piles1 = piles.copy()
	# lecture des instructions
	for n, dep, fin in instructions:
		piles1 = deplacer(piles1, int(n), int(dep)-1, int(fin)-1)
	
	list_top1 = [pile[-1] for pile in piles1 if pile != []]
	
	print("Part 1 :","".join(list_top1))


	piles2 = piles.copy()
	# lecture des instructions
	for n, dep, fin in instructions:
		piles2 = deplacerBloc(piles1, int(n), int(dep)-1, int(fin)-1)

	list_top2 = [pile[-1] for pile in piles2 if pile != []]
	
	print("Part 2 :","".join(list_top2))