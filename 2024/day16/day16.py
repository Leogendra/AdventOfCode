import heapq
from math import inf




def print_grid(obstacles, visited, maxX, maxY):
    for i in range(maxY):
        for j in range(maxX):
            if ((j, i) in obstacles):
                print("#", end="")
            elif ((j, i) in visited):
                print("o", end="")
            else:
                print(" ", end="")
        print()
    print()





for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day16/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    forbiden_movements = {"v": "^", "^": "v", "<": ">", ">": "<"}

    maxX, maxY = len(data[0]), len(data)
    start, end = (1, maxY-2), (maxX-2, 1)
    objects_map = {}

    for i in range(maxY):
        for j in range(maxX):
            if (data[i][j] == "#"):
                objects_map[(j, i)] = "#"

    bestScore = inf
    visited = set()
    queue = [(0, (start, ">"))]
    while queue:
        score, (coords, direction) = heapq.heappop(queue)
        
        if (coords in visited):
            continue

        if (coords == end):
            bestScore = score
            break

        # For all 4 neightbours
        for newX, newY, newDirection in [(0, -1, "^"), (1, 0, ">"), (0, 1, "v"), (-1, 0, "<")]:
            if (newDirection != forbiden_movements[direction]): # If no 180-turn
                new_coords = (coords[0]+newX, coords[1]+newY)
                if (new_coords not in objects_map): # If no wall
                    if (newDirection == direction): # Straight
                        heapq.heappush(queue, (score+1, (new_coords, direction)))
                        visited.add(coords)
                    else: # 90-turn
                        heapq.heappush(queue, (score+1001, (new_coords, newDirection)))


    print(f"Best score: {bestScore}")
    


    
    print("\n\033[93m--- Part Two ---\033[0m")

    # /!\ Keeping the best score

    visited_best_path = set()
    visited_list_global = {}

    queue = [(0, start, ">", [])]
    while queue:
        score, coords, direction, visited_list = heapq.heappop(queue)

        if (coords in visited_list): 
            # This path has already been here
            continue
            
        if ((coords in visited_list_global) and (visited_list_global[coords] < score)):
            # A best path exists
            continue

        visited_list.append(coords)

        if (coords == end):
            if (score == bestScore):
                visited_best_path.update(visited_list)
                bestScore = score
                continue
            else:
                break


        # For all 4 neightbours
        for newX, newY, newDirection in [(0, -1, "^"), (1, 0, ">"), (0, 1, "v"), (-1, 0, "<")]:
            if (newDirection != forbiden_movements[direction]): # If no 180-turn
                new_coords = (coords[0]+newX, coords[1]+newY)
                if (new_coords not in objects_map): # If no wall
                    if (newDirection == direction): # Straight
                        heapq.heappush(queue, (score+1, new_coords, direction, [v for v in visited_list]))
                        visited_list_global[coords] = score+1000
                    else: # 90-turn
                        heapq.heappush(queue, (score+1001, new_coords, newDirection, [v for v in visited_list]))


    print(f"Number of best seats: {len(visited_best_path)}")