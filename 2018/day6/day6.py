for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2018/day6/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    grid = {}
    for i, line in enumerate(data):
        x, y = map(int, line.split(", "))
        grid[(x, y)] = str(i)

    next_pile = [coords for coords in grid.keys()]
    maxCycles = 1000
    cycles = 0
    while cycles < maxCycles:
        cycles += 1
        current_pile = [coords for coords in next_pile]
        next_pile = []
        indicePile = 0
        while indicePile < len(current_pile):
            
            x, y = current_pile[indicePile]
            indicePile += 1
            tmpLetter = f"{grid[(x, y)]}-"

            # check des 4 voisins
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                voisin = (x+dx, y+dy)
                if (voisin not in grid.keys()):
                    next_pile.append(voisin)
                    grid[voisin] = tmpLetter
                elif (str(grid[voisin])[-1] == '-') and (str(grid[voisin]) != tmpLetter):
                    grid[voisin] = '.'
                
        # On passe le tmp en lettre
        for coords in next_pile:
            grid[coords] = str(grid[coords]).strip('-')

        # On print la grid pour debug
        # for y in range(10):
        #     for x in range(10):
        #         print(grid.get((x, y), " "), end="")
        #     print()
        # print()
        # input()

    # On regarde les lettres infinies
    locations_infinite = set()
    for coords in next_pile:
        locations_infinite.add(str(grid[coords]).strip('-'))

    # On compte les lettres
    letter_count = {}
    for coords, letter in grid.items():
        letter_count[letter] = letter_count.get(letter, 0) + 1

    for letter in locations_infinite:
        letter_count.pop(letter, None)

    print(f"Plus grande aire finie : {max(letter_count.values())}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    emeteurs = []
    grid = []
    for i, line in enumerate(data):
        x, y = map(int, line.split(", "))
        emeteurs.append((x, y))

    maxSum = 32 if (fichier == "test") else 10000
    maxDistance = 10 if (fichier == "test") else 1000

    for x in range(maxDistance):
        for y in range(maxDistance):
            distanceTotale = 0
            for emeteur in emeteurs:
                emX, emY = emeteur
                distanceTotale += abs(emX - x) + abs(emY - y)

            if distanceTotale < maxSum:
                grid.append((x, y))

    print(f"Taille de la zone : {len(grid)}")
    

