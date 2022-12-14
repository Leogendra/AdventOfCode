def getPackets(txt):
    if len(txt) == 1:
        return int(txt)
    elif txt == "[]":
        return []
    else: #if txt[0] == "[":
        packet = []
        pack = ""
        cptOuvrantes = 0
        for i in range(1, len(txt)):
            if txt[i] == "," and cptOuvrantes == 0:
                packet.append(getPackets(pack))
                pack = ""
                continue
            elif txt[i] == "[":
                cptOuvrantes += 1
            elif txt[i] == "]":
                if cptOuvrantes > 0:
                    cptOuvrantes -= 1
                else:
                    packet.append(getPackets(pack))
                    break
            pack += txt[i]

        return packet



def packBefore(pack1, pack2): # two lists
    j1, j2 = 0, 0
    while j1 < len(pack1) and j2 < len(pack2):
        item1, item2 = pack1[j1], pack2[j2]
        if isinstance(item1, list) and isinstance(item2, list):
            res = packBefore(item1, item2)
            if res != "continue":
                return res
        elif isinstance(item1, list):
            return packBefore(item1, [item2])
        elif isinstance(item2, list):
            return packBefore([item1], item2)
        else: # both are integers
            if item1 < item2:
                return True
            elif item1 > item2:
                return False
        j1 += 1
        j2 += 1

    if (j1 == len(pack1)) and (j2 == len(pack2)):
        return "continue"  
    else:
        return (j1 == len(pack1))
            


def DIY_sort(liste):
    if len(liste) <= 1:
        return liste
    else:
        pivot = liste[0]
        left = []
        right = []
        for i in range(1, len(liste)):
            item = liste[i]
            if packBefore(item, pivot):
                left.append(item)
            else:
                right.append(item)
        return DIY_sort(left) + [pivot] + DIY_sort(right)



for fichier in ["test", "input"]:
    print(f"\nFICHIER {fichier}.txt")
    input = [line.strip() for line in open(f"2022/day13/{fichier}.txt", "r")]
    
    packets = []
    for line in input:
        if line != "":
            packets.append(eval(line))

    packets_ordered = []
    for i in range(len(packets)//2):
        isOrdered = packBefore(packets[2*i], packets[2*i+1])
        if (isOrdered):
            packets_ordered.append(i+1)


    print(f"Part 1 : {sum(packets_ordered)}")

    packets += [[[2]], [[6]]]
    packets = DIY_sort(packets)

    decoder_key = (packets.index([[2]])+1) * (packets.index([[6]])+1)
    print(f"Part 2 : {decoder_key}")
    if decoder_key != 140:
        break

    