for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    directions = [line.strip() for line in open(f"2015/day3/{fichier}.txt", "r")][0]

    print("--- Part One ---")

    position = [0, 0]
    history = [(0, 0)]

    for dir in directions:
        if dir == ">":
            position[0] += 1
        if dir == "<":
            position[0] -= 1
        if dir == "^":
            position[1] += 1
        if dir == "v":
            position[1] -= 1

        if not((position[0],position[1]) in history):
            history.append((position[0],position[1]))
    
    print(len(history))


    print("\n--- Part Two ---")

    position_santa = [0, 0]
    position_robot = [0, 0]
    history = [[0, 0]]

    for i, dir in enumerate(directions):
        if i%2 == 0:
            if dir == ">":
                position_santa[0] += 1
            if dir == "<":
                position_santa[0] -= 1
            if dir == "^":
                position_santa[1] += 1
            if dir == "v":
                position_santa[1] -= 1

            if not(position_santa in history):
                history.append([position_santa[0], position_santa[1]])
        else:
            if dir == ">":
                position_robot[0] += 1
            if dir == "<":
                position_robot[0] -= 1
            if dir == "^":
                position_robot[1] += 1
            if dir == "v":
                position_robot[1] -= 1

            if not(position_robot in history):
                history.append([position_robot[0], position_robot[1]])
    
    print(len(history))

    # code