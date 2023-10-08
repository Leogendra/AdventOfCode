import os

# récupère le nom du dossier actuel
currentDirectory = os.getcwd().split('\\')[-1]

# Génère les fichiers du jour 1 au jour 25
for x in range(1, 26):

    text = f"""for fichier in ["test", "input"]:
    print("\\033[92m" + f"\\n*** FICHIER {{fichier}}.txt ***" + "\\033[0m")
    data = [line.strip() for line in open(f"{currentDirectory}/day{x}/{{fichier}}.txt", "r")]

    print("\\033[93m--- Part One ---\\033[0m")
    
    print("\\n\\033[93m--- Part Two ---\\033[0m")
    """

    os.mkdir(f'day{x}')
    with open(f'day{x}/day{x}.py', 'w') as f:
        f.write(text)
    with open(f'day{x}/input.txt', 'w') as f:
        pass
    with open(f'day{x}/test.txt', 'w') as f:
        pass