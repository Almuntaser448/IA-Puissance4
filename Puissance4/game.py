from player import *
from board import *
from miniMax import *
from MCT import *


class Game:
    player1 = None
    player2 = None
    board = Board()

    def __init__(self):
        self.player1 = Player(Piece('R'), '')
        self.player2 = Player(Piece('Y'), '')
        self.playerIA = Player(Piece('R'), "IA")

    def start(self):
        """
        method of starting a game with two human players.

        Initialize the names of the players.
        """
        name1 = input('Enter name of player 1: ')
        name2 = input('Enter name of player 2: ')
        self.player1.name = name1
        self.player2.name = name2
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
        """
        method of starting a game with two players, one human and one IA.

        Initialize the names of the player and the difficulty.
        """
        name = input('Enter name of player: ')
        difficulty = input('Enter difficulty: (1-Easy, 2-Medium, 3-Hard)')
        try:
            difficulty = int(difficulty)
        except:
            print('Valeur "{}" non reconnue'.format(difficulty))
            return self.startIA()
        self.player2.name = name

        players = [self.playerIA, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
            IA = MiniMax()
            IA.root.board = deepcopy(self.board)
            caseAjouer = IA.createTree(False, difficulty)

            if(cnt % 2 == 0):
                self.board.showGrid()
                self.playerIA.playIA(self.board, caseAjouer)
            else:
                self.board.showGrid()
                self.player2.play(self.board)
            cnt += 1

        # Game finished
        self.board.showGrid()
        self.showWinner(players)

        restart = input('Restart? yes:Y no:Other ')
        if restart.lower() == 'y':
            self.board.reset()
            self.startIA()

    def startIAAlphaBeta(self):
        """
        method of starting a game with two players, one human and one IA.

        AlphaBeta version.

        Initialize the names of the player and the difficulty.
        """
        name = input('Enter name of player: ')
        difficulty = input('Enter difficulty: (1-Easy, 2-Medium, 3-Hard)')
        try:
            difficulty = int(difficulty)
        except:
            print('Valeur "{}" non reconnue'.format(difficulty))
            return self.startIA()
        self.player2.name = name
        players = [self.playerIA, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
            IA = MiniMax()
            IA.root.board = deepcopy(self.board)
            caseAjouer = IA.createTree(True)
            cnt += 1
            if(cnt % 2 == 1):
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

    def startMCT(self):
        """
        method of starting a game with two players, one human and one IA.

        MCTS (Monte Carlo tree search) version.

        Initialize the names of the player and the difficulty.
        """
        name = input('Enter name of player: ')
        difficulty = input('Enter difficulty: (1-Easy, 2-Medium, 3-Hard)')
        try:
            difficulty = int(difficulty)
        except:
            print('Valeur "{}" non reconnue'.format(difficulty))
            return self.startIA()
        self.player2.name = name
        players = [self.playerIA, self.player2]
        cnt = 0
        self.showPlayers(players)

        # Game in progress
        while not self.board.isFinished()[0]:
            IA = MCT()
            IA.root.board = deepcopy(self.board)
            caseAjouer = IA.createTree()
            cnt += 1
            if(cnt % 2 == 1):
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

    def showPlayers(self, players):
        """
        Allows the display of players and their scores
        """
        print('')
        for i in players:
            print(i.name, '- Score:', i.score)

    def showWinner(self, players):
        """
        Allows the display of the winner
        """
        if self.board.winner != None:
            for player in players:
                if player.piece.color == self.board.winner:
                    player.score += 1
                    print(player.name, 'win this round!')
        else:
            print('Game Finished')
