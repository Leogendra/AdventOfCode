for fichier in ["input"]:
    print(f"\n*** FICHIER {fichier}.txt ***")
    input = [line.strip() for line in open(f"2019/day2/{fichier}.txt", "r")]

    print("--- Part One ---")

    data = [int(x) for x in input[0].split(",")]
    if fichier == "input":
        data[1] = 12
        data[2] = 2

    ptr = 0
    while ptr < len(data):
        if data[ptr] == 99:
            break
        else:
            if data[ptr] == 1:
                data[data[ptr+3]] = data[data[ptr+1]] + data[data[ptr+2]]
            elif data[ptr] == 2:
                data[data[ptr+3]] = data[data[ptr+1]] * data[data[ptr+2]]
            ptr += 4

    print(data[0])

    print("\n--- Part Two ---")

    def run_program(noun, verb):
        program_data = [int(x) for x in input[0].split(",")]
        program_data[1] = noun
        program_data[2] = verb

        ptr = 0
        while ptr < len(program_data):
            if program_data[ptr] == 99:
                break
            else:
                if program_data[ptr] == 1:
                    program_data[program_data[ptr+3]] = program_data[program_data[ptr+1]] + program_data[program_data[ptr+2]]
                elif program_data[ptr] == 2:
                    program_data[program_data[ptr+3]] = program_data[program_data[ptr+1]] * program_data[program_data[ptr+2]]
                ptr += 4

        return program_data[0]

    desired_output = 19690720

    for noun in range(100):
        for verb in range(100):
            result = run_program(noun, verb)
            if result == desired_output:
                print("Noun:", noun)
                print("Verb:", verb)
                print("Result:", 100 * noun + verb)
                break


    
    break