from numpy import False_
from board import Board
from copy import *


class Node:
    parent = None
    childs = []
    value = None
    depth = 0
    horizion = 0
    board = None
    nodeDeRouteMinMax = None
    fin = False
    alpha = None
    beta = None

    def __init__(self, parent, depth, horizion):
        self.childs = []
        self.parent = parent
        self.depth = depth
        self.horizion = horizion
        self.board = Board()
        if self.parent != None:
            self.parent.childs.append(self)
           # self.parent.addChild(self)
            self.board = deepcopy(self.parent.board)

    def addChild(self, node):
        self.childs.append(node)

    def getChilds(self):
        return self.childs
