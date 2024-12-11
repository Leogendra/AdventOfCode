def calculate_number_stones(data, nbBlinks):
    stones = {}
    for stone in data:
        stones[stone] = stones.get(stone, 0) + 1

    for i in range(nbBlinks):
        current_stones = [(k, v) for k, v in stones.items()]
        for stone, nbStones in current_stones:
            if (stone == 0):
                stones[stone] -= nbStones
                stones[1] = stones.get(1, 0) + nbStones
            elif (len(str(stone)) % 2 == 0):
                stoneStr = str(stone)
                stone1 = int(stoneStr[:len(stoneStr)//2])
                stone2 = int(stoneStr[len(stoneStr)//2:])
                stones[stone] -= nbStones
                stones[stone1] = stones.get(stone1, 0) + nbStones
                stones[stone2] = stones.get(stone2, 0) + nbStones
            else:
                stones[stone] -= nbStones
                stones[stone*2024] = stones.get(stone*2024, 0) + nbStones

    return sum(v for _, v in stones.items())




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2024/day11/{fichier}.txt", "r") if line.strip() != ""][0]
    data = list(map(int, data.split()))

    print("\033[93m--- Part One ---\033[0m")
            
    nbBlinks = 25
    print(f"Number of stones after {nbBlinks} blinks: {calculate_number_stones(data, nbBlinks)}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
            
    nbBlinks = 75
    print(f"Number of stones after {nbBlinks} blinks: {calculate_number_stones(data, nbBlinks)}")