for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    data = [line.strip() for line in open(f"2018/day5/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")
    
    polymere = data[0]
    i = 1
    while i < len(polymere):
        u1, u2 = polymere[i-1], polymere[i]
        if (u1.lower() == u2.lower()) and (u1 != u2):
            polymere = polymere[:i-1] + polymere[i+1:]
            i = max(1, i-2)
        i += 1

    print(f"La taille restante du polymere est de {len(polymere)}")


    print("\n\033[93m--- Part Two ---\033[0m")
    
    import math, string

    polymere = data[0]
    longueurPlusCourte = float('inf')
    chaineARetirer = ''

    for LETTRE in string.ascii_uppercase:
        lettre = LETTRE.lower()
        poly = polymere.replace(LETTRE, '').replace(lettre, '')
        i = 1
        while i < len(poly):
            u1, u2 = poly[i-1], poly[i]
            if (u1.lower() == u2.lower()) and (u1 != u2):
                poly = poly[:i-1] + poly[i+1:]
                i = max(1, i-2)
            i += 1
        if longueurPlusCourte > len(poly):
            longueurPlusCourte = len(poly)
            chaineARetirer = LETTRE


    print(f"Longueur plus courte {longueurPlusCourte} en retirant {chaineARetirer}")