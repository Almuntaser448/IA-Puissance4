from game import *
from miniMax import *


def start():
    gameMode = input('GameMode: (1-Human vs IA, 2-Human vs Human)')

    if gameMode == '1':
        Game().startIA()  # Min Max est nickel
        # Game().startIAAlphaBeta()#alpha beta block au dernier moment il sort de la board
        # Game().startMCT()
    elif gameMode == '2':
        Game().start()


start()
