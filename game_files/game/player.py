from game.deck import Deck


class Player:
    def __init__(self, isDealer, deck):
        self.cards = []
        self.isDealer = isDealer
        self.deck = deck
        self.score = 0

    def check_score(self):
        '''
        add values of each card in the hand and return a score. 
        add a value check in that if you score over 21, any ace value cards in your deck are reassigned to 1 from 11
        '''
        a_counter = 0
        self.score = 0
        for card in self.cards:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()

        while a_counter != 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def hit(self):
        '''
        add card to hand
        if new value is over 21, initiate bust, if less than 21, add card to hand and value to score
        '''
        self.cards.extend(self.deck.draw(1))
        self.check_score()
        if self.score > 21:
            return 1
        return 0

    def deal(self):
        '''
        deal function, starts game with dealing 2 cards and returning score value
        '''
        self.cards.extend(self.deck.draw(2))
        self.check_score()
        if self.score == 21:
            return 1
        else:
            return 0

    def show(self):
        '''
        shows card values and score value of cards in hand
        '''
        if self.isDealer:
            print("\nDealer's Cards\n")
        else:
            print("\nPlayer's Cards\n")

        for card in self.cards:
            card.show()

        print(f'\nScore: {str(self.score)}')
