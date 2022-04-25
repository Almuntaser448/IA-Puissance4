from board import Board
from copy import copy


class Node:
    parent = None
    childs = list()
    value = None
    depth = 0
    horizion = 0
    board = None

    def __init__(self, parent, depth, horizion):
        self.parent = parent
        self.depth = depth
        self.horizion = horizion
        self.board = Board()
        if self.parent != None:
            self.board = copy(self.parent.board)

    def addChild(self, node):
        self.childs.append(node)
