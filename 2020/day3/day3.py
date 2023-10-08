for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    trees = [line.strip() for line in open(f"2020/day3/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    right = 3
    down = 1
    forestLenght = len(trees[0])

    treesEncounter = 0
    x, y = 0, 0

    while y < len(trees):
        if trees[y][x % forestLenght] == "#":
            treesEncounter += 1
        x += right
        y += down

    print(treesEncounter)

    print("\n\033[93m--- Part Two ---\033[0m")

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    maxTreesEncounter = 1

    for right, down in slopes:
        treesEncounter = 0
        x, y = 0, 0

        while y < len(trees):
            if trees[y][x % forestLenght] == "#":
                treesEncounter += 1
            x += right
            y += down

        maxTreesEncounter *= treesEncounter

    print(maxTreesEncounter)
