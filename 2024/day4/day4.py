def check_four_neightbours_xmas(grid, maxX, maxY, x, y):
    counter = 0
    # left to right
    if ((x+3) < maxX):
        word = f"{grid[y][x]}{grid[y][x+1]}{grid[y][x+2]}{grid[y][x+3]}"
        if (word in ["XMAS", "SAMX"]):
            counter += 1

    # up to bottom
    if ((y+3) < maxY):
        word = f"{grid[y][x]}{grid[y+1][x]}{grid[y+2][x]}{grid[y+3][x]}"
        if (word in ["XMAS", "SAMX"]):
            counter += 1

    # diagonal left to right
    if ((x+3) < maxX and (y+3) < maxY):
        word = f"{grid[y][x]}{grid[y+1][x+1]}{grid[y+2][x+2]}{grid[y+3][x+3]}"
        if (word in ["XMAS", "SAMX"]):
            counter += 1

    # diagonal right to left
    if ((x-3) >= 0 and (y+3) < maxY):
        word = f"{grid[y][x]}{grid[y+1][x-1]}{grid[y+2][x-2]}{grid[y+3][x-3]}"
        if (word in ["XMAS", "SAMX"]):
            counter += 1

    return counter


def check_x_mas(grid, maxX, maxY, x, y):
    if (((x-1) >= 0) and ((x+1) < maxX) and ((y-1) >= 0) and ((y+1) < maxY)):
        word1 = f"{grid[y-1][x-1]}{grid[y][x]}{grid[y+1][x+1]}"
        word2 = f"{grid[y-1][x+1]}{grid[y][x]}{grid[y+1][x-1]}"
        if ((word1 in ["MAS", "SAM"]) and (word2 in ["MAS", "SAM"])):
            return 1

    return 0




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day4/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    height = len(data)
    widht = len(data[0])

    cpt = 0
    for i in range(height):
        for j in range(widht):
            if (data[i][j] in ["X", "S"]):
                cpt += check_four_neightbours_xmas(data, widht, height, j, i)

    print(cpt)



    
    print("\n\033[93m--- Part Two ---\033[0m")

    cpt = 0
    for i in range(height):
        for j in range(widht):
            if (data[i][j] == "A"):
                cpt += check_x_mas(data, widht, height, j, i)

    print(cpt)