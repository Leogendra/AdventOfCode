import hashlib

for fichier in ["input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    doorId = [line.strip() for line in open(f"2016/day5/{fichier}.txt", "r")][0]

    print("\033[93m--- Part One ---\033[0m")

    password = ""
    i = 0
    while len(password) < 8:
        m = hashlib.md5()
        m.update((doorId + str(i)).encode("utf-8"))
        if m.hexdigest()[:5] == "00000":
            password += m.hexdigest()[5]
        i += 1

    print(password)
    


    print("\n\033[93m--- Part Two ---\033[0m")
    
    password = ['-' for _ in range(8)]
    i = 0
    while '-' in password:
        m = hashlib.md5()
        m.update((doorId + str(i)).encode("utf-8"))
        if m.hexdigest()[:5] == "00000":
            position, char = m.hexdigest()[5:7]
            if position.isdigit() and int(position) < 8 and password[int(position)] == "_":
                password[int(position)] = char
        i += 1

    print("".join(password))