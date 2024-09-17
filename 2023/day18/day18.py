RESET = "\033[0m"


def get_voisins(x, y, maxX, maxY):
    voisins = []
    for i, j, dir in [(-1,0,"U"), (0,-1,"L"), (0,1,"R"), (1,0,"D")]:
        if y+i < 0 or y+i >= maxY:
            continue
        elif x+j < 0 or x+j >= maxX:
            continue
        voisins.append([y+i, x+j, dir])
    return voisins


def print_ground(ground, color=""):
    for line in ground:
        for elem in line:
            if elem == 0:
                print(".", end="")
            else:
                print(color + "#" + RESET, end="")
        print("")
    print()


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day18/{fichier}.txt", "r") if line.strip() != ""]

    instructions = []
    for line in data:
        direction, meters, color = line.split(" ")
        instructions.append((direction, int(meters), color.strip("()")))


    dico_instructions = {
        "U": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
        "D": (0, 1)
    }

    print("\033[93m--- Part One ---\033[0m")

    groundLenght = 20
    ground = [[0 for _ in range(groundLenght)] for _ in range(groundLenght)]

    startX, currentX = groundLenght//2, groundLenght//2
    startY, currentY = groundLenght//2, groundLenght//2
    # startX, currentX = 0, 0
    # startY, currentY = 0, 0
    ground[currentY][currentX] = 1

    # creusage du tours
    for instruction in instructions:
        direction, meters, color = instruction
        x, y = dico_instructions[direction]
        for i in range(meters):
            currentX += x
            currentY += y
            ground[currentY][currentX] = 1


    print("jusque là ça va")

    print_ground(ground)

    sommeCreusee = 0
    print(f"Somme cresée : {sommeCreusee}")
    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    break
