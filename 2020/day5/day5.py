for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2020/day5/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    maxSeatId = 0
    seat_list = []

    for boardingPass in data:
        maxRow = 127
        maxColumn = 7
        minRow = 0
        minColumn = 0
        for seat in boardingPass:
            if seat == "B":
                minRow += (maxRow - minRow + 1) // 2
            if seat == "F":
                maxRow -= (maxRow - minRow + 1) // 2
            if seat == "R":
                minColumn += (maxColumn - minColumn + 1) // 2
            if seat == "L":
                maxColumn -= (maxColumn - minColumn + 1) // 2

        # print(f"min Row : {minRow}, max Row : {maxRow} - min Column : {minColumn}, max Column : {maxColumn}")
        seatId = minRow * 8 + minColumn
        maxSeatId = max(maxSeatId, seatId)
        seat_list.append(seatId)

    print(f"Max seat ID : {maxSeatId}")
    



    print("\n\033[93m--- Part Two ---\033[0m")

    seat_list.sort()
    previousSeat = seat_list[0]

    for seat in seat_list[1:]:
        if previousSeat + 2 == seat:
            print(f"Seat ID : {seat-1}")
            break
        else:
            previousSeat = seat
    

