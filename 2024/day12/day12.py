def get_direct_neighbours(coords, maxX, maxY):
    x, y = coords
    neighbours = []
    if x > 0:
        neighbours.append((x-1, y))
    if x < maxX-1:
        neighbours.append((x+1, y))
    if y > 0:
        neighbours.append((x, y-1))
    if y < maxY-1:
        neighbours.append((x, y+1))
    return neighbours




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day12/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    maxX, maxY = len(data[0]), len(data)

    visitedPlots = set()
    totalPrice = 0
    for i in range(maxY):
        for j in range(maxX):
            if (j, i) in visitedPlots:
                continue
            visitedPlots.add((j, i))
            currentPlant = data[i][j]
            currentRegion = {(j, i)}
            currentArea = 1
            currentPerimeter = 4
            queueToVisit = [(j, i)]
            while queueToVisit:
                currentPlot = queueToVisit.pop()
                neightbours = get_direct_neighbours(currentPlot, maxX, maxY)

                for neighbour in neightbours:
                    if (neighbour in visitedPlots):
                        continue

                    neighbourPlant = data[neighbour[1]][neighbour[0]]
                    if (neighbourPlant != currentPlant):
                        continue

                    currentArea += 1
                    currentPerimeter += 2 - 2*sum(1 for n in get_direct_neighbours(neighbour, maxX, maxY) if ((n != currentPlot) and (n in currentRegion)))

                    visitedPlots.add(neighbour)
                    currentRegion.add(neighbour)
                    queueToVisit.append(neighbour)


            totalPrice += currentArea * currentPerimeter


    print(f"Total price: {totalPrice}")


    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    """
    # shitty code that doesn't work
    
    visitedPlots = set()
    totalPrice = 0
    for i in range(maxY):
        for j in range(maxX):
            if (j, i) in visitedPlots:
                continue
            visitedPlots.add((j, i))
            currentPlant = data[i][j]
            currentRegion = {(j, i)}
            currentArea = 1
            currentSides = 0
            queueToVisit = [(j, i)]
            while queueToVisit:
                currentPlot = queueToVisit.pop()
                # print(f"{currentPlot=}")
                neightbours = get_direct_neighbours(currentPlot, maxX, maxY)
                for neighbour in neightbours:
                    if (neighbour in visitedPlots):
                        continue

                    neighbourPlant = data[neighbour[1]][neighbour[0]]
                    if (neighbourPlant != currentPlant):
                        continue

                    currentArea += 1
                    nbNeightbours = sum(1 for n in get_direct_neighbours(neighbour, maxX, maxY) if ((n != currentPlot) and (n in currentRegion)))

                    if (nbNeightbours == 0):
                        continue

                    if (nbNeightbours == 1) or (nbNeightbours == 2):
                        neightboursNeightbour = [n for n in get_direct_neighbours(neighbour, maxX, maxY) if (n in currentRegion)]

                        if (nbNeightbours == 1):
                            neightbourNeightbour = neightboursNeightbour[0]
                            if ((neightbourNeightbour[0] == currentPlot[0]) and ((neightbourNeightbour[1] == currentPlot[1]+2) or (neightbourNeightbour[1] == currentPlot[1]-2))) or ((neightbourNeightbour[1] == currentPlot[1]) and ((neightbourNeightbour[0] == currentPlot[0]+2) or (neightbourNeightbour[0] == currentPlot[0]-2))): 
                                # neighbour is in front
                                currentSides -= 4
                            else:
                                # neightbour is on the side
                                currentSides -= 2

                        if (nbNeightbours == 2):

                            for nN in neightboursNeightbour:
                                nbNeightboursNeightbour = sum(1 for n in get_direct_neighbours(nN, maxX, maxY) if ((n != neighbour) and (n in currentRegion)))
                                if nN in currentRegion:
                                    currentPerimeter -= 1
                                    break

                    if (nbNeightbours == 3):
                        currentSides -= 4


                    # print(f"validNeighbour{neighbour}")
                    visitedPlots.add(neighbour)
                    currentRegion.add(neighbour)
                    queueToVisit.append(neighbour)


            totalPrice += currentArea * currentSides


    print(f"Total price: {totalPrice}")
    
    
    break
    """