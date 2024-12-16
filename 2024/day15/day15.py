def deepcopy_dict(d):
    if not isinstance(d, dict):
        return d
    copied_dict = {}
    for key, value in d.items():
        copied_dict[key] = deepcopy_dict(value)
    return copied_dict


def make_move(grid, x, y, symbol, direction):
    directions_map = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    newPosX, newPosY = x+directions_map[direction][0], y+directions_map[direction][1]

    # If the place is free
    if (newPosX, newPosY) not in grid:
        if symbol != "@":
            grid[(newPosX, newPosY)] = symbol
        if (x, y) in grid: 
            grid.pop((x, y))
        return grid, newPosX, newPosY
    
    else:
        # If it's a wall, do nothing
        if grid[(newPosX, newPosY)] == "#":
            return grid, x, y
        
        # If it's a object, tyr to move it
        else:
            newGrid, newX, newY = make_move(grid, newPosX, newPosY, grid[(newPosX, newPosY)], direction)

            # if it didn't move
            if (newX, newY) == (newPosX, newPosY):
                return grid, x, y
            
            else:
                if symbol != "@":
                    newGrid[(newPosX, newPosY)] = symbol
                if (x, y) in newGrid: 
                    newGrid.pop((x, y))
                return grid, newPosX, newPosY
            

def make_big_move(grid, x, y, symbol, direction):
    directions_map = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    newPosX, newPosY = x+directions_map[direction][0], y+directions_map[direction][1]
    initial_grid = {k: v for k, v in grid.items()}

    # print(f"[DEBUG {symbol}] Moving in {direction=} from ({x}, {y}) to ({newPosX}, {newPosY})")

    # If the place is free
    if (newPosX, newPosY) not in grid:
        if symbol != "@":
            grid[(newPosX, newPosY)] = symbol
        if (x, y) in grid: 
            grid.pop((x, y))
        return grid, newPosX, newPosY
    
    else:
        # If it's a wall, do nothing
        if grid[(newPosX, newPosY)] == "#":
            return initial_grid, x, y
        
        # If it's a object, tr to move all its parts
        else:
            # Move left and right blocs
            if direction in ["^", "v"]:
                if grid[(newPosX, newPosY)] == "]":
                    # Move a side
                    newGrid, newX, newY = make_big_move(grid, newPosX, newPosY, "]", direction)
                    if (newX, newY) == (newPosX, newPosY):
                        return initial_grid, x, y
                    # Then the other side
                    newGrid, newX, newY = make_big_move(newGrid, newPosX-1, newPosY, "[", direction)
                    if (newX, newY) == (newPosX-1, newPosY):
                        return initial_grid, x, y

                elif grid[(newPosX, newPosY)] == "[":
                    newGrid, newX, newY = make_big_move(grid, newPosX, newPosY, "[", direction)
                    if (newX, newY) == (newPosX, newPosY):
                        return initial_grid, x, y
                    newGrid, newX, newY = make_big_move(newGrid, newPosX+1, newPosY, "]", direction)
                    if (newX, newY) == (newPosX+1, newPosY):
                        return initial_grid, x, y
                
                # All blocs have moved, the current block can move
                if symbol != "@":
                    newGrid[(newPosX, newPosY)] = symbol
                if (x, y) in newGrid: 
                    newGrid.pop((x, y))
                return grid, newPosX, newPosY
            
            # Just push all the objects
            else:
                newGrid, newX, newY = make_big_move(grid, newPosX, newPosY, grid[(newPosX, newPosY)], direction)
                # if it didn't move
                if (newX, newY) == (newPosX, newPosY):
                    return initial_grid, x, y
                
                else:
                    if symbol != "@":
                        newGrid[(newPosX, newPosY)] = symbol
                    if (x, y) in newGrid: 
                        newGrid.pop((x, y))
                    return grid, newPosX, newPosY


def print_map(obstacle_map, guardX, guardY, maxX, maxY):
    for i in range(maxY):
        for j in range(maxX):
            if ((guardX, guardY) == (j, i)):
                print("@", end="")
            elif (j, i) in obstacle_map:
                print(obstacle_map[(j, i)], end="")
            else:
                print(".", end="")
        print()




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day15/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")


    obstacle_map = {}
    movements = ""

    guardX, guardY = 0, 0
    maxX, maxY = 0, 0
    isMovements = False

    # Parse input
    for i, line in enumerate(data):
        if line == "":
            isMovements = True
        elif (isMovements):
            movements += line
        else:
            maxX, maxY = len(line), i+1
            for j, c in enumerate(line):
                if c == "#":
                    obstacle_map[(j, i)] = "#"
                elif c == "O":
                    obstacle_map[(j, i)] = "O"
                elif c == "@":
                    guardX, guardY = j, i


    for direction in movements:
        obstacle_map, guardX, guardY = make_move(obstacle_map, guardX, guardY, "@", direction)

    # print_map(obstacle_map, maxX, maxY, guardX, guardY)

    sumGPS = 0
    for (x, y) in obstacle_map:
        if obstacle_map[(x, y)] == "O":
            sumGPS += y*100 + x

    print(f"Sum of GPS: {sumGPS}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    obstacle_map = {}
    movements = ""

    guardX, guardY = 0, 0
    maxX, maxY = 0, 0
    isMovements = False

    # Parse input
    for i, line in enumerate(data):
        if line == "":
            isMovements = True
        elif (isMovements):
            movements += line
        else:
            maxX, maxY = len(line)*2, i+1
            for j, c in enumerate(line):
                if c == "#":
                    obstacle_map[(j*2, i)] = "#"
                    obstacle_map[(j*2 + 1, i)] = "#"
                elif c == "O":
                    obstacle_map[(j*2, i)] = "["
                    obstacle_map[(j*2 + 1, i)] = "]"
                elif c == "@":
                    guardX, guardY = j*2, i
                    

    for direction in movements:
        obstacle_map, guardX, guardY = make_big_move(obstacle_map, guardX, guardY, "@", direction)

    # print_map(obstacle_map, guardX, guardY, maxX, maxY)

    sumGPS = 0
    for (x, y) in obstacle_map:
        if obstacle_map[(x, y)] == "[":
            sumGPS += y*100 + x

    print(f"Sum of GPS: {sumGPS}")