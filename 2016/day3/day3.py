for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    triangles = [line.strip() for line in open(f"2016/day3/{fichier}.txt", "r")]

    print("--- Part One ---")

    possible = 0
    for tri in triangles:
        sides = [int(side) for side in tri.split(" ") if side.strip() != '']
        a = sides[0]
        b = sides[1]
        c = sides[2]
        if (a+b <= c) or (a+c <= b) or (b+c <= a):
            continue
        else:
            possible += 1

    print(possible)


    print("\n--- Part Two ---")

    possible = 0
    sides1 = []
    sides2 = []
    sides3 = []

    for i, tri in enumerate(triangles):
        if i%3 == 0:
            sides1 = [int(side) for side in tri.split(" ") if side.strip() != '']
        if i%3 == 1:
            sides2 = [int(side) for side in tri.split(" ") if side.strip() != '']
        if i%3 == 2:
            sides3 = [int(side) for side in tri.split(" ") if side.strip() != '']

            a1, a2, a3 = sides1
            b1, b2, b3 = sides2
            c1, c2, c3 = sides3

            for a, b, c in [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]:
                if (a+b <= c) or (a+c <= b) or (b+c <= a):
                    continue
                else:
                    possible += 1

    print(possible)