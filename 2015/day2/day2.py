for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    boxes = [line.strip() for line in open(f"2015/day2/{fichier}.txt", "r")]

    print("--- Part One ---")

    total_paper = 0
    for box in boxes:
        l, w, h = [int(x) for x in box.split("x")]
        smaller = min(l*w, w*h, h*l)
        dimension = 2*l*w + 2*w*h + 2*h*l + smaller
        total_paper += dimension
    
    print(f"Total paper : {total_paper}")

    print("\n--- Part Two ---")
    total_ribbon = 0
    for box in boxes:
        l, w, h = [int(x) for x in box.split("x")]
        ribbon = 2*min(l+w, w+h, h+l)
        bow = l*w*h
        total_ribbon += (ribbon + bow)

    print(f"Total ribbon : {total_ribbon}")