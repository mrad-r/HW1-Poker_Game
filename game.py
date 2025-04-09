from deck import Deck, Card

class Hand:
    """
    A hand of 5 cards dealt from a deck
    """
    def __init__(self, deck):
        """
        Creates a new hand of five cards dealt from the deck
        :param deck: A Deck object with a deal() method that returns a card
        """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        """
        Returns the five cards in the given hand
        :return: A list of five cards (the hand)
        """
        return self._cards

    def __str__(self):
        """
        Returns a string of five cards corresponding to the hand
        :return: A string representing the five cards in the hand
        """
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if each card of the hand is on the same suit (condition for a flush)
        :return: True if all the cards have the same suit and False otherwise.
        """
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Checks the number of matches (a pair of cards with the same rank) in the hand
        :return: An integer representing the number of matches
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand has exactly one pair
        :return: True if the hand has exactly one pair, False otherwise
        """
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        """
        Checks if the hand has exactly two pairs
        :return: True if the hand has exactly two pairs, False otherwise
        """
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        """
        Checks if the hand has exactly three cards with the same rank
        :return: True if the hand has exactly three cards with the same rank, False otherwise
        """
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        """
        Checks if the hand has exactly four cards with the same rank
        :return: True if the hand has exactly four cards with the same rank, False otherwise
        """
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        """
        Checks if the hand has three cards with the same rank and a pair (condition for a full house)
        :return: True if the hand is a full house, False otherwise
        """
        if self.num_matches == 8:
            return True
        else:
            return False

    @property
    def is_straight(self):
        """
        Checks if the hand contains five cards in a sequence with no cards with repeated ranks (condition for a straight)
        :return: True if the hand is a straight, False otherwise
        """
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != \
                Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True
matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    count += 1
    if hand.is_straight:
        # print(hand)
        matches += 1
        # break

print(f"The probability of straight is {100*matches/count}%")

