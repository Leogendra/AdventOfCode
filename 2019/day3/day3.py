for fichier in ["test", "input", "input2"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    paths = [line.strip() for line in open(f"2019/day3/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")
    
    grid = {}
    intersections = []

    for path_number, path in enumerate(paths):
        x, y = 0, 0
        for instruction in path.split(","):
            direction = instruction[0]
            distance = int(instruction[1:])
            for i in range(distance):
                if direction == "U":
                    y += 1
                elif direction == "D":
                    y -= 1
                elif direction == "R":
                    x += 1
                elif direction == "L":
                    x -= 1
                if (x, y) not in grid:
                    grid[(x, y)] = path_number+1
                elif grid[(x, y)] != path_number+1:
                    intersections.append((x, y))
                    grid[(x, y)] = "X"

    # On cherche l'intersection la plus proche de (0, 0)
    plusProche = (99999, 99999)
    for intersection in intersections:
        if abs(intersection[0]) + abs(intersection[1]) < abs(plusProche[0]) + abs(plusProche[1]):
            plusProche = intersection

    print(f"La distance de l'intersection la plus proche de (0, 0) est {abs(plusProche[0]) + abs(plusProche[1])}")
            
    # print de la grid
    # for y in range(19, -1, -1):
    #     for x in range(20):
    #         if (x, y) in grid:
    #             print(grid[(x, y)], end="")
    #         else:
    #             print(".", end="")
    #     print()





    print("\n\033[93m--- Part Two ---\033[0m")

    steps = {}

    for path_number, path in enumerate(paths):
        x, y, step = 0, 0, 0
        for instruction in path.split(","):
            direction = instruction[0]
            distance = int(instruction[1:])
            for i in range(distance):
                step += 1
                if direction == "U":
                    y += 1
                elif direction == "D":
                    y -= 1
                elif direction == "R":
                    x += 1
                elif direction == "L":
                    x -= 1

                if (x, y) in intersections:
                    if (x, y) not in steps:
                        steps[(x, y)] = step
                    else:
                        steps[(x, y)] += step

    shortest_steps = 99999
    for coord, steps_to_go in steps.items():
        if steps_to_go < shortest_steps:
            shortest_steps = steps_to_go

    print(f"Chemin le plus court pour rejoindre l'intersection {shortest_steps}")