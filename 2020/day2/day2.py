for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    input = [line.strip() for line in open(f"2020/day2/{fichier}.txt", "r")]

    print("--- Part One ---")

    nbValid = 0
    for line in input:
        infos = line.split(" ")
        min, max = map(int, infos[0].split("-"))
        letter = infos[1][0]
        password = infos[2]
        nbLetter = password.count(letter)
        if (nbLetter <= max) and (nbLetter >= min):
            nbValid += 1

    print(f"Nombre de mots de passe valides: {nbValid}")

    print("\n--- Part Two ---")

    nbValid = 0
    for line in input:
        infos = line.split(" ")
        min, max = map(int, infos[0].split("-"))
        letter = infos[1][0]
        password = infos[2]
        if (password[min-1] == letter) or (password[max-1] == letter):
            if (password[min-1] == letter) and (password[max-1] == letter):
                continue
            else:
                nbValid += 1

    print(f"Nombre de mots de passe valides: {nbValid}")
    
    # break