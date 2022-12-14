"""
Solocode Assignment:Tic-Tac-Toe
Author: Oghenekome Victory Igho
"""

import random
def main():
   
    #define global variables
    board = createBoard()
    currentPlayer = "X"
    winner = None
    gameRunning = True

    while gameRunning:
        createBoard()
        printBoard(board)
        playerInput(currentPlayer, board)
        checkWin(board)
        checkDraw(board)
        checkHorizontal(board)
        switchPlayers(currentPlayer)
        computer(currentPlayer, board)
        checkWin(board)
        checkDraw(board)

# create the game board
def createBoard():
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    return board

#print game board
def printBoard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("------------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("------------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# take player input
def playerInput(currentPlayer, board):
    # global currentPlayer
    global gameRunning
    inp = int(input("Please enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops! player already entered that spot")


# #check for win or Draw

def checkHorizontal(board):
    #use variable outside function"
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[3]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

# #check for a tie
def checkDraw(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin(board):
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is: {winner}")



#switch the player
def switchPlayers(currentPlayer):
    if currentPlayer == "X":
        # currentPlayer = "O"
        return "O"
    else:
        # currentPlayer = "X"
        return "X"
#make computer play 
def computer(currentPlayer, board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayers(currentPlayer)


#check for win or Draw
if __name__ == "__main__":
    main()