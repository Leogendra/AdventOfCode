for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day5/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    page_order_before = {}
    page_order_after = {}
    updates = []

    for line in data:
        if ("|" in line):
            pages = [int(nb) for nb in line.split("|")]

            if (pages[0] not in page_order_before):
                page_order_before[pages[0]] = []
            page_order_before[pages[0]].append(pages[1])

            if (pages[1] not in page_order_after):
                page_order_after[pages[1]] = []
            page_order_after[pages[1]].append(pages[0])

        elif ("," in line):
            updates.append([int(nb) for nb in line.split(",")])
        
    cpt = 0
    for update in updates:
        valid = True
        for i in range(len(update)):
            currentPage = update[i]
            if currentPage in page_order_after:
                for beforePage in page_order_after[currentPage]:
                    if (beforePage in update) and (beforePage in update[i:]):
                        valid = False
                        break
        if valid:
            cpt += update[len(update)//2]

    print(cpt)




    print("\n\033[93m--- Part Two ---\033[0m")

    cpt = 0
    for update in updates:
        valid = True
        for i in range(len(update)):
            currentPage = update[i]
            if currentPage in page_order_after:
                for beforePage in page_order_after[currentPage]:
                    if (beforePage in update) and (beforePage in update[i:]):
                        valid = False
                        break

        if not(valid):
            new_update = [nb for nb in update]
            i = 0
            while i < len(new_update):
                # word = ", ".join([f"*{new_update[j]}*" if i == j else f"{new_update[j]}" for j in range(len(new_update))])
                # print(f"  [{word}]")
                currentPage = new_update[i]
                if currentPage in page_order_after:
                    for beforePage in page_order_after[currentPage]:
                        if (beforePage in new_update) and (beforePage not in new_update[:i]):
                            toSwap = new_update.index(beforePage)
                            new_update[toSwap], new_update[i] = new_update[i], new_update[toSwap]
                            i = 0
                            break
                i += 1
                        
            cpt += new_update[len(new_update)//2]

    print(cpt)