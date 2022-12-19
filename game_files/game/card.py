class Card:
    def __init__(self, value, suit):
        '''
        Initialize the card class with values and suits
        '''
        self.cost = value
        self.value = ['Ace', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'Jack', 'Queen', 'King'][value - 1]
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades'][suit]

    def price(self):
        '''
        Set values to each assignment in the value list from __init__
        anything over 10 is set to 10
        anything below 1 is set to Ace value of 1 or 11
        '''
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost

    def show(self):
        '''
        Show value of card and suit its attched to
        '''
        print(f'{self.value} of {self.suit}')
