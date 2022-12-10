def part1(fichier):
    commands = [line.strip() for line in open(f"2022/day{day}/{fichier}.txt", "r")]
    cpt = 0
    X = 1
    cycle = 1
    importantCycle = 20
    for cmd in commands:
        if cycle+1 >= importantCycle:
            cpt += X*importantCycle
            importantCycle += 40
        if cmd == "noop":
            cycle += 1

        else:
            V = int(cmd.split()[1])
            cycle += 2
            X += V

    return cpt



def part2(fichier):
    commands = [line.strip() for line in open(f"2022/day{day}/{fichier}.txt", "r")]
    CRT = ""
    X = 1
    cycle = 0
    for cmd in commands:
        if cmd == "noop":
            CRT += ('#' if (cycle%40 in [X-1, X, X+1]) else '.')
            cycle += 1
        else:
            V = int(cmd.split()[1])
            for _ in range(2):
                CRT += ('#' if (cycle%40 in [X-1, X, X+1]) else '.')
                cycle += 1
            X += V            

    screen = []
    for i in range(6):
        screen.append(CRT[40*i:40*i+40])
    return screen



day = 10
print("Part 1 (test) :",part1("test"))
print("Part 1 (input) :",part1("input"))
print("\nPart 2 (test) :\n")
print("\n".join(part2("test")))
print("Part 2 (input) :")
print("\n".join(part2("input")))