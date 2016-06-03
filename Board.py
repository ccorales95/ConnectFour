class Board(object):
    def __init__(self, rows, columns):
        self.board = [['_' for x in range (columns)] for y in range (rows)]
        self.rows = rows
        self.columns = columns


    def __str__(self):
        st = ''
        for rownum in range (len(self.board)):
            for entry in range (len(self.board[rownum])):
                st += self.board[rownum][entry] + ' '
            st += '\n'
        return st

    def play(self, column, char):
        #in this method, rownum starts counting from the bottom
        for rownum in range (self.rows):
            if self.board[self.rows - 1 - rownum][column] == '_':
                self.board[self.rows - 1 - rownum][column] = char
                return
        #flow only reaches this point if none of the entries in that column is empty
        print ('Invalid play- column is full')

    def getCol(self):
        # method to get the number of columns
        return self.columns

    def getRow(self):
        # method to get the number of rows
        return self.rows

'''
board = Board(6, 7)
board.play(1, 'x')
board.play(1, 'x')
board.play(1,'o')
board.play(2, 'o')
board.play(3, 'x')
print board.board
'''