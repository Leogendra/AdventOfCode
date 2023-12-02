for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day1/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")
    
    somme = 0

    for line in data:
        chiffres = []
        for char in line:
            if not(char.isalpha()):
                chiffres.append(char)
    
        if len(chiffres) > 0:
            somme += int(chiffres[0] + chiffres[-1])
        
    print(f"Somme des lignes : {somme}")



    print("\n\033[93m--- Part Two ---\033[0m")
    

    # on ajoute les premières et dernières lettres pour que plusieurs chiffres puissent partager une lettre : eightwo
    numbers = {"one":"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"n9e"}

    somme = 0

    for line in data:
        
        for numStr, num in numbers.items():
            line = line.replace(numStr, num)
        
        chiffres = []
        for char in line:
            if not(char.isalpha()):
                chiffres.append(char)

        if len(chiffres) > 0:
            somme += int(chiffres[0] + chiffres[-1])
        
    print(f"Somme des lignes : {somme}")