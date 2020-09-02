"""
Stores info about current game state & determines valid moves.
"""

class GameState():
    def __init__(self):
        ## Board is 8x8 array of string arrays, with each space being
        ## represented as board[row][column]. The ordering is correct
        ## within each array (the first element is a, second is b, etc.)
        ## but the ordering for columns is reversed (the first array is
        ## the 8th row on the board, as shown below).
        self.board = [
            # a    b    c    d    e    f    g    h
            ["bR","bN","bB","bK","bQ","bB","bN","bR"], # 8
            ["bP","bP","bP","bP","bP","bP","bP","bP"], # 7
            ["--","--","--","--","--","--","--","--"], # 6
            ["--","--","--","--","--","--","--","--"], # 5
            ["--","--","--","--","--","--","--","--"], # 4
            ["--","--","--","--","--","--","--","--"], # 3
            ["wP","wP","wP","wP","wP","wP","wP","wP"], # 2
            ["wR","wN","wB","wK","wQ","wB","wN","wR"]  # 1
            # a    b    c    d    e    f    g    h
        ]
        self.whiteToMove = True
        self.moveLog = []
    
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append[move]
        self.whiteToMove = not self.whiteToMove

class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                    "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                    "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}


    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startCol = startSquare[1]
        self.endRow = endSquare[0]
        self.endCol = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)

    def getRankAndFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]