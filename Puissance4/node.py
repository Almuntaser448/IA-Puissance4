from board import Board


class Node:
    parent = None
    childs = list()
    value = None
    depth = 0
    grid = None

    def __init__(self, parent, depth):
        self.parent = parent
        self.depth = depth
        if self.parent != None:
            self.grid = self.parent.grid
        else:
            self.grid = Board()

    def addChild(self, node):
        self.childs.append(node)
