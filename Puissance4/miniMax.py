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
        print(self.root.board.showGrid())

    def createTree(self):

        if self.root.board.isFinished():
            if self.root.board.winner != None:
                if self.root.board.winner == 'R':
                    self.root.value = 1
                elif self.root.board.winner == 'Y':
                    self.root.value = -1
                else:
                    self.root.value = 0
        for et in range(7):  # intialsation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[et] = []
        self.arbre[0].append([self.root])
        for etage in range(6):
            for ListsNodesEtagesActuels in self.arbre[etage]:
                for NodePere in ListsNodesEtagesActuels:
                    listtemp = []
                    for horizion in range(7):
                        noeudAct = Node(NodePere, etage, horizion)
                        NodePere.addChild(noeudAct)
                        listtemp.append(noeudAct)
                        if not noeudAct.fin:
                            self.updateGrid(noeudAct, horizion, etage)
                    self.arbre[etage+1].append(listtemp)

    def showTree(self):
        print(self.root.board.showGrid())
        print(self.root.value)


    def lancementMinMax(self):#attention certain en bas n'ont pas de valeur car le gris  a fini avant
       for etage in range (6):
         for ListsNodesEtagesActuels in self.arbre[5-etage]:
             for NodePere in ListsNodesEtagesActuels:
                  if NodePere.fini:
                      continue
                  min=3
                  max=-3
                  
                  for node in NodePere.getChilds:
                      ilyaNodes=False
                      if not node.fini:
                          ilyaNodes=True
                      else:
                          continue
                      if(etage % 2 == 0):#min because it's 1 3 5
                          if(node.value<min):
                              min=node.value
                      else:
                          if(node.value>max):
                              max=node.value
                  if ilyaNodes:
                      if(etage % 2 == 0):
                        NodePere.value=min
                      else:
                          NodePere.value=max

    def updateGrid(self, noeudAct, horizion, etage):
        players = [self.playerIA, self.playerOther]
        actualPlayer = int()
        if etage % 2 == 0:
            actualPlayer = 0
        else:
            actualPlayer = 1
        noeudAct.board.placePiece(horizion, players[actualPlayer])
        if noeudAct.board.isFinished():
            if noeudAct.board.winner != None:
                if self.playerIA.piece.color == self.board.winner:
                    noeudAct.value=1
                else:
                    noeudAct.value=-1
            else:
                noeudAct.value=0
            for noeud in noeudAct.getChilds:
                noeud.fin=True
