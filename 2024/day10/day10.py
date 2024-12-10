for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day10/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    maxX, maxY = len(data[0]), len(data)

    scoreTrailheads = 0
    queue = []
    for i in range(maxY):
        for j in range(maxX):
            if data[i][j] == "0":
                queue.append((j, i, 0))
                trailheadEnds = {}

                while queue:
                    pathX, pathY, pathValue = queue.pop(0)
                    if pathValue == 9:
                        trailheadEnds[(pathX, pathY)] = True
                        continue
                    else:
                        for nX, nY in [(pathX+1, pathY), (pathX-1, pathY), (pathX, pathY+1), (pathX, pathY-1)]:
                            if (nX >= 0) and (nX < maxX) and (nY >= 0) and (nY < maxY):
                                if (data[nY][nX] == str(pathValue+1)):
                                    queue.append((nX, nY, pathValue+1))

                scoreTrailheads += len(trailheadEnds)

    print(f"sum of trailheads scores: {scoreTrailheads}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    queue = []
    for i in range(maxY):
        for j in range(maxX):
            if data[i][j] == "0":
                queue.append((j, i, 0))

    totalTrailheads = 0
    while queue:
        pathX, pathY, pathValue = queue.pop(0)
        if pathValue == 9:
            totalTrailheads += 1
            continue
        else:
            for nX, nY in [(pathX+1, pathY), (pathX-1, pathY), (pathX, pathY+1), (pathX, pathY-1)]:
                if (nX >= 0) and (nX < maxX) and (nY >= 0) and (nY < maxY):
                    if (data[nY][nX] == str(pathValue+1)):
                        queue.append((nX, nY, pathValue+1))

    print(f"total number of trailheads: {totalTrailheads}")
    

