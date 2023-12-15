def get_all_distances(galaxies, void_rows, void_columns, expansion):
    totalDistances = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            distance = 0
            
            while (x1 != x2):
                if x1 < x2:
                    if x1+1 in void_columns:
                        distance += expansion
                    else:
                        distance += 1
                    x1 += 1
                elif x1 > x2:
                    if x1-1 in void_columns:
                        distance += expansion
                    else:
                        distance += 1
                    x1 -= 1

            while (y1 != y2):
                if y1 < y2:
                    if y1+1 in void_rows:
                        distance += expansion
                    else:
                        distance += 1
                    y1 += 1
                elif y1 > y2:
                    if y1-1 in void_rows:
                        distance += expansion
                    else:
                        distance += 1
                    y1 -= 1
            
            totalDistances += distance

    return totalDistances


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day11/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    galaxies = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "#":
                galaxies.append((x, y))

    void_rows = []
    for y in range(len(data)):
        if data[y].count("#") == 0:
            void_rows.append(y)
    
    void_columns = []
    for x in range(len(data[0])):
        if ("".join([data[y][x] for y in range(len(data))])).count("#") == 0:
            void_columns.append(x)


    distances = get_all_distances(galaxies, void_rows, void_columns, 2)

    print(f"Somme des distances: {distances}")



    print("\n\033[93m--- Part Two ---\033[0m")

    distances = get_all_distances(galaxies, void_rows, void_columns, 1000000)

    print(f"Somme des distances avec expansion 1000000 : {distances}")