"""
Main driver: handles user input & displays objects
"""

import pygame as p
from engine import GameState
from engine import Move

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = WIDTH//8

FPS = 15

IMAGES = {}

def loadImages():
    pieces = {"bR","bN","bB","bK","bQ","bP","wR","wN","wB","wK","wQ","wP"}
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("assets/" + piece + ".png"), (SQUARE_SIZE,SQUARE_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gamestate = GameState()
    loadImages()
    running = True
    selected_square = ()                                # Stores previously-clicked square
    clicks = []                                         # [(6,4),(4,4)] moves white pawn forward two
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            if e.type == p.MOUSEBUTTONDOWN:
                mouse_position = p.mouse.get_pos()      # Gives (x, y) location of mouse
                col = mouse_position[0]//SQUARE_SIZE
                row = mouse_position[1]//SQUARE_SIZE
                if (selected_square == (row, col)):
                    selected_square = ()                # If already selected, deselect
                    clicks = []                         # Clear clicks
                else:
                    selected_square = (row, col)
                    clicks.append(selected_square)
                if (len(clicks) == 2):
                    move = Move(clicks[0], clicks[1], gamestate.board)
                    print(move.getChessNotation())
                    gamestate.makeMove(move)
                    selected_square = ()
                    clicks = []

        drawGameState(screen, gamestate)                # Draws screen every tick
        clock.tick(FPS)
        p.display.flip()                                # Updates screen every tick

## Package the draw methods for the board and the pieces, and execute in that order ##
def drawGameState(screen, gamestate):
    drawBoard(screen)
    drawPieces(screen, gamestate.board)

## Draw alternating colors for chessboard ##
def drawBoard(screen):
    colors = [p.Color("white"),p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen, color, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

## Draw pieces ##
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

if __name__ == "__main__":
    main()