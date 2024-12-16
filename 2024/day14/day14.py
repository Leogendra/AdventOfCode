for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day14/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    robots_list = []
    for line in data:
        robots_list.append([[int(nb) for nb in eq.split("=")[1].split(",")] for eq in line.split(" ")])


    maxX, maxY = (11, 7) if (fichier == "test") else (101, 103)
    midX, midY = maxX//2, maxY//2
    numberOfSeconds = 100

    for _ in range(numberOfSeconds):
        for i in range(len(robots_list)):
            [robotX, robotY], [speedX, speedY] = robots_list[i]
            robots_list[i][0] = [(robotX+speedX)%maxX, (robotY+speedY)%maxY]


    cadrants_list = [0, 0, 0, 0]
    for robot in robots_list:
        x, y = robot[0]
        if (x < midX and y < midY):
            cadrants_list[0] += 1
        elif (x > midX and y < midY):
            cadrants_list[1] += 1
        elif (x < midX and y > midY):
            cadrants_list[2] += 1
        elif (x > midX and y > midY):
            cadrants_list[3] += 1

    safetyFactor = cadrants_list[0] * cadrants_list[1] * cadrants_list[2] * cadrants_list[3]


    print(f"Safety factor: {safetyFactor}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    robots_list = []
    for line in data:
        robots_list.append([[int(nb) for nb in eq.split("=")[1].split(",")] for eq in line.split(" ")])


    maxX, maxY = (11, 7) if (fichier == "test") else (101, 103)
    midX, midY = maxX//2, maxY//2
    quitMsg = ""
    seconds = 0

    while (quitMsg == ""):
        seconds += 1

        # move the robots
        for i in range(len(robots_list)):
            [robotX, robotY], [speedX, speedY] = robots_list[i]
            robots_list[i][0] = [(robotX+speedX)%maxX, (robotY+speedY)%maxY]

        # Locate the robots
        robots_positions = {}
        interact = False
        for robot in robots_list:
            x, y = robot[0]
            if (x, y) in robots_positions:
                interact = True
                break
            robots_positions[(x, y)] = 1

        # print the robots
        if not(interact):
            print(f"Second {seconds}")
            for i in range(maxY):
                line = ""
                for j in range(maxX):
                    if (j, i) in robots_positions:
                        line += str(robots_positions[(j, i)])
                    else:
                        line += "."
                print(line)

            quitMsg = input("")