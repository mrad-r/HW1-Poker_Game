import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    # SUITS = ["clubs", "diamonds", "hearts", "spades"]
    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        return self.__str__() # repr is the same as str

class Deck:
    def __init__(self):
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
            self._cards = _cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self._cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)

if __name__ == "__main__":
    c1 = Card("A", "♣")
    print(c1)
    c1._suit = "♥"
    print(c1._suit, c1.rank)

    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)




