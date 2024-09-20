for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2015/day6/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in data:
        instruction = instruction.split()
        action = "off"
        if instruction[0] == "toggle":
            x1, y1 = instruction[1].split(",")
            x2, y2 = instruction[3].split(",")
            action = "toogle"
        else:
            x1, y1 = instruction[2].split(",")
            x2, y2 = instruction[4].split(",")
            if instruction[1] == "on":
                action = "on"

        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if action == "on":
                    grid[y][x] = 1
                elif action == "off":
                    grid[y][x] = 0
                else:
                    grid[y][x] = 1 - grid[y][x]

    print(f"Number of lit lights: {sum(sum(light for light in row) for row in grid)}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in data:
        instruction = instruction.split()
        action = "off"
        if instruction[0] == "toggle":
            x1, y1 = instruction[1].split(",")
            x2, y2 = instruction[3].split(",")
            action = "toogle"
        else:
            x1, y1 = instruction[2].split(",")
            x2, y2 = instruction[4].split(",")
            if instruction[1] == "on":
                action = "on"

        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if action == "on":
                    grid[y][x] += 1
                elif action == "off":
                    grid[y][x] = max(0, grid[y][x] - 1)
                else:
                    grid[y][x] += 2

    print(f"Number of lit lights: {sum(sum(light for light in row) for row in grid)}")