class Board(object):
    def __init__(self, rows, columns):
        self.board = [['_' for x in range (columns)] for y in range (rows)]


    def __str__(self):
        st = ''
        for rownum in range (len(self.board)):
            for entry in range (len(self.board[rownum])):
                st += self.board[rownum][entry] + ' '
            st += '\n'
        return st

board = Board(6, 7)
print board