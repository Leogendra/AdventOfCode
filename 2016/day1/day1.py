for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    instr = [dir.strip() for dir in [line.strip().split(",") for line in open(f"2022/day12/{fichier}.txt", "r")][0]]

    dir = 0
    walk = [0, 0, 0, 0]
    for inst in instr:
        if inst[0] == "L":
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        walk[dir] += int(inst[1:])
   
    print(f"Part 1 : {abs(walk[0]-walk[2]) + abs(walk[1] - walk[3])} steps")


    dir = 0
    walk = [0, 0, 0, 0]
    x, y = (0, 0)
    visited = [(x,y)]
    found = False
    for inst in instr:
        if inst[0] == "L":
            dir = (dir - 1) % 4
        else:
            dir = (dir + 1) % 4
        for i in range(int(inst[1:])):
            if dir == 0:
                y -= 1
            elif dir == 1:
                x += 1
            elif dir == 2:
                y += 1
            else:
                x -= 1
            if (x,y) in visited:
                print(f"Part 2 : {abs(x) + abs(y)} steps")
                found = True
            walk[dir] += 1
            visited.append((x,y))
        if found:
            break