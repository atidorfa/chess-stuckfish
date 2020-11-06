import numpy as np

"""
This class is responsible for storing all information about the current state of a chess game. 
It also be responsible for determining the valid moves at the current state. It will also keep a move log.
"""

class GameState():
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []

    '''
    Take a move as a parameter and execute it(this will not work for casteling, pawn promotion and en-passant)
    '''
    def makeMove(self, move):
        self.board[move.startX][move.startY] = "--"
        self.board[move.endX][move.endY] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

    '''
    Undo the last move made
    '''
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startX][move.startY] = move.pieceMoved
            self.board[move.endX][move.endY] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    '''
    All moves considering checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    '''
    All moves withouth considering checks
    '''
    def getAllPossibleMoves(self):
        moves = [Move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)): #number of rows
            for c in range(len(self.board[r])): #number of columns in given row
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
        
        return moves

    '''
    Get all the pawn moves for the pawn located at row, col and add these moves to the list
    '''
    def getPawnMoves(self, r, c, moves):
        pass

    '''
    Get all the rook moves for the pawn located at row, col and add these moves to the list
    '''
    def getRookMoves(self, r, c, moves):
        pass


class Move():

    #map -> key: value

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startX = startSq[0]
        self.startY = startSq[1]
        self.endX = endSq[0]
        self.endY = endSq[1]
        self.pieceMoved = board[self.startX][self.startY]
        self.pieceCaptured = board[self.endX][self.endY]
        self.moveID = self.startX * 1000 + self.startY * 100 + self.endX * 10 + self.endY
        print(self.moveID)

    '''
    Overriding the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        #make this like real chess notation in future
        return self.getRankFile(self.startX, self.startY) + self.getRankFile(self.endX, self.endY)

    def getRankFile(self, x, y):
        return self.colsToFiles[y] + self.rowsToRanks[x]