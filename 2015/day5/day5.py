import re

for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    data = [line.strip() for line in open(f"2015/day5/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    niceStrings = 0
    for line in data:
        if not(re.search(r'([aeiou].*){3,}', line)):
               continue
        elif not(re.search(r'(.)\1', line)):
            continue
        elif re.search(r'ab|cd|pq|xy', line):
            continue
        else:
             niceStrings += 1

    print(f"Nombre de niceStrings: {niceStrings}")


    print("\n\033[93m--- Part Two ---\033[0m")

    niceStrings = 0
    for line in data:
        if not(re.search(r'(.{2})(.*)\1', line)):
            continue
        if not(re.search(r'(.)(.)\1', line)):
            continue
        niceStrings += 1

    print(f"Nombre de niceStrings: {niceStrings}")
    