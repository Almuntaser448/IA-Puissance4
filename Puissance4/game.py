from player import *
from board import *
from miniMax import *


class Game:
    player1 = None
    player2 = None
    board = Board()

    def __init__(self):
        name1 = input('Enter name of player 1: ')
        name2 = input('Enter name of player 2: ')
        self.player1 = Player(Piece('R'), name1)
        self.player2 = Player(Piece('Y'), name2)

    def start(self):
        players = [self.player1, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished():
            self.board.showGrid()
            cnt += 1
            players[int(cnt % 2 == 0)].play(self.board)

        # Game finished
        self.board.showGrid()
        self.showWinner(players)

        restart = input('Restart? yes:Y no:Other ')
        if restart.lower() == 'y':
            self.board.reset()
            self.start()

    def showPlayers(self, players):
        print('')
        for i in players:
            print(i.name, '- Score:', i.score)

    def showWinner(self, players):
        if self.board.winner != None:
            for player in players:
                if player.piece.color == self.board.winner:
                    player.score += 1
                    print(player.name, 'win this round!')
        else:
            print('Game Finished')
