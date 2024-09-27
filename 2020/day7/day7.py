for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2020/day7/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    rules = {}
    for line in data:
        infos = line.split(" contain ")
        bagColor = infos[0].replace("bags", "").strip()
        rules[bagColor] = {}
        contains = infos[1].split(", ")
        for contain in contains:
            if contain != "no other bags.":
                nb, clr1, clr, _bag = contain.split(" ")
                rules[bagColor][clr1 + " " + clr] = int(nb)


    myBag = "shiny gold"
    numberOfBags = 0
    for bagColor in rules:
        if bagColor != myBag:
            containsMyBag = False
            bagsList = [bagColor]
            while bagsList and not(containsMyBag):
                currentBag = bagsList.pop()
                currentBagContains = rules[currentBag]
                for containedBag in currentBagContains:
                    if containedBag == myBag:
                        containsMyBag = True
                        break
                    else:
                        bagsList.append(containedBag)
            if containsMyBag:
                numberOfBags += 1


    print(f"Number of bags that can carry: {numberOfBags}")




    print("\n\033[93m--- Part Two ---\033[0m")

    numberOfBags = 0
    bagsList = [myBag]
    while bagsList:
        currentBag = bagsList.pop()
        currentBagContains = rules[currentBag]
        for containedBag in currentBagContains:
            numberOfBags += currentBagContains[containedBag]
            for i in range(currentBagContains[containedBag]):
                bagsList.append(containedBag)


    print(f"Number of bags contained: {numberOfBags}")