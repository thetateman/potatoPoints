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
    index = 0
    for b in range(0, len(deck)):
        pick_card = random.randint(0, 39 - index)
        print("testing...pick_card:  " + str(pick_card))
        shuffled_deck_x.append(deck[pick_card])
        deck.pop(pick_card)
        index = index + 1
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

exit()