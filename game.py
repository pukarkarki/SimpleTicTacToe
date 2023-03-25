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

#clear the screen
os.system("clear")
print("---------------")
display(board)

while(flag):
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
		break
	#if eBoard = 0 and if no moves are left then game is DRAW
	elif (eBoard == 0 and (not isMovesLeft(board))):
		print("DRAW!!")
		flag = False
		break
	print("AI is thinking...")
	#a simple delay of 2 seconds to show that 
	#AI is doing some serious thinking :D :D
	time.sleep(2)
	os.system("clear")
	#compute the bestMove1 by calling minimax function and
	#bestMove2 by calling minimax with alphabeta pruning
	bestMove1, count1, bestMove2, count2 = findBestMove(board)
	print("Best move using minimax ",bestMove1)
	print("The number of time minimax is called is ",count1)
	print("Best move using minimax with alpha beta pruning is ",bestMove2)
	print("The number of time minimax with alpha beta pruning is called is ",count2)
	#make the move on the board based on position
	#returned by any one of the function above
	board[bestMove1[0]][bestMove1[1]] = opponent
	print("---------------")
	display(board)
	#if eBoard = -10 then MIN player i.e. O has WON
	if(evaluate(board) == -10):
		print("Player O Won")
		flag = False
		break
	#if eBoard = 0 and if no moves are left then game is DRAW
	elif (eBoard == 0 and (not isMovesLeft(board))):
		print("DRAW!!")
		flag = False
		break






