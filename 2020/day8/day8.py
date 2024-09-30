for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2020/day8/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    acc = 0
    ptr_memory = []
    ptr = 0
    while (ptr < len(data)):
        if ptr in ptr_memory:
            break
        ptr_memory.append(ptr)
        code, value = data[ptr].split(" ")
        if code == "nop":
            ptr += 1
        else:
            value = int(value)
            if code == "acc":
                acc += value
                ptr += 1
            else:
                ptr += value

    print(f"Accumulateur : {acc}")
    



    print("\n\033[93m--- Part Two ---\033[0m")
    
    valueToChange = 0
    while True:
        if data[valueToChange].split(" ")[0] == "acc":
            valueToChange += 1
            continue
        else:
            current_data = [line for line in data]
            current_data[valueToChange] = ("jmp " if data[valueToChange].startswith("nop") else "nop ") + data[valueToChange].split(" ")[1]

        acc = 0
        ptr_memory = []
        ptr = 0
        while (ptr < len(current_data)):
            if ptr in ptr_memory:
                break
            ptr_memory.append(ptr)
            code, value = current_data[ptr].split(" ")
            if code == "nop":
                ptr += 1
            else:
                value = int(value)
                if code == "acc":
                    acc += value
                    ptr += 1
                else:
                    ptr += value

        if ptr >= len(current_data):
            break
        valueToChange += 1
        

    print(f"Accumulateur : {acc}")
    

