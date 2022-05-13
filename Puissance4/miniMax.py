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
        #es=0
        for i in range(5):  # intialsation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[i] = []
        self.arbre[0].append([self.root])
        nodeValide=False
        for depth in range(4):
            for nodesInDepth in self.arbre[depth]:
                for nodeParent in nodesInDepth:
                    tempList = []
                    for x in range(7):
                        currentNode = Node(nodeParent, depth, x) #separe la jeu de pere
                       
                        nodeValide=self.updateGrid(currentNode, depth, x)
                        if nodeValide :
                            #es=es+1
                            tempList.append(currentNode)
                    self.arbre[depth+1].append(tempList)
                    #if(depth==3) and (x==6):
                        #print(es)
#le chemain va etre connu dans un list ou stack par example,
#a chaque etape je vais ajouter deux jetons dans mon stack
#avant que je l'ajoute je dois verifer bien que l'etat actuel de jeu est presnent dans le stack (par example le joeur peut choisir un cas pire pour lui donc le stack n'est plus valide)
#si l'etat actuel de jeu n'est pas la je dois vider mon stack et le remplire a nouveux
#si dans le stack j'arrive a un cas ou j'ai gange j'arrete la recherche de min max
#le stack doit etre FIFO soit First In First Out, car je vais ajourer le board par ordre et je voulais qu'il sort par ordre
#je dois ajouter une methode de recouperer les noeuds dans le board comme ca je peux recree le board dans le stock dans mon jeu actuel

#un autre moyenne de faire la jeu difficille est de fair un programe qui choisit entre les diffrents strategies des  joeur et adopter celui qui le convient le miileux

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
       # currentNode.board.showGrid()
        if currentNode.board.isFinished():
            self.setNodeValue(currentNode)
        return nValide

    #score difficult
    #1 alone=0
    #oponent alone=-1
    #2 in a row=10
    #opponent 2 in a row =-15
    #3 in a row =100
    #opponent 3 in a row= -1000
    #oponent 4 in a row= - 99999999
    #4 in a row = 999999999
    def setNodeValue(self, currentNode):
        if currentNode.board.winner != None:
            if self.playerIA.piece.color == currentNode.board.winner:
                currentNode.value = 1
            else:
                currentNode.value = -1
        else:
            currentNode.value = 0
        currentNode.fin = True
