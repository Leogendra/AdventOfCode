for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2020/day6/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    groups = []
    group = []
    for line in data:
        if line == "":
            groups.append(group)
            group = []
        else:
            group.append(line)
    if group != []:
        groups.append(group)

    yesCount = 0
    for group in groups:
        questions = []
        for line in group:
            for char in line:
                questions.append(char)
        yesCount += len(set(questions))

    print(f"Nombre de 'yes' : {yesCount}")       


    
    print("\n\033[93m--- Part Two ---\033[0m")

    yesCount = 0
    for group in groups:
        questions = set(char for char in group[0])
        for i, line in enumerate(group):
            questions = questions & set([char for char in line])
        yesCount += len(set(questions))

    print(f"Nombre de 'yes' : {yesCount}")    
    

