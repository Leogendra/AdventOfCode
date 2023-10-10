for fichier in ["test", "input"]:
    print("\033[92m" + f"\n*** FICHIER {fichier}.txt ***" + "\033[0m")
    phrases = [line.strip() for line in open(f"2017/day4/{fichier}.txt", "r")]

    print("\033[93m--- Part One ---\033[0m")

    valides = 0

    for phrase in phrases:
        dejaVu = []
        valid = True
        for word in phrase.split(' '):
            if word in dejaVu:
                valid = False
                break
            else:
                dejaVu.append(word)

        valides += valid

    print(f"Nombre de passphrases sans mots répétés : {valides}")

    print("\n\033[93m--- Part Two ---\033[0m")

    valides = 0

    for phrase in phrases:
        dejaVu = []
        valid = True
        for word in phrase.split(' '):
            for dejaWord in dejaVu:
                if len(word) == len(dejaWord):
                    for c in word:
                        if c in dejaWord:
                            dejaWord = dejaWord.replace(c, '', 1)
                    if len(dejaWord) == 0:
                        valid = False
                        break
            if not(valid):
                break
            else:
                dejaVu.append(word)

        valides += valid

    print(f"Nombre de passphrases sans anagrammes : {valides}")