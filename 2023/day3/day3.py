for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day3/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    len_x = len(data[0])
    len_y = len(data)
    somme = 0
    
    gears = {}
    gears_to_add = []

    _num = ""
    engine = False

    for y, line in enumerate(data):
        for x, char in enumerate(line):

            if char.isdigit():
                _num += char

                # check des voisins
                if not(engine):
                    for i in range(3):
                        new_y = y + i - 1
                        if (new_y >= 0) and (new_y < len_y):
                            for j in range(3):
                                new_x = x + j - 1
                                if (new_x >= 0) and (new_x < len_x):
                                    value = data[new_y][new_x]
                                    if not(value.isdigit()) and (value != '.'):
                                        engine = True
                                        # PART 2
                                        if value == '*':
                                            gears_to_add.append([new_x, new_y])

            elif _num != "":
                for x_gear, y_gear in gears_to_add:
                    gears.setdefault(str(x_gear)+'-'+str(y_gear), []).append(int(_num))
                gears_to_add = []
                if engine:
                    somme += int(_num)
                    engine = False
                _num = ""

        if _num != "":
            for x_gear, y_gear in gears_to_add:
                gears.setdefault(str(x_gear)+'-'+str(y_gear), []).append(int(_num))
            gears_to_add = []
            if engine:
                somme += int(_num)
                engine = False
            _num = ""


    print(f"La somme des numéros des moteurs est {somme}")


    
    print("\n\033[93m--- Part Two ---\033[0m")    
    
    gearRatio = 0

    for gear, values in gears.items():
        if len(values) == 2:
            gearRatio += values[0] * values[1]

    print(f"Le gear-ratio est de {gearRatio}")