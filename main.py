from sys import argv, stderr
from dependencies import Game


class ToManyPlayersError(Exception):
    pass


def read_args():
    arguments = argv[1:]
    try:
        players = abs(int(arguments[0]))
        if players > 7:
            raise ToManyPlayersError
        return players
    except IndexError:
        stderr.write("python3 main.py NUMBER_OF_PLAYERS\n")
        exit(-1)
    except ToManyPlayersError:
        stderr.write("Number of players between 1 to 7\n")
        exit(-1)


def main():
    number_of_players = read_args()
    game_session = Game(number_of_players)
    while "y" in input("\033[1;34mDo you want to play?[y/n]\033[0;0m").lower():
        game_session.start()
    print("Ok! Good bye!!")



if __name__ == '__main__':
    main()
