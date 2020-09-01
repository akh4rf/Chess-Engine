"""
Main driver: handles user input & displays objects
"""

import pygame as p
import engine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = WIDTH/8

FPS = 15

IMAGES = {}

def loadImages():
    pieces = {"bR","bN","bB","bK","bQ","bP","wR","wN","wB","wK","wQ","wP"}
    for piece in pieces:
        IMAGES[piece] = p.image.load("assets/" + piece + ".png")

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gamestate = engine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gamestate)    # Draws screen every tick
        clock.tick(FPS)
        p.display.flip()                    # Updates screen every tick

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
    pass

if __name__ == "__main__":
    main()