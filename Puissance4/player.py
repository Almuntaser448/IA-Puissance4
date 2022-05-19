from board import *
from piece import *
import random
import string


class Player:
    name = str()  # str
    piece = None  # Piece
    score = 0  # int

    def __init__(self, piece: Piece, name: str):
        if name == '':
            self.name = 'Player_'+self.getRandomName()
        else:
            self.name = name
        self.piece = piece

    def getRandomName(self):
        """
        to Complete.
        """
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(3))
        return result_str

    def play(self, board):
        """
        to Complete.
        """
        print('\nAu tour de ', self.name)
        posX = int(input('Enter postion: '))
        board.placePiece(posX, self)

    def playIA(self, board, posX):
        """
        to Complete.
        """
        board.placePiece(posX, self)
