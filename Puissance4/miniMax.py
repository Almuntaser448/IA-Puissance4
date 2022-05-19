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
        self.playerIA = Player(Piece('R'), 'IAEntrainment')
        self.playerOther = Player(Piece('Y'), 'Other')
        self.arbre = {}

    def createTree(self, avecAlphaBeta, dificulte):
        """
        Method allowing the creation of the tree by assimilating a game state to each node.
        """
        self.root.parent = None
        self.root.beta = 0
        self.root.alpha = 0
        self.root.value = None
        self.root.nodeDeRouteMinMax = None
        self.root.fin = False

        for i in range(5):  # intialisation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[i] = []
        self.arbre[0].append(self.root)
        nodeValide = False
        self.root.valid = True
        for depth in range(4):
            for nodesInDepth in self.arbre[depth]:
                if type(nodesInDepth) == Node:
                    nodesInDepth = [nodesInDepth]
                for nodeParent in nodesInDepth:
                    tempList = []
                    for x in range(7):
                        # separe la jeu de pere
                        currentNode = Node(nodeParent, depth, x)
                        currentNode.board = deepcopy(nodeParent.board)
                        nodeValide = self.updateGrid(currentNode, depth, x)
                        currentNode.valid = nodeValide
                        if nodeValide:
                            tempList.append(currentNode)
                    self.arbre[depth+1].append(tempList)
                    tempList.clear
        for nodeEtage1 in self.root.childs:
            nodeInvalides1 = 0
            if nodeEtage1.valid == True:
                if not(len(nodeEtage1.childs) == 0):
                    for nodeEtage2 in nodeEtage1.childs:
                        if(nodeEtage2.valid == True):
                            nodeInvalides2 = 0

                            if not(len(nodeEtage2.childs) == 0):
                                for nodeEtage3 in nodeEtage2.childs:
                                    if(nodeEtage3.valid):
                                        nodeInvalides3 = 0
                                        if not (len(nodeEtage3.childs)) == 0:
                                            for nodeEtage4 in nodeEtage3.childs:
                                                if(nodeEtage4.valid):
                                                    self.setNodeValue(
                                                        nodeEtage4, dificulte)
                                                else:
                                                    nodeInvalides3 += 1
                                        else:
                                            self.setNodeValue(
                                                nodeEtage3, dificulte)
                                        if(nodeInvalides3 == (len(nodeEtage3.childs))):
                                            self.setNodeValue(
                                                nodeEtage3, dificulte)
                                    else:
                                        nodeInvalides2 += 1
                            else:
                                self.setNodeValue(nodeEtage2, dificulte)
                            if(nodeInvalides2 == (len(nodeEtage2.childs))):
                                self.setNodeValue(nodeEtage2, dificulte)
                        else:
                            nodeInvalides1 += 1
                else:
                    self.setNodeValue(nodeEtage1, dificulte)
                if(nodeInvalides1 == (len(nodeEtage1.childs))):
                    self.setNodeValue(nodeEtage1, dificulte)
        retour = None
        if(avecAlphaBeta):
            retour = self.alphaBetaMinMax(dificulte)
        else:
            retour = self.lancementMinMax()
        return retour

    def lancementMinMax(self):
        """
        Method to launch minmax.

        Return the position to be played by the AI.
        """
        for etage in range(4 - 1, 0 - 1, -1):
            for ListsNodesEtagesActuels in self.arbre[etage]:
                if type(ListsNodesEtagesActuels) == Node:
                    ListsNodesEtagesActuels = [ListsNodesEtagesActuels]
                for NodePere in ListsNodesEtagesActuels:

                    min = 99999
                    max = -99999
                    resNode = None
                    Coupe = True

                    for node in NodePere.childs:
                        if(node.valid == True):
                            Coupe = False
                            if(etage % 2 == 0):  # max
                                if(node.value > max):
                                    max = node.value
                                    resNode = node
                            else:  # min
                                if(node.value < min):
                                    min = node.value
                                    resNode = node
                    if(Coupe == False):
                        if(etage % 2 == 0):
                            NodePere.value = max
                        else:
                            NodePere.value = min

        print("la valeur de la Max choisit est "+str(self.root.value))
        return resNode.horizon

    def alphaBetaMinMax(self, dificulte):
        """
        Methode permettant le lancement de minmax.

        AlphaBeta version.

        Retourne la position à jouer par l'IA
        """
        brouneEtage3 = False
        brouneEtage2 = False
        brouneEtage1 = False
        for nodeEtage1 in self.root.childs:
            nodeInvalides1 = 0
            if nodeEtage1.valid == True:
                if not(len(nodeEtage1.childs) == 0):
                    for nodeEtage2 in nodeEtage1.childs:
                        nodeInvalides2 = 0
                        if nodeEtage2.valid == True:
                            if not(len(nodeEtage2.childs) == 0):
                                for nodeEtage3 in nodeEtage2.childs:
                                    nodeInvalides2 = 0
                                    if nodeEtage2.valid == True:
                                        if not(len(nodeEtage2.childs) == 0):
                                            for nodeEtage4 in nodeEtage3.childs:
                                                if(nodeEtage4.valid == True):
                                                    if(nodeEtage3.value == None):
                                                        self.setNodeValue(
                                                            nodeEtage4, dificulte)
                                                        nodeEtage3.value = nodeEtage4.value
                                                    if nodeEtage4.value < nodeEtage3.value:
                                                        nodeEtage3.value = nodeEtage4.value

                                                    # Min
                                                    if not(nodeEtage2.alpha == None):

                                                        if(nodeEtage2.alpha >= nodeEtage3.value):
                                                            brouneEtage3 = True
                                                            break
                                                    if(nodeEtage3.beta == None):

                                                        nodeEtage3.beta = nodeEtage4.value
                                                    if nodeEtage4.value < nodeEtage3.beta:

                                                        nodeEtage3.beta = nodeEtage4.value
                                            # Max
                                            if (brouneEtage3):
                                                brouneEtage3 = False
                                                continue
                                            if not(nodeEtage1.beta == None):

                                                if(nodeEtage3.value >= nodeEtage1.beta):
                                                    brouneEtage2 = True
                                                    break
                                            if(nodeEtage2.value == None):
                                                if(nodeEtage3.value == None):
                                                    self.setNodeValue(
                                                        nodeEtage2, dificulte)
                                                else:
                                                    nodeEtage2.value = nodeEtage3.value
                                            if(nodeEtage3.valid == True):
                                                if nodeEtage3.value > nodeEtage2.value:

                                                    nodeEtage2.value = nodeEtage3.value
                                                if(nodeEtage2.alpha == None):

                                                    nodeEtage2.alpha = nodeEtage3.value
                                                if nodeEtage3.value > nodeEtage2.alpha:

                                                    nodeEtage2.alpha = nodeEtage3.value
                                  # Min
                                if (brouneEtage2):
                                    brouneEtage2 = False
                                    continue

                                if(nodeEtage1.value == None):
                                    if(nodeEtage2.value == None):
                                        self.setNodeValue(
                                            nodeEtage1, dificulte)
                                    else:
                                        nodeEtage1.value = nodeEtage2.value
                                if not (self.root.alpha == None):
                                    if (self.root.alpha >= nodeEtage1.value):

                                        brouneEtage1 = True
                                        break
                                if(nodeEtage2.valid == True):
                                    if nodeEtage2.value < nodeEtage1.value:

                                        nodeEtage1.value = nodeEtage2.value
                                    if(nodeEtage1.beta == None):
                                        nodeEtage1.beta = nodeEtage2.value
                                    if nodeEtage2.value < nodeEtage1.beta:
                                        nodeEtage1.beta = nodeEtage2.value

            if(self.root.value == None):
                self.root.value = nodeEtage1.value
                nodeEtage1.board.showGrid()
            print(str(nodeEtage1.value) + " :"+str(self.root.value))
            if(nodeEtage1.valid == True):
                if nodeEtage1.value > self.root.value:
                    self.root.value = nodeEtage1.value
                if(self.root.alpha == None):
                    self.root.alpha = nodeEtage1.value
                if self.root.alpha < nodeEtage1.value:
                    self.root.alpha = nodeEtage1.value
            else:
                print(
                    "L'IA ne peut pas traiter cette opton, Merci de essiaer un autre place")

        for nodeAsuivre1 in self.root.childs:
            if self.root.value == nodeAsuivre1.value:
                return nodeAsuivre1.horizon

        return 0

        return finDePredication

    def updateGrid(self, currentNode, depth, x):
        """
        Method to add a piece in the board of a child node according to the one of the father.
        """
        nValide = False
        players = [self.playerIA, self.playerOther]
        actualPlayer = int()
        if depth % 2 == 0:
            actualPlayer = 0
        else:
            actualPlayer = 1
        nValide = currentNode.board.placePiece(x, players[actualPlayer])
        return nValide

    def setNodeValue(self, currentNode, dificulte):
        """
        Methode permettant l'attribution de score à chaque noeud.
        """
        mapJetons = currentNode.board.isFinished()[1]
        if dificulte == 3:  # difficile
            # exemple = mapJetons: {'Y': {3: int(), 2:int()}, 'R': {3: int(), 2:int()}}

            if currentNode.board.winner != None:
                if self.playerIA.piece.color == currentNode.board.winner:
                    currentNode.value = 999999999
                    currentNode.fin = True
                else:
                    currentNode.value = -99999999
            else:
                # currentNode.value = (mapJetons['R'][3]*20 + mapJetons['R'][2]*10) - (
                #    mapJetons['R'][3]*25 + mapJetons['R'][2]*15)
                currentNode.value = (mapJetons['R'][3]*100) + (mapJetons['R'][2]*40) + (
                    mapJetons['Y'][3]*-1000)+(mapJetons['Y'][2]-60)
        elif dificulte == 2:  # moyeene
            if currentNode.board.winner != None:
                if self.playerIA.piece.color == currentNode.board.winner:
                    currentNode.value = 999999999
                    currentNode.fin = True
                else:
                    currentNode.value = -99999999
            else:

                currentNode.value = (mapJetons['R'][3]*1000) + (mapJetons['R'][2]*120) + (
                    mapJetons['Y'][3]*-100)+(mapJetons['Y'][2]-60)
        else:  # facile voir tres facile
            if currentNode.board.winner != None:
                if self.playerIA.piece.color == currentNode.board.winner:
                    currentNode.value = 999999999
                    currentNode.fin = True
                else:
                    currentNode.value = -99999999
            elif mapJetons['R'][3] > 0:
                currentNode.value = 1000
            elif mapJetons['R'][2] > 0:
                currentNode.value = 120
            elif mapJetons['Y'][3] > 0:
                currentNode.value = -100
            elif mapJetons['Y'][2] > 0:
                currentNode.value = -60
            else:
                currentNode.value = 0
