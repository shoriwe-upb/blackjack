from .hand import Hand


class Player(object):
    def __init__(self, player_id):
        self.player_id = player_id
        self.__hands = [Hand(), None]

    def __iter__(self):
        for hand in self.__hands:
            yield hand

    def __repr__(self):
        return str(self.__hands)

    def __str__(self):
        if self.player_id:
            name = f"Player {self.player_id}:"
        else:
            name = "Dealer:"
        return f"{name} {self.__hands}"

    def __getitem__(self, item):
        return self.__hands[item]

    @classmethod
    def ask_for_card(cls):
        response = input("Do you want a card?[y/n]")
        return "y" in response.lower()

    @classmethod
    def ask_split_hand(cls):
        response = input("\033[0;32mDo you want to split you hand?[y/n]\033[0;0m")
        return "y" in response.lower()

    def split_hand(self):
        second_card = self.__hands[0].split()
        self.__hands[1] = Hand([second_card])

    def clean_hands(self):
        self.__hands = [Hand(), None]
