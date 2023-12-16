def get_voisins(x, y, maxX, maxY):
    voisins = []
    for i, j, dir in [(-1,0,"N"), (0,-1,"W"), (0,1,"E"), (1,0,"S")]:
        if y+i < 0 or y+i >= maxY:
            continue
        elif x+j < 0 or x+j >= maxX:
            continue
        voisins.append([y+i, x+j, dir])
    return voisins



def deja_passe(x, y, direction):
    for pipe in direction:
        if (x == pipe[1]) and (y == pipe[0]):
            return True
    return False



def print_board(data, direction_1, direction_2, write=False):
    if write:
        with open("2023/day10/board.txt", "w") as f:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    printed = False
                    for pipe in direction_1:
                        if (i == pipe[0]) and (j == pipe[1]):
                            f.write("#")
                            printed = True
                            break

                    if not(printed):
                        for pipe in direction_2:
                            if (i == pipe[0]) and (j == pipe[1]):
                                f.write("#")
                                printed = True
                                break

                    if not(printed):
                        f.write(data[i][j])

                f.write("\n")

    for i in range(len(data)):
        for j in range(len(data[i])):
            printed = False
            for pipe in direction_1:
                if (i == pipe[0]) and (j == pipe[1]):
                    print("\033[91m"+data[i][j]+"\033[0m", end="")
                    printed = True
                    break

            if not(printed):
                for pipe in direction_2:
                    if (i == pipe[0]) and (j == pipe[1]):
                        print("\033[92m"+data[i][j]+"\033[0m", end="")
                        printed = True
                        break

            if not(printed):
                print(data[i][j], end="")

        print()
    print()




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day10/{fichier}.txt", "r") if line.strip() != ""]


    pipe_directions = {
        "N": ["|", "7", "F"],
        "W": ["-", "F", "L"],
        "E": ["-", "7", "J"],
        "S": ["|", "J", "L"]
    }    
    pipe_from = {
        "N": ["|", "L", "J"],
        "W": ["-", "7", "J"],
        "E": ["-", "L", "F"],
        "S": ["|", "7", "F"]
    }

    maxX = len(data[0])
    maxY = len(data)

    print("\033[93m--- Part One ---\033[0m")


    start = [0,0,-1]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                start = [i, j, 0]
                break
        if start[2] != -1:
            break

    start_voisins = get_voisins(start[1], start[0], maxX, maxY)

    direction_1 = []
    direction_2 = []
    for y, x, dir in start_voisins:
        if data[y][x] in pipe_directions[dir]:
            if direction_1 == []:
                direction_1.append([y, x, 1])
            else:
                direction_2.append([y, x, 1])
                break

    # arrivé au bout du tuyau
    arriveAuBout = False
    while not(arriveAuBout):
        last_1 = direction_1[-1]
        last_2 = direction_2[-1]

        for lastNum, coord in enumerate([last_1, last_2]):
        
            voisins = get_voisins(coord[1], coord[0], maxX, maxY)
        
            for y, x, dir in voisins:
        
                # check si le tuyau suivant peut nous recevoir
                if (data[y][x] in pipe_directions[dir]):

                    # check si on peut aller dans le tuyau suivant
                    if data[coord[0]][coord[1]] in pipe_from[dir]:
                        if lastNum == 0:
                            # check si deja passé par ce tuyau
                            if deja_passe(x, y, direction_1):
                                continue
                            direction_1.append([y, x, coord[2]+1])
                        else:
                            if deja_passe(x, y, direction_2):
                                continue
                            direction_2.append([y, x, coord[2]+1])
                        break

            # print_board(data, direction_1, direction_2)
            # print(f"Direction 1 : {direction_1}")
            # print(f"Direction 2 : {direction_2}")
            # input()

            if (direction_1[-1][0] == direction_2[-1][0]) and (direction_1[-1][1] == direction_2[-1][1]):
                arriveAuBout = True
                break

    # print_board(data, direction_1, direction_2)

    print(f"Part One : {direction_1[-1][2]}")
    





    print("\n\033[93m--- Part Two ---\033[0m")

    accepted_directions = {
        "|": ["N", "S"],
        "-": ["W", "E"],
        "7": ["W", "S"],
        "J": ["W", "N"],
        "L": ["E", "N"],
        "F": ["E", "S"]
    }

    # écartement de la grille
    maxX = maxX*2 - 1
    maxY = maxY*2 - 1
    new_grid = [["." for _ in range(maxX)] for _ in range(maxY)]

    # Zoom sur la grille
    for i in range(len(data)):
        for j in range(len(data[i])):
            new_grid[i*2][j*2] = data[i][j]


    # Racordage des pipes dans les trous
    for i in range(len(data)):
        for j in range(len(data[i])):
            currentPipe = new_grid[i*2][j*2]
            if currentPipe not in accepted_directions.keys():
                continue
            acceptedDirs = accepted_directions[currentPipe]
            for y, x, dir in get_voisins(j*2, i*2, maxX, maxY):
                if dir in acceptedDirs:
                    new_grid[y][x] = "|" if dir in ["N", "S"] else "-"

    ###########################
    #     Partie clochard     #
    ###########################
                    
    start = [0,0,-1]
    for i in range(maxY):
        for j in range(maxX):
            if new_grid[i][j] == "S":
                start = [i, j, 0]
                break
        if start[2] != -1:
            break

    start_voisins = get_voisins(start[1], start[0], maxX, maxY)

    # On recalcule le pipe     
    direction_1 = []
    direction_2 = []
    for y, x, dir in start_voisins:
        if new_grid[y][x] in pipe_directions[dir]:
            if direction_1 == []:
                direction_1.append([y, x, 1])
            else:
                direction_2.append([y, x, 1])
                break

    # arrivé au bout du tuyau
    arriveAuBout = False
    while not(arriveAuBout):
        last_1 = direction_1[-1]
        last_2 = direction_2[-1]

        for lastNum, coord in enumerate([last_1, last_2]):
        
            voisins = get_voisins(coord[1], coord[0], maxX, maxY)
        
            for y, x, dir in voisins:
        
                # check si le tuyau suivant peut nous recevoir
                if (new_grid[y][x] in pipe_directions[dir]):

                    # check si on peut aller dans le tuyau suivant
                    if new_grid[coord[0]][coord[1]] in pipe_from[dir]:
                        if lastNum == 0:
                            # check si deja passé par ce tuyau
                            if deja_passe(x, y, direction_1):
                                continue
                            direction_1.append([y, x, coord[2]+1])
                        else:
                            if deja_passe(x, y, direction_2):
                                continue
                            direction_2.append([y, x, coord[2]+1])
                        break

            if (direction_1[-1][0] == direction_2[-1][0]) and (direction_1[-1][1] == direction_2[-1][1]):
                arriveAuBout = True
                break

    queue = []
    flooded = [(start[0], start[1])]

    # On ajoute le pipe lui meme, clodo mais ça marche
    for dir1 in direction_1:
        flooded.append((dir1[0], dir1[1]))
    for dir2 in direction_2:
        flooded.append((dir2[0], dir2[1]))


    # remplir la queue avec les bords
    for i in range(maxY):
        if (i, 0) not in flooded:
            queue.append((i, 0))
        if (i, maxX-1) not in flooded:
            queue.append((i, maxX-1))

    for j in range(maxX):
        if (0, j) not in flooded:
            queue.append((0, j))
        if (maxY-1, j) not in flooded:
            queue.append((maxY-1, j))

    # Flood du réseau
    while len(queue) > 0:
        elem = queue.pop()
        flooded.append(elem)
        for y, x, dir in get_voisins(elem[1], elem[0], maxX, maxY):
            if ((y, x) not in flooded) and ((y, x) not in queue):
                queue.append((y, x))

    # Maintenant on compte les zones qui sont pas flood (que les cases paires !)
    zoneFermee = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if ((i*2, j*2) not in flooded):
                zoneFermee += 1
        #         print(f"\033[91m{data[i][j]}\033[0m", end="")
        #     else:
        #         print(data[i][j], end="")
        # print()

    print(f"Part One : {zoneFermee}")

    # break
