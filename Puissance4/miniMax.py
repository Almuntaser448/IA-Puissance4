from board import Board
from node import *
from player import *


class MiniMax:
    root = None
    nodesByDepth = None
    playerIA = None
    playerOther = None

    def __init__(self):
        self.root = Node(None, 0)
        self.nodes = {'0': [self.root]}
        self.playerIA = Player(Piece('R'), 'IA')
        self.playerOther = Player(Piece('Y'), 'Other')

        self.createTree()

    def createTree(self):

        self.root.grid.placePiece(0, self.playerIA)
        self.root.grid.placePiece(1, self.playerIA)
        self.root.grid.placePiece(2, self.playerIA)
        self.root.grid.placePiece(3, self.playerIA)
        if self.root.grid.isFinished():
            if self.root.grid.winner != None:
                if self.root.grid.winner == 'R':
                    self.root.value = 1
                elif self.root.grid.winner == 'Y':
                    self.root.value = -1
                else:
                    self.root.value = 0

    def showTree(self):
        print(self.root.grid.showGrid())
        print(self.root.value)
