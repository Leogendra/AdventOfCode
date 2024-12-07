directions_coords = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
directions_next = {"^": ">", ">": "v", "v": "<", "<": "^"}

def count_guard_move(grid, guard_coords, maxX, maxY):
    positions_visited = {}
    block_hit = {}
    guardX, guardY, guardDirection = guard_coords
    inLoop = False

    while not(inLoop) and ((guardX >= 0) and (guardX < maxX) and (guardY >= 0) and (guardY < maxY)):
        guardCoordsDirection = directions_coords[guardDirection]
        if ((guardX, guardY) in grid.keys()): # if the current position is a block, go back and turn
            if ((guardX, guardY) in block_hit.keys()): # if the block has been hit: check direction
                if (guardDirection in block_hit[(guardX, guardY)]): # if we already hit this block in that direction: loop
                    inLoop = True
                    break
                else:
                    block_hit[(guardX, guardY)].append(guardDirection)

            else: # The block has not been hit
                block_hit[(guardX, guardY)] = [guardDirection]
            guardX -= guardCoordsDirection[0]
            guardY -= guardCoordsDirection[1]
            guardDirection = directions_next[guardDirection]
        else:
            positions_visited[(guardX, guardY)] = True
            guardX += guardCoordsDirection[0]
            guardY += guardCoordsDirection[1]

        # print_grid(grid, [guardX, guardY, guardDirection], maxX, maxY)
        # input()

    if (inLoop):
        return -1
    else:
        return len(positions_visited.keys())
        

def print_grid(grid, guard_coords, maxX, maxY):
    for i in range(maxY):
        for j in range(maxX):
            if (i == guard_coords[1]) and (j == guard_coords[0]):
                print(guard_coords[2], end="")
            elif (j, i) in grid:
                print("#", end="")
            else:
                print(".", end="")
        print()


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day6/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    directions_coords = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    directions_next = {"^": ">", ">": "v", "v": "<", "<": "^"}
    maxX, maxY = len(data[0]), len(data)

    obstacle_map = {}
    for i in range(maxY):
        for j in range(maxX):
            if data[i][j] == "#":
                obstacle_map[(j, i)] = True
            elif data[i][j] != ".":
                initial_guard_state = [j, i, data[i][j]]

    print(count_guard_move(obstacle_map, initial_guard_state, maxX, maxY))



    
    print("\n\033[93m--- Part Two ---\033[0m")

    nbObstructionPosition = 0
    for i in range(maxY):
        for j in range(maxX):
            if ((j, i) != (initial_guard_state[0], initial_guard_state[1])) and ((j, i) not in obstacle_map.keys()):
                obstacle_map[(j, i)] = True
                if (count_guard_move(obstacle_map, initial_guard_state, maxX, maxY) == -1):
                    nbObstructionPosition += 1
                obstacle_map.pop((j, i))

    print(nbObstructionPosition)
