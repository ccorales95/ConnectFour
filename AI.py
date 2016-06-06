from Board import Board
import copy
from checkRow import compute_k
import random

def minmaxplay(board, depth, player):
    #this is a minmax algorithm
    #basically, player x will attempt to minimize the score
    #player o will attempt to maximize the score
    #score will range from -1000 to 1000
    #starting from one player, the algorithm will attempt to recursively pick the best sequence of moves
    #for both players based on the evaluation of some heuristic
    #the heuristic, in particular, will be maximized in the event of a win condition for player o
    #and will be higher in the event of many 'three in a row' or 'n - 1' in a row' sequences for player o
    #the opposite will apply for player x
    #depending on the player we're gonna try to minimize or maximize heuristicscore
    bestscore = 0
    if player == 'x':
        bestscore = 1000
    if player == 'o':
        bestscore = -1000
    bestplay = -1
    #this stores the best candidate for a good play
    for x in range (board.columns):
        if depth == 0:
        #if depth is 0, we've reached the end
            if player == 'x':
                for x in range (board.columns):
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'x')
                    potentialscore = heuristic(simulboard)
                    if potentialscore < bestscore:
                        bestscore = potentialscore
                        bestplay = x
            if player == 'o':
                for x in range (board.columns):
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'o')
                    potentialscore = heuristic(simulboard)
                    if potentialscore > bestscore:
                        bestscore = potentialscore
                        bestplay = x
            if bestplay == -1:
                bestplay = random.randint(0, 6)
            return (bestplay, bestscore)

        else:
            if player == 'x':
                for x in range (board.columns):
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'x')
                    (playatx, scoreatx) = minmaxplay(simulboard, depth - 1, 'o')
                    potentialscore = scoreatx
                    if potentialscore < bestscore:
                        bestscore = potentialscore
                        bestplay = x
            if player == 'o':
                for x in range (board.columns):
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'o')
                    (playatx, scoreatx) = minmaxplay(simulboard, depth - 1, 'x')
                    potentialscore = scoreatx
                    if potentialscore > bestscore:
                        bestscore = potentialscore
                        bestplay = x
            if bestplay == -1:
                bestplay = random.randint(0, 6)
            return (bestplay, bestscore)


def heuristic(board):
    #if a winning position, then maxes out the score
    if compute_k(board, 4, 'x') >= 1:
        return -1000
    if compute_k(board, 4, 'o') >= 1:
        return 1000
    #the heuristic just cgunts the number of 3 in a rows, because this is a good indicator for whether a
    #position is strong in connect four
    #it's a bit dumb, but all we need about the heurscore is its ordering.
    #as it's defined, it will probably only go up to about 10 or so in a normal game, but that doesn't matter
    heurscore = compute_k(board, 3, 'o') - compute_k(board, 3, 'x')
    return heurscore

