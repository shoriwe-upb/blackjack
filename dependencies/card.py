class Card(object):
    def __init__(self, card):
        self.__raw_card = card
        self.symbol = card[-1]
        self.raw_value = card[:-1]
        if card[:-1] in "AJQK":
            if card[:-1] == "A":
                self.value = 11
            else:
                self.value = 10
        else:
            self.value = int(card[:-1])

    def __iter__(self):
        for symbol in self.__raw_card:
            yield symbol

    def __repr__(self):
        return self.__raw_card

    def __str__(self):
        return str(self.__repr__())

    def __add__(self, other):
        return self.value + other.value
