# Tictactoe - Adapted from https://github.com/Miraj50/Awesome-Tkinter-Apps/blob/master/Tic%20Tac%20Toe/tictactoe.py
import tkinter as tk
from tkinter import *


class GameOverException (BaseException):
    pass


class TTT (tk.Tk):
    def __init__(self):
        super ().__init__ ()
        self.title ("TicTacToe")
        self.gameButtons = []
        self.turn = 'X'
        self.count = 0
        self.resizable (True, True)
        self.createGameUI ()
        self.minsize (550, 200)

    def getBoard(self):
        return [[self.gameButtons[i][j]['text'] for j in range (3)] for i in range (3)]

    def createGameUI(self):
        self.leftFrame = Frame (self)
        self.leftFrame.grid (row=0, column=0)
        # create the board
        for i in range (0, 3):
            row = []
            for j in range (0, 3):
                button = tk.Button (self.leftFrame, width=8, height=5,
                                    font="Verdana 12 bold", bg="snow2",
                                    command=lambda x=i, y=j: self.place_on (x, y))
                row.append (button)
                row[j].grid (row=i, column=j)
            self.gameButtons.append (row)

    def place_on(self, x, y):
        self.count += 1
        player = self.turn
        self.gameButtons[x][y].config (text=player, state="disabled")
        win = self.checkWinner ()
        if win:
            self.displayResult (win)
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        self.title ("Turn " + self.turn)

    def checkWinner(self):  # Can be improved
        char = self.turn
        # horizontal
        if (((self.gameButtons[0][0]["text"] == char) and (self.gameButtons[0][1]["text"] == char) and (
                self.gameButtons[0][2]["text"] == char)) or
                ((self.gameButtons[1][0]["text"] == char) and (self.gameButtons[1][1]["text"] == char) and (
                        self.gameButtons[1][2]["text"] == char)) or
                ((self.gameButtons[2][0]["text"] == char) and (self.gameButtons[2][1]["text"] == char) and (
                        self.gameButtons[2][2]["text"] == char)) or
                # vertical
                ((self.gameButtons[0][0]["text"] == char) and (self.gameButtons[1][0]["text"] == char) and (
                        self.gameButtons[2][0]["text"] == char)) or
                ((self.gameButtons[0][1]["text"] == char) and (self.gameButtons[1][1]["text"] == char) and (
                        self.gameButtons[2][1]["text"] == char)) or
                ((self.gameButtons[0][2]["text"] == char) and (self.gameButtons[1][2]["text"] == char) and (
                        self.gameButtons[2][2]["text"] == char)) or
                # diagonal
                ((self.gameButtons[0][0]["text"] == char) and (self.gameButtons[1][1]["text"] == char) and (
                        self.gameButtons[2][2]["text"] == char)) or
                ((self.gameButtons[0][2]["text"] == char) and (self.gameButtons[1][1]["text"] == char) and (
                        self.gameButtons[2][0]["text"] == char))):
            return (char)
        elif self.count == 9:
            return ("DRAW")
        else:
            return None

    def displayResult(self, char):
        self.rightFrame = Frame (self)
        self.rightFrame.grid (row=0, column=1, sticky="nsew")
        if char == "DRAW":
            topText = tk.Label (self.rightFrame, text=f"Its a DRAW !", font="Verdana 12 bold")
        else:
            topText = tk.Label (self.rightFrame, text=f"{char} is the WINNER !", font="Verdana 12 bold")
        topButton = tk.Button (self.rightFrame, text="New Game", bg='blue', fg='white', activebackground='blue3',
                               activeforeground='white', command=self.Restart)
        topText.grid (row=0, column=0, padx=10, pady=10)
        topButton.grid (row=1, column=0)

    def Restart(self):
        for widget in self.winfo_children ():
            widget.destroy ()
        self.gameButtons = []
        self.turn = "X"
        self.count = 0
        self.createGameUI ()


if __name__ == "__main__":
    TTT ().mainloop ()