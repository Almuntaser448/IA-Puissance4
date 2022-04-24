from board import *
from piece import *
import random
import string


class Player:
    name = str()
    piece = None
    score = 0

    def __init__(self, piece: Piece, name: str):
        if name == '':
            self.name = 'Player_'+self.getRandomName()
        else:
            self.name = name
        self.piece = piece

    def getRandomName(self):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(3))
        return result_str

    def play(self, board):
        print('\nAu tour de ', self.name)
        posX = int(input('Enter postion: '))
        board.placePiece(posX, self)
