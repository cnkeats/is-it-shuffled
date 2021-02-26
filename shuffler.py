
import random

cardImageMap = {}
cardNumberMap = {}
sortedFullDeck = []

index = 0
for suit in ('S', 'H', 'C', 'D'):
    for value in ('A','2','3','4','5','6','7','8','9','10','J','Q','K'):
        cardImageMap[value + suit] = 'images/playing-cards/' + value + suit + '.png'
        cardNumberMap[index] = value + suit
        index += 1
        sortedFullDeck.append(value + suit)

def riffleShuffle(deck, imperfect = True):
    deckSize = len(deck)
    halfSize = deckSize // 2

    if imperfect:
        for i in range(0, 7):
            halfSize += random.randint(-1,1)

    half1 = deck[:halfSize]
    half2 = deck[halfSize:]
    
    # sometimes the other deck should start on top!
    if (random.randint(0,len(deck))) > halfSize:
        half1, half2 = half2, half1

    shuffledDeck = []

    index1 = 0
    index2 = 0
    chooseLeft = False
    while index1 + index2 < len(deck):
        chooseLeft = not chooseLeft

        chanceOfDefect = 0.1
        r = random.uniform(0,1)

        if imperfect and r <= chanceOfDefect:
            chooseLeft = not chooseLeft
        if index1 < len(half1) and (index2 >= len(half2) or chooseLeft):
            shuffledDeck.append(half1[index1])
            index1 += 1
        else:
            shuffledDeck.append(half2[index2])
            index2 += 1
    return shuffledDeck

deck = range(0,52)
print(*deck)
deck = riffleShuffle(deck)
print(*deck)