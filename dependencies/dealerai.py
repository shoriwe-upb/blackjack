class DealerAI(object):
    def __init__(self, players):
        self.__dealer_points = players[0][0].sum_hand_of_cards()
        self.__players = players
        self.__risk = self.counts_cards(players)
    # I don't know if this work outside Rain man
    @classmethod
    def counts_cards(cls, players):
        risk = 0
        for player in players:
            for hand in player:
                if hand:
                    for card in hand:
                        if card.value not in (7, 8, 9):
                            if card.value < 10:
                                risk += 1
                            else:
                                risk -= 1
        return risk

    def update_risk(self, card):
        if card.value not in (7, 8, 9):
            if card.value < 10:
                self.__risk += 1
            else:
                self.__risk -= 1

    def ask_for_card(self):
        dealer_points = self.__players[0][0].sum_hand_of_cards()
        wins = 0
        for player in self.__players:
            for hand in player:
                if hand:
                    if hand.sum_hand_of_cards() > dealer_points:
                        wins += 1

        if not wins:
            return True
        else:
            if wins < int(len(self.__players[1:]) / 2):
                if self.__risk >= 2:
                    return True
            else:
                if self.__risk - 2:
                    return True
