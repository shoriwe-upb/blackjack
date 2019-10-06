from .player import Player
from .deck import Deck
from .dealerai import DealerAI


class Game(object):
    def __init__(self, number_of_players):
        self.__number_of_players = number_of_players
        self.__players = self.__create_players(number_of_players)
        self.__deck = Deck()

    @classmethod
    def check_splitable_hand(cls, hand):
        return hand[0].raw_value == hand[1].raw_value

    @classmethod
    def __create_players(cls, number_of_players):
        buffer = []
        for n in range(number_of_players + 1):
            buffer.append(Player(n))
        return buffer

    def divide_start_cards(self):
        self.__deck.shuffle()
        for n in range(2):
            for player in self.__players:
                player[0].add_card(self.__deck.pop())
                # Only do this if the user receive his last start card
                if n:
                    print(player)
                    if self.check_splitable_hand(player[0]) and player.player_id:
                        if player.ask_split_hand():
                            player.split_hand()
                            for hand in player:
                                card = self.__deck.pop()
                                hand.add_card(card)
                            print(player)
                    elif player.player_id == 0 and player[0].check_blackjack():
                        return False
        return True

    def divide_rest_of_game(self):
        for player in self.__players[1:]:
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print("\033[1;34m", player, "\033[0;0m")
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            for hand in player:
                if hand:
                    print("\033[0;32m", "Your Hand:", hand, "\033[0;0m")
                    print("\033[1;31m", "Dealer Hand:", self.__players[0][0], "\033[0;0m")
                    print("\033[0;32m", "Your hand value:", hand.sum_hand_of_cards(), "\033[0;0m")
                    print("\033[1;31m", "Dealer Points:", self.__players[0][0].sum_hand_of_cards(), "\033[0;0m")
                    while hand.sum_hand_of_cards() < 21:
                        if player.ask_for_card():
                            card = self.__deck.pop()
                            print("\033[0;32m", "You got", card, "\033[0;0m")
                            hand.add_card(card)
                        else:
                            break
                        print("\033[0;32m", "Your hand value now:", hand.sum_hand_of_cards(), "\033[0;0m")
                        print("Your hand now:", hand)
                    print("=======Hand results=========")
                    points = hand.sum_hand_of_cards()
                    if points == 21:
                        print("\033[1;32m", "Nice!", "\033[0;0m")
                    elif points < 21:
                        print("\033[1;32m", "You got", points, "\033[0;0m")
                    else:
                        print("\033[1;31m", "You fly far away my friend; with", points, "\033[0;0m")
                    print("============================")
            print()
        print()
        print("------Dealer thinking------")
        print("Dealer starts with:", self.__players[0])
        dealer = DealerAI(self.__players)
        while self.__players[0][0].sum_hand_of_cards() < 21:
            print(self.__players[0])
            if dealer.ask_for_card():
                card = self.__deck.pop()
                print("Dealer receive:", card)
                self.__players[0][0].add_card(card)
                dealer.update_risk(card)
                print("\033[1;31m", "Dealer points now:",self.__players[0][0].sum_hand_of_cards(), "\033[0;0m")
            else:
                break

    def show_winners(self):
        dealer_points = self.__players[0][0].sum_hand_of_cards()
        for player in self.__players:
            if player.player_id:
                print(player)
                for hand in player:
                    if hand:
                        hand_points = hand.sum_hand_of_cards()
                        if hand_points > 21:
                            win = False
                        else:
                            if hand_points < dealer_points:
                                if dealer_points > 21:
                                    win = True
                                else:
                                    win = False
                            elif hand_points > dealer_points:
                                win = False
                            else:
                                if hand.check_blackjack() and not self.__players[0][0].check_blackjack():
                                    win = True
                                else:
                                    win = False
                        if win:
                            print("\033[0;32m", "You win with:", hand, "\033[0;0m")
            else:
                print("\033[1;31m", player, "\033[0;0m")

    def start(self):
        self.__deck.merge_cementery()
        self.__deck.shuffle()
        for player in self.__players:
            player.clean_hands()
        print("------Dividing cards------")
        if self.divide_start_cards():
            print()
            print("------Now it's your time------")
            self.divide_rest_of_game()
            print()
            print("------Checking winners------")
            self.show_winners()
        else:
            print("\033[1;31m", "Sorry but the dealer won", "\033[0;0m")
