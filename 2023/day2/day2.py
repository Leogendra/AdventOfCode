for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day2/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    contraintes = {"red":12, "green":13, "blue":14}

    somme = 0
    power = 0

    for line in data:
        cubes = {"red":0, "green":0, "blue":0}
        _game, _values = line.split(":")
        gameId = int(_game.split(" ")[1])
        values = [val.strip(';,') for val in _values.split(" ") if val != ""]

        for i in range(len(values), 0, -2):
            couleur = values[i-1]
            valeur = int(values[i-2])
            cubes[couleur] = max(valeur, cubes[couleur])

        validGame = True
        power += cubes["red"] * cubes["green"] * cubes["blue"]
        for couleur in cubes.keys():
            if cubes[couleur] > contraintes[couleur]:
                validGame = False

        if validGame:
            somme += gameId


    print(f"La somme des ID des game possible est {somme}")




    print("\n\033[93m--- Part Two ---\033[0m")

    print(f"La somme des power des game est {power}")


    # break