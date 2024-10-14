import random

def create_marketcards(number):
    marketcards = []

    for x in range(number):
        newcard = [random.randint(1,4),random.randint(1,4),random.randint(1,4),random.randint(1,4)]
        newcard.sort()
        marketcards.append(newcard)

    return marketcards
