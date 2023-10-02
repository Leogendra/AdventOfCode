for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    square_goal = int([line.strip() for line in open(f"2017/day3/{fichier}.txt", "r")][0])

    print("\033[93m--- Part One ---\033[0m")

    square_size = 1
    distance_from_center = 0

    while square_size*square_size < square_goal:
        square_size += 2
        distance_from_center += 1

    found = False
    mid = (square_size + 1) // 2
    starting_point = (square_size-2)**2

    print(f"starting_point : {starting_point}")

    position = square_goal - starting_point + 1

    step_in_sides = (position % (square_size - 1))
    if step_in_sides == 0:
        step_in_sides = square_size - 1
    steps = distance_from_center + abs(step_in_sides - mid)
    # print(f"abs(step_in_sides - mid) : {abs(step_in_sides - mid)}\nPosition : {position}, Position + starting_point : {starting_point + (position - 1)}, steps : {steps}")

    if square_size*square_size != square_goal:
        print(f"Number of steps : {steps}")
    else:
        print(f"Number of steps (edge) : {square_size - 1}")






    print("\n\033[93m--- Part Two ---\033[0m")

    grid = {(0, 0): 1}
    indice = 1
    result = 1

    x, y = 0, 0
    direction = 0   # 0: droite, 1: haut, 2: gauche, 3: bas
    step = 1
    
    while result <= square_goal:

        if direction == 0:
            x += 1
        elif direction == 1:
            y += 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y -= 1

        # Passage à la prochaine direction
        if indice % step == 0:
            direction = (direction + 1) % 4
            if direction == 0 or direction == 2:
                step += 1

        indice += 1

        result = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (x+i, y+j) in grid.keys():
                    result += grid[(x+i, y+j)]

        grid[(x, y)] = result


    print("First value larger than the input :", result)