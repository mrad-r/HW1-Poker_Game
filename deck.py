import random
class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]
    # SUITS = ["clubs", "diamonds", "hearts", "spades"]
    def __init__(self, rank, suit):
        """
        Creates a Card object with a specific rank and suit.

        :param rank: A string representing the rank of the card, which is one of the elements of RANKS.
        :param suit: A string representing the suit of the card, which is one of the elements of SUITS.
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Returns the rank of the card.
        :return: A string corresponding to the rank of the card.
        """
        return self._rank

    @property
    def suit(self):
        """
        Returns the suit of the card.

        :return: A string corresponding to the suit of the card.
        """
        return self._suit

    def __str__(self):
        """
        Returns a string comprising the rank and the suit of the card

        :return: A string combining the rank and the suit of the card
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Returns the string that represents the card

        :return: A string combining the rank and suit of the card
        """
        return self.__str__() # repr is the same as str

    def __eq__(self, other):
        """
        Compares two cards by checking if they have the same rank.

        :param other: A different card object to compare with self
        :return: True if both cards have the same rank. False if the ranks of the cards are different.
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Compares two cards by checking which one has the highest rank.

        :param other: A second card object to be compared with self.
        :return: True if the rank of self card (current card)  is lower than other card. False otherwise.
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

class Deck:
    def __init__(self):
        """
        Creates a deck with 52 cards, each with a rank and a suit by creating a list of objects called "_cards"
        """
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """
        Returns the list of card objects in the deck
        :return: A list of the card objects that make up the deck.
        """
        return self._cards

    def __str__(self):
        """
        Returns the deck as a string.
        :return: A string with all the cards of the deck
        """
        return str(self._cards)

    def shuffle(self):
        """
        Shuffles the deck by randomizing the order of the cards.

        :return: A string with the cards of the deck in a random order.
        """
        random.shuffle(self.cards)

    def deal(self):
        """
        Returns and removes the first card of the deck, simulating a deal.
        :return: The first card object of the deck
        """
        return self.cards.pop(0)

if __name__ == "__main__":
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)

