for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2016/day8/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    width, height = [7, 3] if (fichier == "test") else [50, 6]
    grid = {}
    for line in data:
        if line.startswith("rect"):
            dimA, dimB = list(map(int, line.split()[1].split("x")))
            for x in range(dimA):
                for y in range(dimB):
                    grid[(x, y)] = "#"

        else:
            rotateA = int(line.split()[2].split("=")[1])
            byB = int(line.split()[-1])
            toUpdate = []
            grid_keys = list(grid.keys())


            if line.startswith("rotate row"):
                for coords in grid_keys:
                    if coords[1] == rotateA:
                        toUpdate.append(coords)
                        grid.pop(coords)
                for coords in toUpdate:
                    grid[(coords[0]+byB)%width, coords[1]] = "#"

            else: # column
                for coords in grid_keys:
                    if coords[0] == rotateA:
                        toUpdate.append(coords)
                        grid.pop(coords)
                for coords in toUpdate:
                    grid[(coords[0], (coords[1]+byB)%height)] = "#"


    print(f"Number of pixels lit: {len(grid)}")


    

    print("\n\033[93m--- Part Two ---\033[0m")

    for y in range(height):
        for x in range(width):
            print(grid.get((x, y), "."), end="")
        print()