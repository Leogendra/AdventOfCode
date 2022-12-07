def tailleDossier(d):
    if isinstance(d, list):
        return sum([tailleDossier(file) for file in d])
    else:
        return d


for fichier in ["test"]:
    commandes = [line.strip() for line in open(f"2022/day7/{fichier}.txt","r")]
    cpt1 = 0
    arbre = []    # arborescence
    courant = []  # savoir où on se trouve
    dico = {}     # correspondance nom de dossier/indice dans l'arbre
    cptDossiers = 0

    commandes.pop(0)
    for line in commandes:          # construction de l'arborescence
        cmd = line.split()
        # print("\ndico :",dico)
        # print("courant :",courant)
        # print("arbre :",arbre)
        # print("cmd :",cmd)

        if cmd[0] == "$":           # si c'est un commande
            if cmd[1] == "cd":      # au met à jour notre pointeur courant
                if cmd[2] == "..":
                    courant.pop()
                else:
                    courant.append(dico[cmd[2]])

            elif cmd[1] == "ls":
                cptDossiers = 0
                continue
        
        else:                       # si pas une commande mais une liste de dossiers/fichiers
            cur = arbre             # pointeur vers le dossier courant
            for ind in courant:
                cur = cur[ind]

            if cmd[0] == "dir":
                cur.append([])      # append le dossier dans l'arbre
                dico[cmd[1]] = cptDossiers
            else:   
                cur.append(int(cmd[0]))  # append le fichier dans l'arbre
            
            cptDossiers += 1

    tailleDossiers = [] # calcul de la taille de chaque dossier
    for doss in arbre:
        if tailleDossier(doss) > 100000:
            guez

    print("Part 1 :",cpt1)

    cpt2 = 0
	
    print("Part 2 :",cpt2)

    if cpt1 != 95437:
        break