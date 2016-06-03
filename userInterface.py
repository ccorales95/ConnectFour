# imports
from Board import Board
from checkRow import compute_k

myBoard = Board(6, 7)

print("Connect Four! (2 Player)\n")

print("1 2 3 4 5 6 7")
print(myBoard)  # print Board

user1Won = 0
user2Won = 0
stalemate = 0
while (user1Won + user2Won + stalemate) == 0:
    # get user1's 'play'
    print("Player 1: it's your turn!")
    validPlay = False
    while not validPlay:
        play = int(raw_input("Where would you like to play? -> "))
        while (play < 1) or (play > 7):
            print("Sorry. That is not a valid play. Please choose a column from 1 to 7.")
            play = int(raw_input("Where would you like to play? -> "))
        confirm = raw_input("So you would like to play your piece in column " + str(play) + "? (Y/N) -> ")
        while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
            print("Sorry. That is not a valid confirmation. Please input 'Y' if " + str(
                play) + " is the correct column and 'N' if you would like to choose a different column.")
            confirm = raw_input("So you would like to play your piece in column " + str(play) + "? (Y/N) -> ")
        # put user1's play into the board
        validPlay = myBoard.play(play-1, 'o')
    # print the board
    print("1 2 3 4 5 6 7")
    print(myBoard)  # print Board
    # check if there's a win by user1
    user1Won = compute_k(myBoard, 4, 'o')
    if user1Won > 0:
        break;

    # get user2's play
    print("Player 2: it's your turn!")
    validPlay = False
    while not validPlay:
        play = int(raw_input("Where would you like to play? -> "))
        while (play < 1) or (play > 7):
            print("Sorry. That is not a valid play. Please choose a column from 1 to 7.")
            play = int(raw_input("Where would you like to play? -> "))
        confirm = raw_input("So you would like to play your piece in column " + str(play) + "? (Y/N) -> ")
        while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
            print("Sorry. That is not a valid confirmation. Please input 'Y' if " + str(
                play) + " is the correct column and 'N' if you would like to choose a different column.")
            confirm = raw_input("So you would like to play your piece in column " + str(play) + "? (Y/N) -> ")
        # put user2's play into the board
        validPlay = myBoard.play(play-1, 'x')
    # print the board
    print("1 2 3 4 5 6 7")
    print(myBoard)  # print Board
    # check if there's a win by user2
    user2Won = compute_k(myBoard, 4, 'x')
    if user2Won > 0:
        break;

# the end! (Announce the winner)
if user1Won > 0:
    print("Player 1 Won!!!")
if user2Won > 0:
    print("Player 2 Won!!!")