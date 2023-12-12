def line_incorrect(line, nums):
    
    springs = [spring for spring in line.split('.') if spring != '']
    
    if len(springs) != len(nums):
        return True
    
    for i in range(len(springs)):
        if len(springs[i]) != nums[i]:
            return True
        
    return False



def get_number_permutations(line, nums, i):

    if (i == len(line)):
        if line_incorrect(line, nums) or (line.count('#') != sum(nums)):
            return 0
        else:
            return 1

    if (line.count('#') > sum(nums)):
        return 0
    
    if line[i] != '?':
        return get_number_permutations(line, nums, i+1)
    
    else:
        # on procède par backtracking
        permutations = 0
        for char in ['#', '.']:
            new_line = line[:i] + char + line[i+1:]
            permutations += get_number_permutations(new_line, nums, i+1)

        return permutations
    


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day12/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    somme = 0

    for line in data:
        springs, _numbers = line.split()
        numbers = list(map(int, _numbers.split(',')))


        somme += get_number_permutations(springs, numbers, 0)

    print(f"Somme des arrangements : {somme}")
    
    print("\n\033[93m--- Part Two ---\033[0m")

