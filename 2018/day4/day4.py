print('\n\n')
for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    records = [line.strip() for line in open(f"2018/day4/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    guards = {}

    for record in sorted(records):
        if "Guard" in record:
            guardId = int(record.split()[3][1:])
            if guardId not in guards:
                guards[guardId] = [0] * 60  # [0, 0, 0, 0, 0, 0, ...]
        elif "falls" in record:
            start = int(record.split()[1][3:5])
        elif "wakes" in record:
            end = int(record.split()[1][3:5])
            for minute in range(start, end):
                guards[guardId][minute] += 1

    bestGuard = max(guards, key=lambda x: sum(guards[x]))                # garde qui a la plus grande somme de toutes les minutes
    bestMinute = guards[bestGuard].index(max(guards[bestGuard]))         # index de la minute la plus dormie
    print(f"Guard {bestGuard} slept the most at minute {bestMinute}")
    print(f"Answer: {bestGuard * bestMinute}")



    print("\n\033[93m--- Part Two ---\033[0m")

    bestGuard = max(guards, key=lambda x: max(guards[x]))               # garde qui a la plus grande minute
    bestMinute = guards[bestGuard].index(max(guards[bestGuard]))        # index de la minute la plus dormie
    print(f"Guard {bestGuard} slept the most at minute {bestMinute}")
    print(f"Answer: {bestGuard * bestMinute}")
