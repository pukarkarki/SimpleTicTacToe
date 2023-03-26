import tkinter as tk
import time
import os
import sys
from logic import *


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Tic-Tac-Toe")

        #Set geometry (widthxheight)
        master.geometry('270x300')
        #Player is X
        self.player = 'X'
        #Opponent is O
        self.opponent = 'O'
        #Define the board
        self.board = [[ '_', '_', '_' ],
	                  [ '_', '_', '_' ],
                      [ '_', '_', '_' ]]
        #Define an array to store button objects
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        #Generate buttons
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    self.master,
                    text=" ",
                    font=("Helvetica", 30),
                    width=3,
                    height=2,
                    command=lambda row=row, col=col: self.on_button_click(row, col),
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        self.status_var = tk.StringVar()
        self.status_var.set("Player X turn")
        self.status_label = tk.Label(self.master, textvariable=self.status_var)
        self.status_label.grid(row=3, column=0, columnspan=3)
        self.resetButton = tk.Button(
                    self.master,
                    text="Reset",
                    font=("Helvetica", 10),
                    fg='RED',
                    width=1,
                    height=1,
                    command= reset,
                )
        self.resetButton.grid(row=4, column=0, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == "_":
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            self.status_var.set("Player O is thinking")
            root.update_idletasks()
            time.sleep(2)
            bestMove1, count1, bestMove2, count2 = findBestMove(self.board)
            print("The best move is ",bestMove1)
            self.board[bestMove1[0]][bestMove1[1]] = self.opponent
            self.buttons[bestMove1[0]][bestMove1[1]].config(text=self.opponent)
            eBoard = evaluate(self.board)
	        #if eBoard = 10 then MAX player i.e. X has WON
            if(eBoard == 10):
                self.status_var.set("Winner: {}".format(player))
                for row in self.buttons:
                    for button in row:
                        button.config(state="disabled")

            elif(eBoard == -10):
                self.status_var.set("Winner: {}".format(opponent))
                for row in self.buttons:
                    for button in row:
                        button.config(state="disabled")

            elif(eBoard == 0 and not isMovesLeft(self.board)):
                self.status_var.set("Draw")
                for row in self.buttons:
                    for button in row:
                        button.config(state="disabled")
            else:
                self.status_var.set("Player X turn")


def reset():
    python = sys.executable
    os.execl(python, python, * sys.argv)

root = tk.Tk()
root.resizable(False,False)
game = TicTacToe(root)
root.mainloop()
