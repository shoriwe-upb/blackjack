from random import randint, shuffle
from .card import Card


card_reference = ('AH', 'AP', 'AT', 'AD', '2H', '2P', '2T', '2D', '3H', '3P', '3T', '3D', '4H', '4P',
                        '4T', '4D', '5H', '5P', '5T', '5D', '6H', '6P', '6T', '6D', '7H', '7P', '7T', '7D',
                        '8H', '8P', '8T', '8D', '9H', '9P', '9T', '9D', '10H', '10P', '10T', '10D', 'JH',
                        'JP', 'JT', 'JD', 'QH', 'QP', 'QT', 'QD', 'KH', 'KP', 'KT', 'KD')


class Deck(object):
    def __init__(self):
        self.__cards = [Card(raw_card) for raw_card in card_reference]
        shuffle(self.__cards)
        self.__card_cemetery = []

    def __repr__(self):
        return self.__cards, self.__card_cemetery

    def __str__(self):
        return str(self.__repr__())

    @classmethod
    def __shuffle_split(cls, cards):
        middle = int(len(cards) / 2)
        return cards[middle:] + cards[:middle]

    @classmethod
    def __shuffle_one_over_other(cls, cards):
        buffer = []
        middle = int(len(cards) / 2)
        for card_index in range(middle):
            buffer.append(cards[middle:][card_index])
            buffer.append(cards[:middle][card_index])
        return buffer

    def pop(self):
        out_card = self.__cards.pop()
        self.__card_cemetery.append(out_card)
        return out_card

    def merge_cementery(self):
        for dead_card in self.__card_cemetery:
            self.__cards.insert(0, dead_card)

    def shuffle(self):
        for number in range(randint(1, 1000)):
            self.__cards = self.__shuffle_split(self.__shuffle_one_over_other(self.__cards))
