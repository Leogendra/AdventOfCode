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

    print(f"Start : {start}")
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

    print_board(data, direction_1, direction_2)

    print(f"Part One : {direction_1[-1][2]}")
    
    print("\n\033[93m--- Part Two ---\033[0m")
    

    # break
