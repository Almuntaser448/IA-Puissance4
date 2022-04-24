from board import Board
from node import *
from player import *


class MiniMax:
    root = None
    nodesByDepth = None
    playerIA = None
    playerOther = None
    arbre= None
    def __init__(self):
        self.root = Node(None, 0,100)
        self.nodes = {'0': [self.root]}
        self.playerIA = Player(Piece('R'), 'IA')
        self.playerOther = Player(Piece('Y'), 'Other')
        self.arbre={}
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
        for et in range(7):# intialsation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[et] = []
        self.arbre[0].append([self.root])
        for etage in range(6):
            for ListsNodesEtagesActuels in self.arbre[etage]:
                for NodePere in ListsNodesEtagesActuels:
                    listtemp=[]
                    for horizion in range(7):
                        noeudAct= Node(NodePere, etage,horizion)
                        NodePere.addChild(noeudAct)
                        listtemp.append(noeudAct)
                    self.arbre[etage+1].append(listtemp)


    def showTree(self):
        print(self.root.grid.showGrid())
        print(self.root.value)
