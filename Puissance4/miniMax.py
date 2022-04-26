from numpy import True_
from board import Board
from node import *
from player import *


class MiniMax:
    root = None
    nodesByDepth = None
    playerIA = None
    playerOther = None
    arbre = None

    def __init__(self):
        self.root = Node(None, 0, 100)
        self.nodes = {'0': [self.root]}
        self.playerIA = Player(Piece('R'), 'IA')
        self.playerOther = Player(Piece('Y'), 'Other')
        self.arbre = {}
        self.createTree()
        # self.lancementMinMax()

    def createTree(self):
        for i in range(43):  # intialsation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[i] = []
        self.arbre[0].append([self.root])
        nodeValide=False
        for depth in range(42):
            print(depth)
            for nodesInDepth in self.arbre[depth]:
                for nodeParent in nodesInDepth:
                    tempList = []
                    for x in range(7):
                        currentNode = Node(nodeParent, depth, x) #separe la jeu de pere
                       
                        nodeValide=self.updateGrid(currentNode, depth, x)
                        if nodeValide :
                            tempList.append(currentNode)
                    self.arbre[depth+1].append(tempList)

    def lancementMinMax(self):
        for etage in range(6):
            for ListsNodesEtagesActuels in self.arbre[5-etage]:
                for NodePere in ListsNodesEtagesActuels:
                    if NodePere.fin:
                        continue
                    min = 3
                    max = -3

                    for node in NodePere.childs:
                        ilyaNodes = False
                        if not node.fin:
                            ilyaNodes = True
                        else:
                            continue
                        if(etage % 2 == 0):  # min because it's 1 3 5
                            if(node.value < min):
                                min = node.value
                        else:
                            if(node.value > max):
                                max = node.value
                    if ilyaNodes:
                        if(etage % 2 == 0):
                            NodePere.value = min
                        else:
                            NodePere.value = max

    def updateGrid(self, currentNode, depth, x):
        nValide=False
        players = [self.playerIA, self.playerOther]
        actualPlayer = int()
        if depth % 2 == 0:
            actualPlayer = 0
        else:
            actualPlayer = 1
        nValide=currentNode.board.placePiece(x, players[actualPlayer])
        if currentNode.board.isFinished():
            self.setNodeValue(currentNode)
        return nValide
    def setNodeValue(self, currentNode):
        if currentNode.board.winner != None:
            if self.playerIA.piece.color == currentNode.board.winner:
                currentNode.value = 1
            else:
                currentNode.value = -1
        else:
            currentNode.value = 0
        currentNode.fin = True
