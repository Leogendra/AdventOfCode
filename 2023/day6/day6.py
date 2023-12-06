import math


def calculate_ways_bruteforce(time, record):
    ways = 0
    hold = time/2 # selon le calcul de la dérivé de f(x) = x*(time-x) on a un maximum en x = time/2
    if int(hold) == hold:
        ways += 1 # on part du principe qu'on bat le record
        hold -= 1
    else:
        ways += 2 # on bat le record 2 fois
        hold = time//2 - 1

    currentTime = hold * (time - hold)
    while (hold > 0) and (currentTime > record):
        ways += 2
        hold -= 1
        currentTime = hold * (time - hold)

    return ways



def calculate_ways_math(time, record):
    ways = 0
    f_x = lambda x: -(x**2) + time*x - record

    delta = time**2 - (4 * -1 * (-record))

    if delta < 0:
        return 0  # Pas de solution réelle, aucune façon de battre le record

    sqrt_delta = math.sqrt(delta)
    borne_inf = math.floor((-time + sqrt_delta) / (-2)) + 1 # la borne représenta la valeur à partir de laquelle le record n'est pas battu, on prend donc le premier nombre au dessus
    borne_sup = math.ceil((-time - sqrt_delta) / (-2)) - 1

    return borne_sup - borne_inf + 1




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day6/{fichier}.txt", "r")]

    times = [time.strip() for time in data[0].split(":")[1].split(" ") if (time.strip() != "")]
    distances = [time.strip() for time in data[1].split(":")[1].split(" ") if (time.strip() != "")]
    races = [(int(time), int(distance)) for time, distance in zip(times, distances)]

    print("\033[93m--- Part One ---\033[0m")

    numberOfWays = 1
    for time, record in races:
        numberOfWays *= calculate_ways_math(time, record)

    print(f"Nombre de manière de gagner : {numberOfWays}")

    


    print("\n\033[93m--- Part Two ---\033[0m")

    raceTime = int(''.join(times))
    raceDistance = int(''.join(distances))
    
    ways = calculate_ways_math(raceTime, raceDistance)

    print(f"Grosse course : {ways}")

