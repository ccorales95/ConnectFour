from Board import Board
import copy
from AI import minmaxplay

board = Board(6, 7)
board.play(2, 'x')
board.play(6, 'o')
board.play(3, 'x')
board.play(2, 'o')
board.play(4, 'x')
print minmaxplay(board, 3, 'o')