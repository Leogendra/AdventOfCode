for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day4/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    gains = 0
    for line in data:
        jeu = line.split(":")[1]
        _gagnants, _numeros = jeu.split("|")
        gagnants = [int(num) for num in _gagnants.strip().split(" ") if num != '']
        numeros = [int(num) for num in _numeros.strip().split(" ") if num != '']
        
        numerosGagnants = 0
        for num in numeros:
            if num in gagnants:
                numerosGagnants += 1

        if numerosGagnants > 0:
            gains += 2**(numerosGagnants - 1)

    print(f"Somme des gains : {gains}")
    
    print("\n\033[93m--- Part Two ---\033[0m")

    nbCartes = 0
    cartes = {}
    for line in data:
        _carte, _jeu = line.split(":")
        carte_id = _carte.split(" ")[-1]
        _gagnants, _numeros = _jeu.split("|")
        gagnants = [int(num) for num in _gagnants.strip().split(" ") if num != '']
        numeros = [int(num) for num in _numeros.strip().split(" ") if num != '']
        cartes[carte_id] = {"win":gagnants, "nums":numeros, 'number':1}
        

    for id, carte in cartes.items():
        gagnants = carte['win']
        numeros = carte['nums']
        number = carte['number']
        nbCartes += number
        
        numerosGagnants = 0
        for num in numeros:
            if num in gagnants:
                numerosGagnants += 1
                cartes[str(int(id) + numerosGagnants)]['number'] += number

    # somme des number

    print(f"Somme des cartes : {nbCartes}")
    # break