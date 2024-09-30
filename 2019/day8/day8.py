for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2019/day8/{fichier}.txt", "r") if line.strip() != ""][0]

    print("\033[93m--- Part One ---\033[0m")

    width, height = (2, 2) if (fichier == "test") else (25, 6)
    layers = []
    current_layer = []
    current_row = []
    for i, digit in enumerate(data):
        if ((i%width) == 0) and (current_row):
            current_layer.append(current_row)
            current_row = []
        if (i%(width*height) == 0) and (current_layer):
            layers.append(current_layer)
            current_layer = []
        current_row.append(digit)
    
    if current_row:
        current_layer.append(current_row)
    if current_layer:
        layers.append(current_layer)

    min_zeros = width*height
    min_layer = []
    for layer in layers:
        zeros = sum([row.count("0") for row in layer])
        if zeros < min_zeros:
            min_zeros = zeros
            min_layer = layer
        
    ones = sum([row.count("1") for row in min_layer])
    twos = sum([row.count("2") for row in min_layer])

    print(f"Resultat : {ones*twos}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    render = []

    for i in range(height):
        render.append([])
        for j in range(width):
            for layer in layers:
                if layer[i][j] != "2":
                    render[i].append(layer[i][j])
                    break

    for row in render:
        print(("".join(row)).replace("0", " ").replace("1", "#"))
        

