import heapq
from math import inf




def print_grid(obstacles, visited, maxX, maxY):
    print("#"*(maxX+2))
    for i in range(maxY):
        print("#", end="")
        for j in range(maxX):
            if ((j, i) in obstacles):
                print("#", end="")
            elif ((j, i) in visited):
                print("o", end="")
            else:
                print(" ", end="")
        print("#")
    print("#"*(maxX+2))




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day18/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    objects_map = {}
    maxFallenBytes = 1024 if fichier == "input" else 12
    for i, line in enumerate(data):
        if (i == maxFallenBytes):
            break
        x, y = [int(nb.strip()) for nb in line.split(",")]
        objects_map[(x, y)] = "#"


    (maxX, maxY) = (71, 71) if fichier == "input" else (7, 7)
    start, end = (0, 0), (maxX-1, maxY-1)
    # print_grid(objects_map, set(), maxX, maxY)

    minSteps = inf
    visited = set()
    queue = [(0, (start))]
    while queue:
        steps, (coords) = heapq.heappop(queue)

        if (coords == end):
            minSteps = steps
            break
        
        if (coords in visited):
            continue

        # For all 4 neightbours
        for newX, newY in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            new_coords = (coords[0]+newX, coords[1]+newY)
            if ((new_coords[0] >= 0) and (new_coords[0] < maxX) and (new_coords[1] >= 0) and (new_coords[1] < maxY)):
                if (new_coords not in objects_map):
                    heapq.heappush(queue, (steps+1, (new_coords)))
                    visited.add(coords)

    print(f"Minimum steps: {minSteps}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    blocableByte = (0, 0)
    maxFallenBytes = 1024 if fichier == "input" else 12
    (maxX, maxY) = (71, 71) if fichier == "input" else (7, 7)
    start, end = (0, 0), (maxX-1, maxY-1)
    trapped = False

    while not(trapped):
        maxFallenBytes += 1
        objects_map = {}
        for i, line in enumerate(data):
            if (i == maxFallenBytes):
                break
            x, y = [int(nb.strip()) for nb in line.split(",")]
            objects_map[(x, y)] = "#"

        steps = 0
        highBoundBlocs = maxX*maxY-len(objects_map)
        visited = set()
        queue = [(0, (start))]
        found = False
        while queue:
            steps, (coords) = heapq.heappop(queue)

            if (coords == end):
                found = True
                break
            
            if (coords in visited):
                continue

            # For all 4 neightbours
            for newX, newY in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_coords = (coords[0]+newX, coords[1]+newY)
                if ((new_coords[0] >= 0) and (new_coords[0] < maxX) and (new_coords[1] >= 0) and (new_coords[1] < maxY)):
                    if (new_coords not in objects_map):
                        heapq.heappush(queue, (steps+1, (new_coords)))
                        visited.add(coords)
        
        if not(found):
            trapped = True

    print(f"First blocable byte: {data[maxFallenBytes-1]}")