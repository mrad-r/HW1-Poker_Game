from Deck import Deck, Card

class PokerHand:
    def __init__(self, deck):

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        return self.number_matches == 8

    @property
    def number_matches(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.number_matches == 2: # simple
            return True
        return False

    @property
    def is_two_pair(self):
        return self.number_matches == 4 # more advanced

    @property
    def is_trips(self):
        if self.number_matches == 6:
            return True
        return False

    @property
    def is_full_house(self):
        if self.number_matches == 8:
            return True
        else:
            return False

    @property
    def is_quads(self):
        if self.number_matches == 12:
            return True
        return False

    @property
    def is_straight(self):
        """
        Checks if the hand is straight
        :return:
        """
        if self.number_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != Card.RANKS.index(self.cards[0].rank)+4:
            return False
        return True


count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:

        matches += 1
        # print(hand)
        break
    count += 1

print(f"probability of a full house is {100*matches/count}%")


