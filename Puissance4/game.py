from player import *
from board import *
from miniMax import *
import collections
from MCT import *

class Game:
    player1 = None
    player2 = None
    board = Board()

    def __init__(self):
        name1 = input('Enter name of player 1: ')
        name2 = input('Enter name of player 2: ')
        self.player1 = Player(Piece('R'), name1)
        self.player2 = Player(Piece('Y'), name2)
        self.playerIA = Player(Piece('R'), "IA")

    def start(self):
        players = [self.player1, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
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

    def startIA(self):
        players = [self.playerIA, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
            IA = MiniMax()
            IA.root.board=deepcopy(self.board)
            caseAjouer = IA.createTree(False,2)
            cnt += 1
            if(cnt % 2 == 1):
                self.board.showGrid()
                self.playerIA.playIA(self.board, caseAjouer)
            else:
                self.board.showGrid()
                self.player2.play(self.board)

        # Game finished
        self.board.showGrid()
        self.showWinner(players)

        restart = input('Restart? yes:Y no:Other ')
        if restart.lower() == 'y':
            self.board.reset()
            self.startIA(IA)
    def startIAAlphaBeta(self):
        players = [self.playerIA, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
            IA = MiniMax()
            IA.root.board=deepcopy(self.board)
            caseAjouer=IA.createTree(True)
            cnt += 1
            if(cnt % 2 == 1):
                self.playerIA.playIA(self.board,caseAjouer)
            else:
                 self.board.showGrid()
                 self.player2.play(self.board)

        # Game finished
        self.board.showGrid()
        self.showWinner(players)

        restart = input('Restart? yes:Y no:Other ')
        if restart.lower() == 'y':
            self.board.reset()
            self.startIA(IA)

    def startMCT(self):
        players = [self.playerIA, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
            IA = MCT()
            IA.root.board=deepcopy(self.board)
            caseAjouer=IA.createTree()
            cnt += 1
            if(cnt % 2 == 1):
                self.playerIA.playIA(self.board,caseAjouer)
            else:
                 self.board.showGrid()
                 self.player2.play(self.board)

        # Game finished
        self.board.showGrid()
        self.showWinner(players)

        restart = input('Restart? yes:Y no:Other ')
        if restart.lower() == 'y':
            self.board.reset()
            self.startIA(IA)

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
