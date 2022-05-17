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
        self.root.parent = None
        self.root.value = None
        self.root.nodeDeRouteMinMax = None
        self.root.fin=False
        for i in range(5):  # intialsation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[i] = []
        self.arbre[0].append(self.root)
        nodeValide=False
        for depth in range(4):
            for nodesInDepth in self.arbre[depth]:
                for nodeParent in nodesInDepth:
                    tempList = []
                    for x in range(7):
                        currentNode = Node(nodeParent, depth, x) #separe la jeu de pere
                        nodeValide=self.updateGrid(currentNode, depth, x)
                        if nodeValide :
                            if(depth==3):
                                self.setNodeValue(currentNode)
                            tempList.append(currentNode)
                    self.arbre[depth+1].append(tempList)


#methode d'arret? pour diffrencier deux jetons libre a deux jetons que le adversaire a arrete 


#pas arreter = les autres sont vide

#il faut voir que si il y a par example 3 pour moi et 3 pour lui le programe peut avoir deux score diffrentes

#trois trois pas le meme score que un seul trois
#plus important deux deux que un seul trois
#savoir si le node apartien a la noudes joues?
#example : if list of the three contains le node qui vient d'etre jouer : score =?



#un autre moyenne de faire la jeu difficille est de fair un programe qui choisit entre les diffrents strategies des  joeur et adopter celui qui le convient le miileux

    def lancementMinMax(self,etapeAfaire):
        finDePredication=False
        for etage in range(4):
            for ListsNodesEtagesActuels in self.arbre[3-etage]:
                for NodePere in ListsNodesEtagesActuels:

                    min =0
                    max =0

                    for node in NodePere.childs:
                        #niveua 4 car c'est 0 1 2 3 4
                        if(etage % 2 == 1):  # min because it's 1 3
                            if(node.value < min):
                                min = node.value
                            if(node.fin==True):
                                finDePredication=True
                        else:
                            if(node.value > max):
                                max = node.value
                            if(node.fin==True):
                                finDePredication=True
                        for node in NodePere.childs:
                             if(etage % 2 == 1):  # min because it's 1 3
                                    if(node.value == min):
                                        NodePere.nodeDeRouteMinMax=node
                                        break
                             else:
                                if(node.value == max):
                                     NodePere.nodeDeRouteMinMax=node
                                     break
                    if(etage % 2 == 1):
                            NodePere.value = min
                    else:
                          NodePere.value = max
        self.arbre.clear()
        etapeAfaire.append(self.root.nodeDeRouteMinMax)
        etapeAfaire.append(self.root.nodeDeRouteMinMax.nodeDeRouteMinMax)
        etapeAfaire.append(self.root.nodeDeRouteMinMax.nodeDeRouteMinMax.nodeDeRouteMinMax)
        dernierNodeVu=self.root.nodeDeRouteMinMax.nodeDeRouteMinMax.nodeDeRouteMinMax.nodeDeRouteMinMax
        etapeAfaire.append(dernierNodeVu)
        self.root=dernierNodeVu
        return finDePredication




    def updateGrid(self, currentNode, depth, x):
        nValide=False
        players = [self.playerIA, self.playerOther]
        actualPlayer = int()
        if depth % 2 == 0:
            actualPlayer = 0
        else:
            actualPlayer = 1
        nValide=currentNode.board.placePiece(x, players[actualPlayer])
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
                currentNode.value = 999999999
                currentNode.fin=True
            else:
                currentNode.value = -99999999
        else:
            if (methode de 3):
                if self.playerIA:
                    currentNode.value =100
                else:
                    currentNode.value =-1000
            elif (methode de 2):
                if self.playerIA:
                    currentNode.value =60
                else:
                    currentNode.value =-70
           else:
               currentNode.value =0
