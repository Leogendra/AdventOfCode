import time


def create_map_of_maps(data, reverse=False):
    _mapName = ""
    map_of_maps = {}
    current_map = {}

    for line in data[2:]:
        if "map:" in line:
            if reverse:
                _truc1, _to, _truc2 = line.split(" ")[0].split('-')
                _mapName = f"{_truc2.strip()}-{_to.strip()}-{_truc1.strip()}"
            else:
                _mapName = line.split(" ")[0].strip()
            current_map = {}

        elif line.strip() == "":
            # save de la map
            map_of_maps[_mapName] = current_map

        else:
            destinationStart, sourceStart, rangeValue = [int(val) for val in line.split(" ")]
            if reverse:
                current_map[destinationStart] = [sourceStart, rangeValue]
            else:
                current_map[sourceStart] = [destinationStart, rangeValue]

    # cas où on a fini mais pas de ligne vide
    map_of_maps[_mapName] = current_map

    return map_of_maps



def search_through_maps(seedValue, map_of_maps, _start, _end):
    while _start != _end:
        for _mapName in map_of_maps.keys():
            if _start == _mapName.split("-")[0]:
                _start = _mapName.split("-")[-1]

                # on cherche si la seed est dans la map
                sorted_sources = sorted(map_of_maps[_mapName].keys())
                lastSourceValue = sorted_sources[0]
                for startSource in sorted_sources:
                    if startSource > seedValue:
                        break
                    lastSourceValue = startSource

                # on regarde si la seed est présente dans la range la plus proche
                destinationStart, rangeValue = map_of_maps[_mapName][lastSourceValue]
                if (seedValue >= lastSourceValue) and (seedValue < lastSourceValue + rangeValue):
                    seedValue = destinationStart + (seedValue - lastSourceValue)
                else:
                    pass # seedValue = seedValue
                break
    return seedValue


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day5/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    _seeds = data[0].split(":")[1].strip().split(" ")
    
    map_of_maps = create_map_of_maps(data)

    seeds = map(int, _seeds)
    lowestLocation = float('inf')

    for seed in seeds:
        seedValue = seed
        _start = "seed"
        _end = "location"
        seedValue = search_through_maps(seedValue, map_of_maps, _start, _end)

        if seedValue < lowestLocation:
            lowestLocation = seedValue

    print(f"Plus petite valeur de location : {lowestLocation}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    maxValue = 23738616
    reversed_map_of_maps = create_map_of_maps(data, reverse=True)

    start_time = time.time()
    seeds_ranges = list(map(int, _seeds))
    lowestLocation = float('inf')

    seed = 0
    trouve = False
    while not(trouve):
        _start = "location"
        _end = "seed"
        seedValue = search_through_maps(seed, reversed_map_of_maps, _start, _end)

        # Si ma seedValue existe dans une range
        for i in range(0, len(seeds_ranges), 2):
            startingSeedValue = seeds_ranges[i]
            rangeValue = seeds_ranges[i+1]
            
            if (seedValue >= startingSeedValue) and (seedValue < startingSeedValue + rangeValue):
                lowestLocation = seed
                trouve = True
                break
        
        seed += 1

    print(f"Plus petite valeur de location : {lowestLocation}, temps : {round(time.time() - start_time, 1)}s")

    # break