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

    def makeMove(self, move):
        self.board[move.startX][move.startY] = "--"
        self.board[move.endX][move.endY] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove

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
        
    def getChessNotation(self):
        #make this like real chess notation in future
        return self.getRankFile(self.startX, self.startY) + self.getRankFile(self.endX, self.endY)

    def getRankFile(self, x, y):
        return self.colsToFiles[y] + self.rowsToRanks[x]