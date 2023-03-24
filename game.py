from logic import *
import os
import time

#define the board
board = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]
#this flag computes the main loop
#this flag is set to False once the game is over
flag = True

def display(board):
	for row in board:
		print(row)

while(flag):
	#clear the screen
	os.system("clear")
	print("---------------")
	display(board)
	#take input position from user
	move = [int(val) for val in input("Your move? ").split()]
	board[move[0]][move[1]] = player
	#clear the screen
	os.system("clear")
	print("---------------")
	display(board)
	#evaluate the board
	eBoard = evaluate(board)
	#if eBoard = 10 then MAX player i.e. X has WON
	if(eBoard == 10):
		print("Player X Won")
		flag = False
	#if eBoard = 0 and if no moves are left then game is DRAW
	elif (eBoard == 0 and (not isMovesLeft(board))):
		print("DRAW!!")
		flag = False
	print("AI is thinking...")
	#a simple delay of 3 seconds to show that 
	#AI is doing some serious thinking
	time.sleep(3)
	os.system("clear")
	#compute the best move by calling minimax function
	bestMove = findBestMove(board)
	#make the move on the board based on position
	#returned by the function above
	board[bestMove[0]][bestMove[1]] = opponent
	print("---------------")
	display(board)
	#if eBoard = -10 then MIN player i.e. O has WON
	if(evaluate(board) == -10):
		print("Player O Won")
		flag = False
	#if eBoard = 0 and if no moves are left then game is DRAW
	elif (eBoard == 0 and (not isMovesLeft(board))):
		print("DRAW!!")
		flag = False






