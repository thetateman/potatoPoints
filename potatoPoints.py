import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Player:
    def __init__(self):
        self.hand = []
        self.field = []
        self.points = 0


def initialize_deck():
    deck = []
    suits = ['h', 'd', 's', 'c']
    for x in range(2, 12):
        for y in suits:
            new_card = Card(x, y)
            deck.append(new_card)
    return deck


def shuffle_deck(deck):
    shuffled_deck_x = []
    index_h = 0
    for b in range(0, len(deck)):
        pick_card = random.randint(0, 39 - index_h)
        # print("testing...pick_card:  " + str(pick_card))
        shuffled_deck_x.append(deck[pick_card])
        deck.pop(pick_card)
        index_h = index_h + 1
    return shuffled_deck_x


new_deck = initialize_deck()
shuffled_deck = shuffle_deck(new_deck)

p1 = Player()
p1.hand.extend(shuffled_deck[0:5])
p1.field.extend(shuffled_deck[5:10])

p2 = Player()
p2.hand.extend(shuffled_deck[10:15])
p2.field.extend(shuffled_deck[15:20])

p3 = Player()
p3.hand.extend(shuffled_deck[20:25])
p3.field.extend(shuffled_deck[25:30])

p4 = Player()
p4.hand.extend(shuffled_deck[30:35])
p4.field.extend(shuffled_deck[35:40])

players = [p1, p2, p3, p4]
lastRoundWinner = 0
print("Hello, welcome to PotatoPoints!\nLicensed under GPL (GNU General Public License) in 2020 by Tate Smith.\n\n")
for trickIndex in range(10):
    realOrderCounter = 0
    turnIndex = lastRoundWinner
    trick = []
    trickColor = ""
    leadingSuit = ""
    playerWinningTrick = turnIndex
    winningCard = 0
    while realOrderCounter <= 3:
        print("\nPlayer 1's Field: ")
        for r in range(len(p1.field)):
            print(str(p1.field[r].value) + str(p1.field[r].suit), end=" ")
        print("\nPlayer 2's Field: ")
        for t in range(len(p2.field)):
            print(str(p2.field[t].value) + str(p2.field[t].suit), end=" ")
        print("\nPlayer 3's Field: ")
        for u in range(len(p3.field)):
            print(str(p3.field[u].value) + str(p3.field[u].suit), end=" ")
        print("\nPlayer 4's Field: ")
        for o in range(len(p4.field)):
            print(str(p4.field[o].value) + str(p4.field[o].suit), end=" ")
        print("\nIt's Player " + str(turnIndex + 1) + "'s turn, please enter a move.")
        print("your hand is listed below:")
        for p in players[turnIndex].hand:
            print(str(p.value) + str(p.suit), end=" ")
        print("")
        moveValue = 0
        moveSuit = 'a'
        move = input()
        if len(move) == 2:
            moveValue = int(move[0])
            moveSuit = move[1]
        elif len(move) == 3:
            moveValue = int(move[0:2])
            moveSuit = move[2]
        else:
            print("please input in the correct format")
            continue
        cardPlayable = False
        otherEligibleCard = False
        tryAgain = False
        for handIter in players[turnIndex].hand:
            if (handIter.value == moveValue) and (handIter.suit == moveSuit):
                if not (realOrderCounter == 0):
                    if (moveSuit == "h" or moveSuit == "d") and (trickColor == "black"):
                        for handIterSecond in players[turnIndex].hand:
                            if handIterSecond.suit == "c" or handIterSecond.suit == "s":
                                otherEligibleCard = True
                                break
                        for fieldIterSecond in players[turnIndex].field:
                            if fieldIterSecond.suit == "c" or fieldIterSecond.suit == "s":
                                otherEligibleCard = True
                                break
                    if (moveSuit == 'c' or moveSuit == "s") and (trickColor == "red"):
                        for handIterSecond in players[turnIndex].hand:
                            if handIterSecond.suit == "h" or handIterSecond.suit == "d":
                                otherEligibleCard = True
                                break
                        for fieldIterSecond in players[turnIndex].field:
                            if fieldIterSecond.suit == "h" or fieldIterSecond.suit == "d":
                                otherEligibleCard = True
                                break
                    if otherEligibleCard:
                        print("You must follow color if you are able.")
                        tryAgain = True
                        break

                cardPlayable = True
                trick.append(handIter)
                players[turnIndex].hand.remove(handIter)
                break
        for fieldIter in players[turnIndex].field:
            if (fieldIter.value == moveValue) and (fieldIter.suit == moveSuit):
                if not (realOrderCounter == 0):
                    if (moveSuit == "h" or moveSuit == "d") and (trickColor == "black"):
                        for handIterSecond in players[turnIndex].hand:
                            if handIterSecond.suit == "c" or handIterSecond.suit == "s":
                                otherEligibleCard = True
                                break
                        for fieldIterSecond in players[turnIndex].field:
                            if fieldIterSecond.suit == "c" or fieldIterSecond.suit == "s":
                                otherEligibleCard = True
                                break
                    if (moveSuit == 'c' or moveSuit == "s") and (trickColor == "red"):
                        for handIterSecond in players[turnIndex].hand:
                            if handIterSecond.suit == "h" or handIterSecond.suit == "d":
                                otherEligibleCard = True
                                break
                        for fieldIterSecond in players[turnIndex].field:
                            if fieldIterSecond.suit == "h" or fieldIterSecond.suit == "d":
                                otherEligibleCard = True
                                break
                    if otherEligibleCard:
                        print("You must follow color if you are able.")
                        tryAgain = True
                        break

                cardPlayable = True
                trick.append(fieldIter)
                players[turnIndex].field.remove(fieldIter)
                break
        if tryAgain:
            continue
        if not cardPlayable:
            print("you don't have that card, try again.")
            continue

        if realOrderCounter == 0:
            leadingSuit = trick[0].suit
            if leadingSuit == "h" or leadingSuit == "d":
                trickColor = "red"
            if leadingSuit == "c" or leadingSuit == "s":
                trickColor = "black"
        else:
            if moveValue > trick[winningCard].value:
                if ((moveSuit == "c" or moveSuit == "s") and (trickColor == "black")) or (
                        (moveSuit == "h" or moveSuit == "d") and (trickColor == "red")):
                    winningCard = realOrderCounter
                    playerWinningTrick = turnIndex
                    print(str(turnIndex) + " is now winning the trick")
            elif moveValue == trick[winningCard].value:
                if moveSuit == leadingSuit:
                    winningCard = realOrderCounter
                    playerWinningTrick = turnIndex
                    print(str(turnIndex) + " is now winning the trick.")

        turnIndex = turnIndex + 1
        if turnIndex == 4:
            turnIndex = 0
        realOrderCounter = realOrderCounter + 1
    trickSum = 0
    for playedCard in trick:
        if playedCard.value % 2 == 0:
            trickSum = trickSum + playedCard.value
    players[playerWinningTrick].points = players[playerWinningTrick].points + trickSum
    lastRoundWinner = playerWinningTrick
    for index in range(4):
        print("Player " + str(index) + ": " + str(players[index].points))

    # print(str(moveValue) + str(moveSuit))

exit(0)
