for fichier in ["test", "input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    input = [line.strip() for line in open(f"2016/day2/{fichier}.txt", "r")]

    print("--- Part One ---")

    # 1 2 3
    # 4 5 6
    # 7 8 9

    start = 5
    for code in input:
        for dir in code:
            if dir == "U" and start > 3:
                start -= 3
            elif dir == "D" and start < 7:
                start += 3
            if dir == "L" and start%3 != 1:
                start -= 1
            elif dir == "R" and start%3 != 0:
                start += 1
        print(start, end="")
    

    print("\n--- Part Two ---")

    #     1
    #   2 3 4
    # 5 6 7 8 9
    #   A B C
    #     D
    no_up = [1, 2, 4, 5, 9]
    no_down = [5, 9, 10, 12, 13]
    no_left = [1, 2, 5, 10, 13]
    no_right = [1, 4, 9, 12, 13]
    
    start = 5
    for code in input:
        for dir in code:
            if dir == "U" and (start not in no_up):
                if (start == 3) or (start == 13):
                    start -= 2
                else:
                    start -= 4
            elif dir == "D" and (start not in no_down):
                if (start == 11) or (start == 1):
                    start += 2
                else:
                    start += 4
            if dir == "L" and (start not in no_left):
                start -= 1
            elif dir == "R" and (start not in no_right):
                start += 1

        convert = {10: "A", 11: "B", 12: "C", 13: "D"}
        if start in convert:
            num_code = convert[start]
        else:
            num_code = start
        
        print(num_code, end="")
    
    # break