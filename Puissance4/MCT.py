from numpy import True_
from board import Board
from node import *
from player import *
import random
import math 
import numpy as np
class MCT:
    root = None
    nodesByDepth = None
    playerIA = None
    playerOther = None
    arbre = None
    visited=None
    def __init__(self):
        self.root = Node(None, 0, 100)
        self.nodes = {'0': [self.root]}
        self.playerIA = Player(Piece('R'), 'IAEntrainment')
        self.playerOther = Player(Piece('Y'), 'Other')
        self.arbre = {}
        self.visited= {}
    def UCB1(self,noeud):
        if(noeud.value==None):
             val=0
        else:
            val=noeud.value/noeud.nvisit
        N=self.root.nvisit
        if(noeud.nvisit==0):
            return 9999999
        n=noeud.nvisit
        return val +2*(math.sqrt(np.log(N)/n))
    def createTree(self):
        self.root.parent = None
        self.root.value = None
        self.root.fin = False

        for i in range(2):  # intialisation de dicctionaire 7 car il y a le root qui n'est pas des situations de case mais c'est le max qui regroupe tout les enfants donc il n'est pas la physiqument
            self.arbre[i] = []
        self.arbre[0].append(self.root)
        nodeValide = False
        self.root.valid=True
        for depth in range(1):
            for nodesInDepth in self.arbre[depth]:
                if type(nodesInDepth) == Node:
                    nodesInDepth = [nodesInDepth]
                for nodeParent in nodesInDepth:
                    tempList = []
                    for x in range(7):
                        # separe la jeu de pere
                        currentNode = Node(nodeParent, depth, x)
                        currentNode.board=deepcopy(nodeParent.board)
                        nodeValide = self.updateGrid(currentNode, depth, x)
                        currentNode.valid=nodeValide
                        if nodeValide:
                            tempList.append(currentNode)
                    self.arbre[depth+1].append(tempList)
                    tempList.clear

        for i in range (3):
            print(i)
            maxucb=0
            noeudAresoudre=None
            nodeAchoisir=None
            for nodeAvisiter in self.root.childs:
                   if self.UCB1(nodeAvisiter)>maxucb:
                    maxucb=self.UCB1(nodeAvisiter)
                    nodeAchoisir=nodeAvisiter
       
            while (len(nodeAchoisir.childs)>0):
                
                maxucb=0
                for ch in nodeAchoisir.childs:
                    if self.UCB1(ch)>maxucb:
                     maxucb=self.UCB1(ch)
                     noeudAresoudre=ch
                nodeAchoisir=noeudAresoudre
            

            if(nodeAchoisir.nvisit==0):
                   nodeAchoisir.value=self.rollOut(nodeAchoisir)
                   while (nodeAchoisir.parent!=None):
                        nodeAchoisir.parent.nvisit+=1
                        nodeAchoisir.parent.valeur+=nodeAchoisir.valeur
                        nodeAchoisir=nodeAchoisir.parent
            else:
                                tempList = []
                                for x in range(7):
                                    # separe la jeu de pere
                                    currentNode = Node(nodeAchoisir, depth, x)
                                    currentNode.board=deepcopy(nodeAchoisir.board)
                                    nodeValide = self.updateGrid(currentNode, depth, x)
                                    currentNode.valid=nodeValide
                                    if nodeValide:
                                        tempList.append(currentNode)
                                self.arbre[len(self.arbre)].append(tempList)
                                tempList.clear
        max=0
        hor=0
        for enf in self.root.childs:
            if(enf.value==None):
                continue
            if(enf.value>max):
                max=enf.value
                hor=enf.horizon
        return hor
    def rollOut(self,noeud):
        tempNoe=deepcopy(noeud)
        finPositive=999999
        finNegative=-999999
        while True:
            if tempNoe.board.winner != None:
               
                if self.playerIA.piece.color == tempNoe.board.winner:
                    return finPositive
                else:
                    return finNegative
            else:
                finPositive-=1
                finNegative+=1
                tempNoe.board.placePiece(random.randint(0,6),self.playerOther)
                tempNoe.board.placePiece(random.randint(0,6),self.playerIA) 


    def updateGrid(self, currentNode, depth, x):
        nValide = False
        players = [self.playerIA, self.playerOther]
        actualPlayer = int()
        if depth % 2 == 0:
            actualPlayer = 0
        else:
            actualPlayer = 1
        nValide = currentNode.board.placePiece(x, players[actualPlayer])
        return nValide