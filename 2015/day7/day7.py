def get_signal(signal):

    try:
        return int(signal)
    except:
        if (signal in signals): 
            return signals[signal]
        
    signalIn = wires[signal] # list
        
    if (len(signalIn) == 1):
        res = get_signal(signalIn[0])

    elif (len(signalIn) == 2):
        _, bit = signalIn
        res = (~get_signal(bit)) & (2**nbBits - 1)
    
    if (len(signalIn) == 3):
        a, operation, b = signalIn
        if operation == "AND":
            res = (get_signal(a) & get_signal(b)) & (2**nbBits - 1)
        if operation == "OR":
            res = (get_signal(a) | get_signal(b)) & (2**nbBits - 1)
        if operation == "LSHIFT":
            res = (get_signal(a) << int(b)) & (2**nbBits - 1)
        if operation == "RSHIFT":
            res = (get_signal(a) >> int(b)) & (2**nbBits - 1)
    signals[signal] = res
    return res


for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2015/day7/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    nbBits = 16
    signals = {}
    wires = {}

    for line in data:
        signalIn, signalOut = line.split(' -> ')
        wires[signalOut] = signalIn.split(" ")

    aSignal = get_signal('a')

    print(f"\nValeur du signal a: {aSignal}")



    
    print("\n\033[93m--- Part Two ---\033[0m")

    wires['b'] = [str(aSignal)]

    signals = {}
    aSignal = get_signal('a')

    print(f"\nValeur du signal a: {aSignal}")

