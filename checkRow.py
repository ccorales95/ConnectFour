import Board

'''class checkRow:
    # board: represents the list within a list structure
    # player: identifies who is making the move
    # k: the number that you are looking for diagonally, vertically, and horizonatlly
    def __init__(self, board, player, k):
        self.board = board
        self.player = player
        self.k = k

    # compute_k takes the list within a list and then goes through it to check and see
    # how many of the constant k there are'''

def compute_k(board, k, player):
    player_count = 0
    k_count = 0
    rows = board.getRow()
    columns = board.getCol()
    #check horizontally
    for i in range(rows):
        for j in range(columns):
            if board.board[i][j] == player:
                player_count += 1
            else:
                player_count = 0

            if player_count == k:
                k_count +=1

    player_count = 0
    #check vertically
    for j in range(columns):
        for i in range(rows):
            if board.board[i][j] == player:
                player_count += 1
            else:
                player_count = 0

            if player_count == k:
                k_count += 1


    player_count = 0
    # checks diagonally
    for i in range(rows-3):
        for j in range(columns-3):
            for m in range(4):
                if board.board[i+m][j+m] == player:
                    player_count += 1
                else:
                    player_count = 0

                if player_count == k:
                    k_count += 1

    return k_count














