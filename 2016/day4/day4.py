for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    rooms = [line.strip() for line in open(f"2016/day4/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    sumSectors = 0

    for room in rooms:
        occurences = {}
        idRoom = 0
        checksum = room.split('[')[1][:-1]
        for code in room.split('[')[0].split('-'):
            if code.isdigit():
                idRoom = int(code)
                break
            else:
                for c in code:
                    occurences[c] = occurences.get(c, 0) + 1

        occurences = [key for key, value in sorted(occurences.items(), key=lambda item: (-item[1], item[0]))]

        if ''.join(occurences[:5]) == checksum:
            sumSectors += idRoom

    print(f"Somme des ID des salles valides : {sumSectors}")
    

    print("\n\033[93m--- Part Two ---\033[0m")

    for room in rooms:
        phrase = ""
        idRoom = int(room.split('[')[0].split('-')[-1])
        checksum = room.split('[')[1][:-1]
        for code in room.split('[')[0].split('-'):
            if code.isdigit():
                break
            else:
                for c in code:
                    phrase += chr((ord(c) - 97 + idRoom) % 26 + 97)
            phrase += ' '

        if "storage" in phrase and "north" in phrase:
            print(f"{phrase} : {idRoom}")
    
    # break