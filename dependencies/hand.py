class Hand(object):
    def __init__(self, cards=None):
        if cards:
            self.__cards = cards
        else:
            self.__cards = []

    def __getitem__(self, item):
        return self.__cards[item]

    def __iter__(self):
        for card in self.__cards:
            yield card

    def __repr__(self):
        return str(self.__cards)

    def __str__(self):
        return self.__repr__()

    def split(self):
        second_card = self.__cards[1]
        self.__cards = [self.__cards[0]]
        return second_card

    def check_blackjack(self):
        return len(self.__cards) == 2 and self.sum_hand_of_cards() == 21

    def sum_hand_of_cards(self):
        number_of_aces = 0
        hand_sum = 0
        for card in self.__cards:
            hand_sum += card.value
            if card.value == 11:
                number_of_aces += 1
        for ace in range(number_of_aces):
            if hand_sum > 21:
                hand_sum -= 10
            else:
                break

        return hand_sum

    def add_card(self, card):
        self.__cards.append(card)
