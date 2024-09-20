for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2017/day6/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    def redistribuate(memory):
        max_memory = max(memory)
        index = memory.index(max_memory)
        memory[index] = 0
        for i in range(max_memory):
            memory[(index + i + 1) % len(memory)] += 1
        return memory

    memory = list(map(int, data[0].split()))
    seen_memory = []
    steps = 0

    while memory not in seen_memory:
        seen_memory.append(memory[:])
        memory = redistribuate(memory)
        steps += 1

    print(f"Number of steps : {steps}")
    
    print("\n\033[93m--- Part Two ---\033[0m")

    seen_memory = memory[:]
    memory = redistribuate(memory)
    steps = 1

    while memory != seen_memory:
        memory = redistribuate(memory)
        steps += 1

    print(f"Number of steps : {steps}")
    

