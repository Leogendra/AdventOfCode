import math

def part1(fichier):
    input = [line.strip() for line in open(f"2022/day{day}/{fichier}.txt", "r")]
    monkeys_full = [[]]
    monkeys_stocks = []
    i = 0
    for line in input:
        if (line == ""):
            i += 1
            monkeys_full.append([])
        else:
            monkeys_full[i].append(line)
            if (line.split()[0] == "Starting"):
                monkeys_stocks.append([int(item.split(",")[0]) for item in line.split()[2:]])

    monkeys_nb = int(monkeys_full[-1][0].split()[1].split(":")[0]) + 1
    monkeys_activity = [0 for _ in range(monkeys_nb)]
    for round in range(20): # 20 rounds
        for monk_nb in range(len(monkeys_full)): # pour tout les monk
            monk = monkeys_full[monk_nb] 
            while (monkeys_stocks[monk_nb] != []): # tant qu'il a un item
                monkeys_activity[monk_nb] += 1 # incrémente le nb d'item touchés

                # calcul de la valeur de worry
                worry = monkeys_stocks[monk_nb].pop(0)
                operation = monk[2].split()
                if (operation[4] == "+"):
                    worry += int(operation[-1])
                else:
                    if (operation[-1] == "old"):
                        worry *= worry
                    else:
                        worry *= int(operation[5])
                worry //= 3

                # check si passe le test
                test = int(monk[3].split()[-1])
                monk_to_give = -1
                if (worry/test == worry//test):
                    monk_to_give = int(monk[4].split()[-1])
                else:
                    monk_to_give = int(monk[5].split()[-1])
                monkeys_stocks[monk_to_give].append(worry)



    monkeys_activity.sort(reverse = True)
    return (monkeys_activity[0] * monkeys_activity[1])




def part2(fichier):
    input = [line.strip() for line in open(f"2022/day{day}/{fichier}.txt", "r")]
    monkeys_full = [[]]
    monkeys_stocks = []
    i = 0
    for line in input:
        if (line == ""):
            i += 1
            monkeys_full.append([])
        else:
            monkeys_full[i].append(line)
            if (line.split()[0] == "Starting"):
                monkeys_stocks.append([int(item.split(",")[0]) for item in line.split()[2:]])

    monkeys_nb = int(monkeys_full[-1][0].split()[1].split(":")[0]) + 1
    monkeys_activity = [0 for _ in range(monkeys_nb)]
    for round in range(10000): # 20 rounds
        for monk_nb in range(len(monkeys_full)): # pour tout les monk
            monk = monkeys_full[monk_nb] 
            while (monkeys_stocks[monk_nb] != []): # tant qu'il a un item
                monkeys_activity[monk_nb] += 1 # incrémente le nb d'item touchés

                # calcul de la valeur de worry
                worry = monkeys_stocks[monk_nb].pop(0)
                operation = monk[2].split()
                if (operation[4] == "+"):
                    worry += int(operation[-1])
                else:
                    if (operation[-1] == "old"):
                        worry *= worry
                    else:
                        worry *= int(operation[5])
                worry %= math.prod([2,3,5,7,11,13,17,19,23])

                # check si passe le test
                test = int(monk[3].split()[-1])
                monk_to_give = -1
                if (worry % test == 0):
                    monk_to_give = int(monk[4].split()[-1])
                else:
                    monk_to_give = int(monk[5].split()[-1])
                monkeys_stocks[monk_to_give].append(worry)


    monkeys_activity.sort(reverse = True)
    return (monkeys_activity[0] * monkeys_activity[1])



day = 11

p1 = part1("test")
print("Part 1 (test) :",p1)
if p1 == 10605:
    print("Part 1 (input) :",part1("input"))

    p2 = part2("test")
    print("Part 2 (test) :",p2)
    if p2 == 2713310158:
        print("Part 2 (input) :",part2("input"))