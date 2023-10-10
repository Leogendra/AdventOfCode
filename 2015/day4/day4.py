import hashlib

for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    code = [line.strip() for line in open(f"2015/day4/{fichier}.txt", "r")][0]

    print("\033[93m--- Part One ---\033[0m")

    i = 0
    while True:
        if hashlib.md5(f"{code}{i}".encode()).hexdigest()[:5] == "00000":
            print(i)
            break
        i += 1

    print("\n\033[93m--- Part Two ---\033[0m")

    i = 0
    while True:
        if hashlib.md5(f"{code}{i}".encode()).hexdigest()[:6] == "000000":
            print(i)
            break
        i += 1