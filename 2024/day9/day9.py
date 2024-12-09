def print_disk(disk, blockIndex):
    for item in disk:
        if (item["isSpace"]):
            print("."*item["size"], end="")
        else:
            print(f"{item["blockId"]}"*item["size"], end="")
    print(f"   {blockIndex=}")
    



for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day9/{fichier}.txt", "r") if line.strip() != ""][0]

    print("\033[93m--- Part One ---\033[0m")

    disk_list = []

    space = False
    blockId = 0
    for char in data:
        number = int(char)

        if (space):
            for _ in range(number):
                disk_list.append(-1)
        else:
            for _ in range(number):
                disk_list.append(blockId)
            blockId += 1
        space = not(space)

    while (-1 in disk_list):
        toPlace = disk_list.pop(-1)
        if (toPlace == -1):
            continue
        firstSpace = disk_list.index(-1)
        disk_list[firstSpace] = toPlace

    print(f"filesystem checksum: {sum([i*disk_list[i] for i in range(len(disk_list))])}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    disk_map_list = []

    space = False
    blockId = 0
    for char in data:
        number = int(char)
        if number > 0:
            disk_map_list.append({
                "blockId": blockId if not(space) else -1,
                "size": number,
                "isSpace": space
            })
        if not(space):
            blockId += 1
        space = not(space)


    blockIndex = len(disk_map_list) - 1
    while blockIndex >= 0:

        # print_disk(disk_map_list, blockIndex)

        if (disk_map_list[blockIndex]["isSpace"]):
            blockIndex -= 1
            continue

        blockSize = disk_map_list[blockIndex]["size"]
        for i in range(blockIndex):
            if (disk_map_list[i]["isSpace"]) and (disk_map_list[i]["size"] >= blockSize):
                if (disk_map_list[i]["size"] == blockSize):
                    disk_map_list[i]["isSpace"] = False
                    disk_map_list[i]["blockId"] = disk_map_list[blockIndex]["blockId"]
                    disk_map_list[blockIndex]["isSpace"] = True
                    disk_map_list[blockIndex]["blockId"] = -1
                else:
                    disk_map_list[i]["size"] -= blockSize
                    toPlace = {k:v for k, v in disk_map_list[blockIndex].items()} # deep copy
                    disk_map_list[blockIndex]["isSpace"] = True
                    disk_map_list[blockIndex]["blockId"] = -1
                    disk_map_list.insert(i, toPlace)
                    blockIndex += 1
                break
        blockIndex -= 1

    checksum, blockIndex = 0, 0
    for item in disk_map_list:
        if (item["isSpace"]):
            blockIndex += item["size"]
            continue
        for _ in range(item["size"]):
            checksum += blockIndex * item["blockId"]
            blockIndex += 1


    print(f"filesystem checksum: {checksum}")