for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day16/{fichier}.txt", "r") if line.strip() != ""]

    directions_map = {
        "N": (-1, 0),
        "S": (1, 0),
        "E": (0, 1),
        "W": (0, -1)
    }

    print("\033[93m--- Part One ---\033[0m")

    redirection_map = {
        "N": {
            "/": ["E"],
            "\\": ["W"],
            "|": ["N"],
            "-": ["E", "W"]
        },
        "S": {
            "/": ["W"],
            "\\": ["E"],
            "|": ["S"],
            "-": ["E", "W"]
        },
        "E": {
            "/": ["N"],
            "\\": ["S"],
            "|": ["N", "S"],
            "-": ["E"]
        },
        "W": {
            "/": ["S"],
            "\\": ["N"],
            "|": ["N", "S"],
            "-": ["W"]
        }
    }

    light_map = {}

    beams = [{ "x": -1, "y": 0, "direction": "E" }]

    while len(beams) > 0:

        beam = beams.pop()
        x = beam["x"]
        y = beam["y"]
        direction = beam["direction"]

        while True:

            # On avance dans la direction
            x += directions_map[direction][1]
            y += directions_map[direction][0]

            if (y < 0) or (y >= len(data)) or (x < 0) or (x >= len(data[y])):
                # On est au bord
                break
            
            new_tile = data[y][x]
            
            if new_tile == ".":
                pass # la direction change pas
            else:
                new_direction = redirection_map[direction][new_tile]
                if len(new_direction) > 1:
                    # On stack la beam dans la queue
                    beams.append({ "x": x, "y": y, "direction": new_direction[1] })

                direction = new_direction[0]

            # On est jamais passé par cette case
            if not(f"{x}-{y}" in light_map.keys()):
                light_map[f"{x}-{y}"] = [direction]

            # On est déjà passé par cette case mais pas dans cette direction
            elif not(direction in light_map[f"{x}-{y}"]):
                light_map[f"{x}-{y}"].append(direction)

            # On est déjà passé par cette case dans cette direction
            else:
                break

    # print de la map
    # for y in range(len(data)):
    #     for x in range(len(data[y])):
    #         if f"{x}-{y}" in light_map.keys():
    #             print("#", end="")
    #         else:
    #             print(data[y][x], end="")
    #     print()

    print(f"Nombre de cases illuminées : {len(light_map.keys())}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    maxEnergized = 0

    entry_points = []
    for i in range(len(data)):
        entry_points.append((-1, i, "E"))
        entry_points.append((len(data[i]), i, "W"))
    for j in range(len(data[0])):
        entry_points.append((j, -1, "S"))
        entry_points.append((j, len(data), "N"))


    for xEntry, yEntry, directionEntry in entry_points:
        light_map = {}

        beams = [{ "x": xEntry, "y": yEntry, "direction": directionEntry }]

        while len(beams) > 0:

            beam = beams.pop()
            x = beam["x"]
            y = beam["y"]
            direction = beam["direction"]

            while True:

                # On avance dans la direction
                x += directions_map[direction][1]
                y += directions_map[direction][0]

                if (y < 0) or (y >= len(data)) or (x < 0) or (x >= len(data[y])):
                    # On est au bord
                    break
                
                new_tile = data[y][x]
                
                if new_tile == ".":
                    pass # la direction change pas
                else:
                    new_direction = redirection_map[direction][new_tile]
                    if len(new_direction) > 1:
                        # On stack la beam dans la queue
                        beams.append({ "x": x, "y": y, "direction": new_direction[1] })

                    direction = new_direction[0]

                # On est jamais passé par cette case
                if not(f"{x}-{y}" in light_map.keys()):
                    light_map[f"{x}-{y}"] = [direction]

                # On est déjà passé par cette case mais pas dans cette direction
                elif not(direction in light_map[f"{x}-{y}"]):
                    light_map[f"{x}-{y}"].append(direction)

                # On est déjà passé par cette case dans cette direction
                else:
                    break

        if len(light_map.keys()) > maxEnergized:
            maxEnergized = len(light_map.keys())


    print(f"Nombre maximal de cases illuminées : {maxEnergized}")