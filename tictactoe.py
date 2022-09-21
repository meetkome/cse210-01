"""
Solocode Assignment:Tic-Tac-Toe
Author: Oghenekome Victory Igho
"""

import random

#define global variables
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


#print game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("------------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("------------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)

#take player input
def playerInput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Oops! player already entered that spot")

#check for win or Draw

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

#check for a tie
def checkDraw(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is: {winner}")
    
#switch the player
def switchPlayers():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"

#make computer play 
def computer(board):
    while currentPlayer == "0":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "0"
            switchPlayers()

#check for win or Draw

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkDraw(board)
    switchPlayers()
    computer(board)
    checkWin()
    checkDraw(board)