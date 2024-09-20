for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2016/day6/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    characters_table = [{} for _ in range(len(data[0]))]
    for code in data:
        for i, char in enumerate(code):
            characters_table[i][char] = characters_table[i].get(char, 0) + 1

    message = ""
    for ligne in characters_table:
        message += sorted(ligne.items(), key=lambda x: x[1], reverse=True)[0][0]

    print(f"Secret message: {message}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    message = ""
    for ligne in characters_table:
        message += sorted(ligne.items(), key=lambda x: x[1])[0][0]

    print(f"Secret message: {message}")
    

