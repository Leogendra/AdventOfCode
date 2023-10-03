for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    instructions = [line.strip() for line in open(f"2018/day3/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    fabric = [['.' for _ in range(1010)] for _ in range(1010)]
    if fichier == "test":
        fabric = [['.' for _ in range(15)] for _ in range(15)]
    

    # d'abord on met tout les claim
    for instruction in instructions:
        split_instruction = instruction.split(" ")
        id_instr = split_instruction[0][1:]
        x, y = map(int, split_instruction[2][:-1].split(","))
        w, h = map(int, split_instruction[3].split("x"))

        for i in range(y, y+h):
            for j in range(x, x+w):
                if fabric[i][j] == '.':
                    fabric[i][j] = id_instr
                else:
                    fabric[i][j] = 'X'


    # ensuite on compte les claim qui overlap
    count = 0
    for line in fabric:
        for case in line:
            if case == 'X':
                count += 1

    if fichier == "test":
        for line in fabric:
            print(''.join(line))
    # else:
    #     with open('result.txt', 'w') as f:
    #         for line in fabric:
    #             f.write(''.join(line) + '\n')


    print(f"Nombre de claim qui overlap : {count}")


    print("\n\033[93m--- Part Two ---\033[0m")

    # on va compter le nombre de claim qui overlap
    for instruction in instructions:
        split_instruction = instruction.split(" ")
        id_instr = split_instruction[0][1:]
        x, y = map(int, split_instruction[2][:-1].split(","))
        w, h = map(int, split_instruction[3].split("x"))

        overlap = False
        for i in range(y, y+h):
            for j in range(x, x+w):
                if fabric[i][j] == 'X':
                    overlap = True
                    break
            if overlap:
                break
        if not overlap:
            print(f"Le claim {id_instr} ne chevauche aucun autre claim")
            break