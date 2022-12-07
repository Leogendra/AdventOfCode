#import lesProblèmes

def tailleDossier(d):
    if isinstance(d, list):
        return sum([tailleDossier(file) for file in d])
    else:
        return d
        

def dossiersAvecMoinsDe(d,n):
    cpt = 0
    if isinstance(d, list):
        taille = tailleDossier(d)
        if taille <= n:
            cpt += taille
        for doss in d:
            cpt += dossiersAvecMoinsDe(doss,n)
    return cpt
    

def dossierASupprimer(doss,n):
    dossierMin = float('inf')
    if isinstance(doss, list):
        tailleDoss = tailleDossier(doss)
        if tailleDoss >= n: 
            dossierMin = tailleDoss
        for d in doss:
            taille = tailleDossier(d)
            if isinstance(d,list) and (taille >= n) and (taille < dossierMin):
                dossierMin = min(taille,dossierASupprimer(d,n))
    return dossierMin

# CODE
for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    commandes = [line.strip() for line in open(f"2022/day7/{fichier}.txt","r")]
    arbre = []      # arborescence
    courant = []    # savoir où on se trouve
    dico = {}       # correspondance nom de dossier/indice dans l'arbre
    cptDossiers = 0 # compter le nb de dossiers dans le dossier courant
    
    commandes.pop(0)
    for line in commandes:          # construction de l'arborescence
        cmd = line.split()
        
        if cmd[0] == "$":           # si c'est un commande
            if cmd[1] == "cd":      # au met à jour notre pointeur courant
                if cmd[2] == "..":
                    courant.pop()
                else:
                    courant.append(dico[str(courant)][cmd[2]])
            elif cmd[1] == "ls":
                cptDossiers = 0
                continue
               
        else:                       
            ptrCourant = arbre             # pointeur vers le dossier courant
            for ind in courant:
                ptrCourant = ptrCourant[ind]
    
            if cmd[0] == "dir":
                ptrCourant.append([])      # append le dossier dans l'arbre
                if str(courant) in dico:
                    dico[str(courant)][cmd[1]] = cptDossiers
                else:
                    dico[str(courant)]= {cmd[1] : cptDossiers}
            else:
                ptrCourant.append(int(cmd[0]))  # append le fichier dans l'arbre
           
            cptDossiers += 1

    print("Part 1 :",dossiersAvecMoinsDe(arbre,100_000))

    tailleALiberer = tailleDossier(arbre)-40_000_000
    print("Part 2 :",dossierASupprimer(arbre,tailleALiberer))