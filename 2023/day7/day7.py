FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


def order_cards(hand):
    allCards = []
    for i in range(len(hand)):
        currentCard = hand[i]
        if currentCard == "W":
            currentCard = 0
        if currentCard == "T":
            currentCard = 10
        elif currentCard == "J":
            currentCard = 11
        elif currentCard == "Q":
            currentCard = 12
        elif currentCard == "K":
            currentCard = 13
        elif currentCard == "A":
            currentCard = 14
        allCards.append(int(currentCard))
    
    return allCards



def get_type(hand):
    hand_values = { card: 0 for card in "W23456789TJQKA" }

    for card in hand:
        hand_values[card] += 1

    # Five of a kind
    if any(value == 5 for value in hand_values.values()):
        handType = FIVE_OF_A_KIND
    
    # Four of a kind
    elif any(value == 4 for value in hand_values.values()):
        handType = FOUR_OF_A_KIND
        if hand_values["W"] > 0:
            handType = FIVE_OF_A_KIND
    
    # Full house or Three of a kind
    elif any(value == 3 for value in hand_values.values()):
        if hand_values["W"] == 3:
            if any(value == 2 for value in hand_values.values()):
                handType = FIVE_OF_A_KIND
            else:
                handType = FOUR_OF_A_KIND
        elif hand_values["W"] == 2:
            handType = FIVE_OF_A_KIND
        elif hand_values["W"] == 1:
            handType = FOUR_OF_A_KIND
        elif any(value == 2 for value in hand_values.values()):
            handType = FULL_HOUSE
        else:
            handType = THREE_OF_A_KIND
        
    # Two pair or One pair
    elif any(value == 2 for value in hand_values.values()):
        nombreDePaires = sum(value == 2 for value in hand_values.values())
        if nombreDePaires == 2:
            handType = TWO_PAIR
            if hand_values["W"] == 2:
                handType = FOUR_OF_A_KIND
            elif hand_values["W"] == 1:
                handType = FULL_HOUSE
        else:
            handType = ONE_PAIR
            if hand_values["W"] > 0:
                handType = THREE_OF_A_KIND
        
    # High card
    else:
        handType = HIGH_CARD
        if hand_values["W"] == 1:
            handType = ONE_PAIR

    return handType



def hand_one_win(player1, player2):
    hand1 = player1[0]
    hand2 = player2[0]
    type1 = get_type(hand1)
    type2 = get_type(hand2)

    if type1 == type2:
        cards1 = order_cards(hand1)
        cards2 = order_cards(hand2)
        i = 0
        while cards1[i] == cards2[i]:
            i += 1
        
        return cards1[i] > cards2[i]
    
    else:
        return type1 > type2

    

def sort_all_hands(hands):
    ordered_hands = []
    for hand in hands:
        i = 0
        while i < len(ordered_hands):
            if hand_one_win(hand, ordered_hands[i]):
                i += 1
            else:
                break
        ordered_hands = ordered_hands[:i] + [hand] + ordered_hands[i:]

    return ordered_hands




for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2023/day7/{fichier}.txt", "r") if line.strip() != ""]

    mains = [line.split() for line in data]

    print("\033[93m--- Part One ---\033[0m")

    mains_triees = sort_all_hands(mains)

    sommeDesParis = 0
    for i, main in enumerate(mains_triees):
        sommeDesParis += (i+1) * int(main[1])

    print(f"Somme des paris: {sommeDesParis}")

    



    print("\n\033[93m--- Part Two ---\033[0m")
    
    for i in range(len(mains)):
        mains[i] = [mains[i][0].replace('J', 'W'), mains[i][1]]

    mains_triees = sort_all_hands(mains)

    sommeDesParis = 0
    for i, main in enumerate(mains_triees):
        sommeDesParis += (i+1) * int(main[1])

    print(f"Somme des paris: {sommeDesParis}")

