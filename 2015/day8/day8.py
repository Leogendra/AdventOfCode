for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2015/day8/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    totalChars = 0
    totalCharsInMemory = 0
    for line in data:
        totalChars += len(line)
        totalCharsInMemory += len(eval(line))


    print(f"Number of escape characters: {totalChars-totalCharsInMemory}")



    
    print("\n\033[93m--- Part Two ---\033[0m")
    
    totalEncodedChars = 0
    for line in data:
        totalEncodedChars += len(line) + 2 + line.count("\\") + line.count("\"")

    print(f"Number of newly encoded characters: {totalEncodedChars-totalChars}")
