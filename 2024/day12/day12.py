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


def get_all_neightbours(coords, maxX, maxY):
    x, y = coords
    neighbours = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (i >= 0) and (i < maxY) and (j >= 0) and (j < maxX):
                neighbours.append((j, i))
    return neighbours




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day12/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    diagonal_map = {
        (1, 1): [(0, 1), (1, 0)],
        (-1, 1): [(0, 1), (-1, 0)],
        (1, -1): [(0, -1), (1, 0)],
        (-1, -1): [(0, -1), (-1, 0)]
    }

    maxX, maxY = len(data[0]), len(data)

    visitedPlots = set()
    totalPrice = 0
    totalPricePart2 = 0
    for i in range(maxY):
        for j in range(maxX):
            if (j, i) in visitedPlots:
                continue
            visitedPlots.add((j, i))
            currentPlant = data[i][j]
            currentRegion = {(j, i)}
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

                    currentPerimeter += 2 - 2*sum(1 for n in get_direct_neighbours(neighbour, maxX, maxY) if ((n != currentPlot) and (n in currentRegion)))

                    visitedPlots.add(neighbour)
                    currentRegion.add(neighbour)
                    queueToVisit.append(neighbour)


            totalPrice += len(currentRegion) * currentPerimeter
            
            ### Part 2
            currentSides = 0
            for plot in currentRegion:
                plotX, plotY = plot

                for cornerX, cornerY in diagonal_map.keys():
                    adjacentSidesDeltas = diagonal_map[(cornerX, cornerY)]
                    adjacentSide1 = (plotX+adjacentSidesDeltas[0][0], plotY+adjacentSidesDeltas[0][1])
                    adjacentSide2 = (plotX+adjacentSidesDeltas[1][0], plotY+adjacentSidesDeltas[1][1])

                    if ((cornerX+plotX, cornerY+plotY) in currentRegion):
                        if (adjacentSide1 not in currentRegion) and (adjacentSide2 not in currentRegion):
                            currentSides += 1
                    
                    else:
                        if ((adjacentSide1 not in currentRegion) == (adjacentSide2 not in currentRegion)):
                            currentSides += 1

            totalPricePart2 += len(currentRegion) * currentSides


    print(f"Total price: {totalPrice}")




    print("\n\033[93m--- Part Two ---\033[0m")


    print(f"Total price: {totalPricePart2}")