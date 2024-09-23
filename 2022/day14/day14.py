import math

def print_carte(carte):
    for line in carte:
        print("".join(line))
    print()


def isBlockedDown(x,y,carte):
    return carte[y+1][x] != "."

def isBlockedLeft(x,y,carte):
    return carte[y+1][x-1] != "."

def isBlockedRight(x,y,carte):
    return carte[y+1][x+1] != "."

def isBlocked(x,y,carte):
    return isBlockedDown(x,y,carte) and isBlockedLeft(x,y,carte) and isBlockedRight(x,y,carte)

def falling(x, y, carte):
    if not(isBlockedDown(x, y, carte)):
        return [x, y+1]
    elif not(isBlockedLeft(x, y, carte)):
        return [x-1, y+1]
    elif not(isBlockedRight(x, y, carte)):
        return [x+1, y+1]
    else:
        return [x, y]



for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    input = [line.strip() for line in open(f"2022/day14/{fichier}.txt", "r")]
    instructions = []
    xmin, xmax, ymin, ymax = [math.inf*(-1)**(i) for i in range(4)]
    for line in input:
        instr = []
        coord = line.split()
        for co in coord:
            if co == "->":
                continue
            else:
                x, y = [int(x) for x in co.split(",")]
                instr.append([x,y])
                xmin = min(xmin, x)
                xmax = max(xmax, x)
                #ymin = min(ymin, y)
                ymax = max(ymax, y)
        instructions.append(instr)
    
    xmin -= 1
    carte = [["." for x in range(xmin, xmax+2)] for y in range(ymax+2)]
    for line in instructions:
        for i in range(len(line)-1):
            x1, y1 = line[i]
            x2, y2 = line[i+1]
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2)+1):
                    carte[y][x1-xmin] = "#"
            elif y1 == y2:
                for x in range(min(x1,x2), max(x1,x2)+1):
                    carte[y1][x-xmin] = "#"
    
    
    cpt = -1
    abyss = False
    while not(abyss):
        sand = [500-xmin,0]
        sand_fell = falling(sand[0], sand[1], carte)
        while sand_fell != sand:
            if (sand_fell[1] > ymax) or (sand_fell[0] < 1) or (sand_fell[0] > xmax):
                abyss = True
                break
            sand = sand_fell
            sand_fell = falling(sand[0], sand[1], carte)
        carte[sand[1]][sand[0]] = "o"
        cpt += 1


    print_carte(carte)
    print(f"Part 1: {cpt} sands")
    

    carte = [["." for x in range(1000)] for y in range(ymax+3)]
    for line in instructions:
        for i in range(len(line)-1):
            x1, y1 = line[i]
            x2, y2 = line[i+1]
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2)+1):
                    carte[y][x1] = "#"
            elif y1 == y2:
                for x in range(min(x1,x2), max(x1,x2)+1):
                    carte[y1][x] = "#"
    
    carte[-1] = ["#" for x in range(1000)]

    cpt2 = 0
    stable = False
    while not(stable):
        sand = [500,0]
        sand_fell = falling(sand[0], sand[1], carte)
        if sand_fell == sand:
            stable = True
        while sand_fell != sand:
            sand = sand_fell
            sand_fell = falling(sand[0], sand[1], carte)
        carte[sand[1]][sand[0]] = "o"
        cpt2 += 1


    print(f"Part 2 : {cpt2} sands")