def tilt_direction(rocks, direction):

    grid = [list(row) for row in rocks]
    indice = 0
    while indice < (len(grid) * len(grid[0])):
        i, j = divmod(indice, len(grid[0]))
        block = grid[i][j]
        if block == "O":
            steps = 1
            while (
                    (i + steps*direction[0]) < len(grid)
                ) and (
                    (i + steps*direction[0]) >= 0
                ) and (
                    (j + steps*direction[1]) < len(grid[0])
                ) and (
                    (j + steps*direction[1]) >= 0
                ) and (
                    grid[i + steps*direction[0]][j + steps*direction[1]] == '.' # On est bloqué si c'est un O ou un #
                ):
                steps += 1
            if steps > 1:
                grid[i + (steps-1)*direction[0]][j + (steps-1)*direction[1]] = "O"
                grid[i][j] = "."

            # if indice > len(grid[0]):
            #     for y in range(min(30, len(grid))):
            #         for x in range(len(grid[0])):
            #             if y == i and x == j:
            #                 print("\033[91m" + grid[y][x] + "\033[0m", end="")
            #             else:
            #                 print(grid[y][x], end="")
            #         print()
            #     input()
        indice += 1
    
    return ["".join(line) for line in grid]



for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day14/{fichier}.txt", "r") if line.strip() != ""]

    directions = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }

    print("\033[93m--- Part One ---\033[0m")


    tilt = "N"
    tilted_data = tilt_direction(data, directions[tilt])

    sommeCharge = 0
    for i in range(len(tilted_data)):
        for j in range(len(tilted_data[i])):
            if tilted_data[i][j] == "O":
                sommeCharge += len(tilted_data) - i

    print(f"Somme de la charge: {sommeCharge}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    #####################
    #   DOES NOT WORK   #
    #####################
    
    cycle = 1
    numberOfCycles = 4 * 1
    tilts = ["N", "W", "S", "E"]
    while cycle <= numberOfCycles:
        tilt = tilts[cycle%4]
        # TODO: fix la fonction pour tilt au S et E (ordre des blocs)
        tilted_data = tilt_direction(tilted_data, directions[tilt])
        cycle += 1

        print(f"\nCycle {cycle} ({tilt})")
        for line in tilted_data:
            print(line)


    sommeCharge = 0
    for i in range(len(tilted_data)):
        for j in range(len(tilted_data[i])):
            if tilted_data[i][j] == "O":
                sommeCharge += len(tilted_data) - i

    print(f"Somme de la charge: {sommeCharge}")