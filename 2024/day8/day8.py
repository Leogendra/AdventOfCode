for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day8/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    maxX, maxY = len(data[0]), len(data)
    antennas_map = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            antenna = data[i][j]
            if (antenna != "."):
                if (antenna not in antennas_map):
                    antennas_map[antenna] = []
                antennas_map[antenna].append((j, i))

    antinodes_map = {}
    for antenna, coords in antennas_map.items():
        nbAntennas = len(coords)
        if (nbAntennas > 1):
            for i in range(nbAntennas-1):
                coordsAntennaI = coords[i]
                for j in range(i+1, nbAntennas):
                    coordsAntennaJ = coords[j]
                    diffCoords = (coordsAntennaI[0] - coordsAntennaJ[0], coordsAntennaI[1] - coordsAntennaJ[1])
                    coordsAntinode1 = (coordsAntennaI[0] + diffCoords[0], coordsAntennaI[1] + diffCoords[1])
                    coordsAntinode2 = (coordsAntennaJ[0] - diffCoords[0], coordsAntennaJ[1] - diffCoords[1])
                    if (coordsAntinode1[0] >= 0) and (coordsAntinode1[0] < maxX) and (coordsAntinode1[1] >= 0) and (coordsAntinode1[1] < maxY):
                        antinodes_map[coordsAntinode1] = True
                    if (coordsAntinode2[0] >= 0) and (coordsAntinode2[0] < maxX) and (coordsAntinode2[1] >= 0) and (coordsAntinode2[1] < maxY):
                        antinodes_map[coordsAntinode2] = True

    print(f"Number of antinodes: {len(antinodes_map.keys())}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    antinodes_map = {}
    for antenna, coords in antennas_map.items():
        nbAntennas = len(coords)
        if (nbAntennas > 1):
            for i in range(nbAntennas-1):
                coordsAntennaI = coords[i]
                for j in range(i+1, nbAntennas):
                    coordsAntennaJ = coords[j]
                    diffCoords = (coordsAntennaI[0] - coordsAntennaJ[0], coordsAntennaI[1] - coordsAntennaJ[1])
                    
                    coordsAntinode1 = (coordsAntennaI[0], coordsAntennaI[1])
                    cptAntinode = 1
                    while (coordsAntinode1[0] >= 0) and (coordsAntinode1[0] < maxX) and (coordsAntinode1[1] >= 0) and (coordsAntinode1[1] < maxY):
                        antinodes_map[coordsAntinode1] = antenna
                        coordsAntinode1 = (coordsAntennaI[0] + diffCoords[0]*cptAntinode, coordsAntennaI[1] + diffCoords[1]*cptAntinode)
                        cptAntinode += 1

                    coordsAntinode2 = (coordsAntennaJ[0], coordsAntennaJ[1])
                    cptAntinode = 1
                    while (coordsAntinode2[0] >= 0) and (coordsAntinode2[0] < maxX) and (coordsAntinode2[1] >= 0) and (coordsAntinode2[1] < maxY):
                        antinodes_map[coordsAntinode2] = antenna
                        coordsAntinode2 = (coordsAntennaJ[0] - diffCoords[0]*cptAntinode, coordsAntennaJ[1] - diffCoords[1]*cptAntinode)
                        cptAntinode += 1

    print(f"Number of antinodes: {len(antinodes_map.keys())}")