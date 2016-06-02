from Board import Board
import copy

board = Board(6, 7)

def playonboard(board):
    board.play(0, 'x')
    return

simulboard = copy.deepcopy(board)
playonboard(simulboard)
print(board)