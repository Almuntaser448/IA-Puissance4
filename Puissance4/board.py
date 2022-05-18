from numpy import place
from player import *


class Board:
    grid = None
    winner = None

    def __init__(self):
        self.grid = [['O']*7 for _ in range(6)]
        self.winner = None

    def isFinished(self):
        mapJetons = {'J': {3: 0, 2: 0}, 'R': {3: 0, 2: 0}}

        # Vertical
        lastPiece = None
        cnt = 0
        for y in range(len(self.grid[0])):
            lastPiece = None
            cnt = 0
            for x in range(len(self.grid)):
                if self.grid[x][y] != lastPiece:
                    lastPiece = self.grid[x][y]
                    if cnt >= 2:
                        mapJetons[lastPiece][cnt] += 1
                    cnt = 0
                if lastPiece != 'O':
                    cnt += 1
                if cnt >= 4:  # jeton l'un apres l'autre
                    self.winner = lastPiece
                    return True

        # Horizontal
        lastPiece = None
        cnt = 0
        for x in range(len(self.grid)):
            lastPiece = None
            cnt = 0
            for y in range(len(self.grid[x])):
                if self.grid[x][y] != lastPiece:
                    lastPiece = self.grid[x][y]
                    if cnt >= 2:
                        mapJetons[lastPiece][cnt] += 1
                    cnt = 0
                if lastPiece != 'O':
                    cnt += 1
                if cnt >= 4:
                    self.winner = lastPiece
                    return True
        # Main diagonal
        lastPiece = None
        cnt = 0
        diagonals = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [2, 0]]
        for pos in diagonals:
            lastPiece = None
            cnt = 0
            while pos[0] < len(self.grid) and pos[1] < len(self.grid[0]):
                if self.grid[pos[0]][pos[1]] != lastPiece:
                    lastPiece = self.grid[pos[0]][pos[1]]
                    if cnt >= 2:
                        mapJetons[lastPiece][cnt] += 1
                    cnt = 0
                if lastPiece != 'O':
                    cnt += 1
                if cnt >= 4:
                    self.winner = lastPiece
                    return True
                pos = pos[0] + 1, pos[1] + 1

        # Second diagonal
        lastPiece = None
        cnt = 0
        diagonals = [[0, 6], [0, 5], [0, 4], [0, 3], [1, 6], [2, 6]]
        for pos in diagonals:
            lastPiece = None
            cnt = 0
            while pos[0] < len(self.grid) and pos[1] >= 0:
                if self.grid[pos[0]][pos[1]] != lastPiece:
                    lastPiece = self.grid[pos[0]][pos[1]]
                    if cnt >= 2:
                        mapJetons[lastPiece][cnt] += 1
                    cnt = 0
                if lastPiece != 'O':
                    cnt += 1
                if cnt >= 4:
                    self.winner = lastPiece
                    return True
                pos = pos[0] + 1, pos[1] - 1
        return (False, mapJetons)

    def placePiece(self, posX: int, Player):
        posY = 6
        fin = True
        for y in range(len(self.grid)):
            try:
                if self.grid[y][posX] == 'O':
                    fin = False
                    posY = y
                    break
            except:
                print('Case non valide')
                Player.play(self)
        if (fin == True):
            print('Case non valide')
            Player.play(self)
        if posY < 6:
            if self.grid[posY][posX] == 'O':
                self.grid[posY][posX] = Player.piece.color
            else:
                self.showGrid()
                print('Case non valide! Veuillez choisir une autre case')
                return Player.play(self)
            return True
        else:
            return False

    def showGrid(self):
        print('')
        for i in range(6-1, 0-1, -1):
            print(self.grid[i])
        xValues = '  '
        for i in range(7):
            xValues += str(i)+'    '
        print('\n'+xValues)

    def reset(self):
        self.__init__()
