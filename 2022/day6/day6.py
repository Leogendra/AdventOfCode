for fichier in ["test", "input"]:
	ligne = [line for line in open(f"2022/day6/{fichier}.txt","r")][0]
	shift = 4
	marker = -1
	for i in range(shift,len(ligne)):
		str = ligne[i-shift:i]
		is_marker = True
		for c in str:
			if str.count(c) > 1:
				is_marker = False
		if is_marker:
			marker = i
			break

	print("Part 1 :",marker)	
	shift = 14
	marker = -1
	for i in range(shift,len(ligne)):
		str = ligne[i-shift:i]
		is_marker = True
		for c in str:
			if str.count(c) > 1:
				is_marker = False
		if is_marker:
			marker = i
			break
	
	print("Part 2 :",marker)