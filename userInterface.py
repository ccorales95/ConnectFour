# imports
from Board import Board



print("Connect Four!")
print(" 1 2 3 4 5 6 7 \n")
# print Board
userWon = 0
AIWon = 0
while (userWon + AIwon) == 0:
    # get the users 'play'
    play = int(raw_input("Where would you like to play? -> "))
    while (play < 1) or (play > 7):
        print("Sorry. That is not a valid play. Please choose a column from 1 to 7.")
        play = int(raw_input("Where would you like to play? -> "))
    confirm = raw_input("So you would like to play your piece in column " + str(play) + "? (Y/N) -> ")
    while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
        print("Sorry. That is not a valid confirmation. Please input 'Y' if " + str(play) + " is the correct column and 'N' if you would like to choose a different column.")
        confirm = raw_input("So you would like to play your piece in column " + str(play) + "? (Y/N) -> ")
    # put 'play' into the board

    # print the board

    # check if there's a win by user

    # get the AI's play

    # put the AI's play into the board

    # print the board

    # check if there's a win by AI

# the end! (Announce the winner)

