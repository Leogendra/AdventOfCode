for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2019/day6/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    orbits = {}
    for line in data:
        orbitsTo_, object_= line.split(')')
        orbits[object_] = orbitsTo_

    totalOrbitCount = 0
    for object_ in orbits.keys():
        orbitCount = 0

        # suivre la chaine des orbites
        while object_ != "COM":
            orbitCount += 1
            object_ = orbits[object_]
        
        # ajouter le total
        totalOrbitCount += orbitCount

    print(f"Total orbits number: {totalOrbitCount}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    myOrbit = [orbitsTo_ for object_, orbitsTo_ in orbits.items() if (object_ == "YOU")][0]
    santaOrbit = [orbitsTo_ for object_, orbitsTo_ in orbits.items() if (object_ == "SAN")][0]

    myChain = []
    myCurrentOrbit = myOrbit
    # suivre la chaine pour YOU
    while myCurrentOrbit != "COM":
        myChain.append(myCurrentOrbit)
        myCurrentOrbit = orbits[myCurrentOrbit]
    
    santaChain = []
    santaCurrentOrbit = santaOrbit
    # suivre la chaine pour SAN
    while santaCurrentOrbit != "COM":
        santaChain.append(santaCurrentOrbit)
        santaCurrentOrbit = orbits[santaCurrentOrbit]

    # Calculer l'intersection
    orbitSwitchCount = 0
    for i, object_ in enumerate(myChain):
        if (object_ in santaChain):
            orbitSwitchCount = i + santaChain.index(object_)
            break

    print(f"Total orbits switchs: {orbitSwitchCount}")