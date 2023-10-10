print('\n')
for fichier in ["test", "input"]:
    print("\n\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    input = [line.strip() for line in open(f"2020/day4/{fichier}.txt", "r")]

    all_passeports = []
    passeport = []
    
    for line in input:
        if line.strip() == '':
            all_passeports.append(passeport)
            passeport = []
        else:
            for field in line.split():
                key, value = field.split(':')
                passeport.append((key, value))
    all_passeports.append(passeport)


    print("\033[93m--- Part One ---\033[0m")
    
    validPassport = 0

    for passeport in all_passeports:
        # print(passeport)
        if len(passeport) == 8:
            validPassport += 1
        elif (len(passeport) == 7) and all(key != "cid" for key, _ in passeport):
            validPassport += 1

    print(f"Nombre de passport valides : {validPassport}")


    print("\n\033[93m--- Part Two ---\033[0m")

    import re
    
    validPassport = 0

    for passeport in all_passeports:
        # print(passeport)
        if (len(passeport) == 8) or (len(passeport) == 7) and all(key != "cid" for key, _ in passeport):
            check = True
            for field, value in passeport:
                if field == "byr":
                    if (int(value) < 1920) or (int(value) > 2002):
                        check = False
                        break
                if field == "iyr":
                    if (int(value) < 2010) or (int(value) > 2020):
                        check = False
                        break
                if field == "eyr":
                    if (int(value) < 2020) or (int(value) > 2030):
                        check = False
                        break
                if field == "hgt":
                    unite = value[-2:]
                    valeur = value[:-2]
                    if valeur.strip() == '':
                        check = False
                        break
                    if unite == "cm":
                        if (int(valeur) < 150) or (int(valeur) > 193):
                            check = False
                            break
                    else:
                        if (int(valeur) < 59) or (int(valeur) > 76):
                            check = False
                            break
                if field == "hcl":
                    if (value[0] != '#') or (len(value[1:]) != 6) or not bool(re.match(r'^[0-9a-f]+$', value[1:])):
                        check = False
                        break
                if field == "ecl":
                    if not(value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                        check = False
                        break
                if field == "pid":
                    if len(value) != 9:
                        check = False
                        break
            
            validPassport += check

                # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                # hgt (Height) - a number followed by either cm or in:
                #     If cm, the number must be at least 150 and at most 193.
                #     If in, the number must be at least 59 and at most 76.
                # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                # pid (Passport ID) - a nine-digit number, including leading zeroes.
                # cid (Country ID) - ignored, missing or not.


    print(f"Nombre de passport valides : {validPassport}")