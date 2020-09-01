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