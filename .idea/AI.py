from Board import Board
import copy

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
    for x in range board.columns:
        if depth == 0:
        #if depth is 0, we've reached the end
            if player == 'x':
                for x in range board.columns:
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'x')
                    potentialscore = heuristic(simulboard)
                    if potentialscore < bestscore:
                        bestscore = potentialscore
                        bestplay = x
            if player == 'o':
                for x in range board.columns:
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'o')
                    potentialscore = heuristic(simulboard)
                    if potentialscore > bestscore:
                        bestscore = potentialscore
                        bestplay = x
            return (bestplay, bestscore)

        else:
            if player == 'x':
                for x in range board.columns:
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'x')
                    (playatx, scoreatx) = minmaxplay(simulboard, depth - 1, 'o')
                    potentialscore = scoreatx
                    if potentialscore < bestscore:
                        bestscore = potentialscore
                        bestplay = x
            if player == 'o':
                for x in range board.columns:
                    simulboard = copy.deepcopy(board)
                    #used to make a copy of the board for the purposes of further simulation
                    simulboard.play(x, 'o')
                    (playatx, scoreatx) = minmaxplay(simulboard, depth - 1, 'x')
                    potentialscore = scoreatx
                    if potentialscore > bestscore:
                        bestscore = potentialscore
                        bestplay = x
            return (bestplay, bestscore)








