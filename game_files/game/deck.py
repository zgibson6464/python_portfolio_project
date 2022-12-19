import random
from game.card import Card


class Deck:
    def __init__(self):
        '''
        Assign empty list value of cards generated and used
        '''
        self.cards = []

    def generate(self):
        '''
        Generate cards in a value range of 1 to 14 for the card value list, add sub range for suits list
        '''
        for x in range(1, 14):
            for y in range(3):
                self.cards.append(Card(x, y))

    def draw(self, iteration):
        '''
        returns card generated from generate() function to player hand
        '''
        cards = []
        for x in range(iteration):
            card = random.choice(self.cards)
            self.cards.remove(card)
            cards.append(card)
        return cards

    def count(self):
        return len(self.cards)
