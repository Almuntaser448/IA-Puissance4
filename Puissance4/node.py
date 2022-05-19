from board import Board
from copy import *


class Node:
    parent = None  # Node
    childs = []  # list(Node)
    value = None  # float
    depth = 0  # int
    horizon = 0  # int
    board = None  # Board
    nodeDeRouteMinMax = None  # Node
    fin = False  # boolean
    alpha = None  # int
    beta = None  # float
    valid = None  # boolean
    nvisit = None  # int

    def __init__(self, parent, depth, horizon):
        self.nvisit = 0
        self.valid = False
        self.childs = []
        self.parent = parent
        self.depth = depth
        self.horizon = horizon
        self.board = Board()
        if self.parent != None:
            self.parent.childs.append(self)
           # self.parent.addChild(self)
            self.board = deepcopy(self.parent.board)

    def addChild(self, node):
        """
        Method to add children to the node.
        """
        self.childs.append(node)

    def getChilds(self):
        """
        Method to get the childrens of the node.
        """
        return self.childs
