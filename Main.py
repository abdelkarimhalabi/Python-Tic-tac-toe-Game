from tkinter import *
from functools import partial


class board:
    def __init__(self):
        self.Board : list = [["1","2","3"],["4","5","6"],["7","8","9"]]

    def reset(self):
        self.Board = [["1","2","3"],["4","5","6"],["7","8","9"]]


class blok:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.b = ""


class player:
    def __init__(self):
        self.name = ""
        self.value = 0
        self.CharValue = 'X'
        self.isHisRound = True
        self.winner = False


window = Tk()
window.title("TIC TAC TOE Game By Abdelkarim El Halabi")
window.geometry("875x792")

myBoard = board()

def changeText(i,j):
    if p1.isHisRound:
        for b in buttons:
            if b.i == i and b.j == j:
                 Button(window, text="X",height = 8,width = 20,state = DISABLED,font=("Courier",16)).grid(column = j,row = i)
                 myBoard.Board[i][j] = "X"
                 print(myBoard.Board)
                 break
        p1.isHisRound = False
        p2.isHisRound = True
        if win():
            p1.winner = True
            print("P1 win")
            disableButtons()

    elif p2.isHisRound:
         for b in buttons:
            if b.i == i and b.j == j:
                 Button(window, text="O",height = 8,width = 20,state = DISABLED,font=("Courier",16)).grid(column = j,row = i)
                 myBoard.Board[i][j] = "O"
                 print(myBoard.Board)
                 break
         p2.isHisRound = False
         p1.isHisRound = True
         if win():
            p2.winner = True
            print("P2 win")
            disableButtons()

def disableButtons():
    for i  in range(0,3):
        for j in range(0,3):
            if myBoard.Board[i][j] != "X" and myBoard.Board[i][j] != "O":
                Button(window, text="",height = 8,width = 20,state = DISABLED,font=("Courier",16)).grid(column = j,row = i)

buttons = []

p1 = player()
p1.value = 1
p1.name = "Player 1"

p2 = player()
p2.name = "Player 2"
p2.value = 2
p2.CharValue = "O"
p2.isHisRound = False

def win():
    return(
        myBoard.Board[0][0] == myBoard.Board[0][1] and myBoard.Board[0][0] == myBoard.Board[0][2] or
        myBoard.Board[1][0] == myBoard.Board[1][1] and myBoard.Board[1][0] == myBoard.Board[1][2] or
        myBoard.Board[2][0] == myBoard.Board[2][1] and myBoard.Board[2][0] == myBoard.Board[2][2] or

        myBoard.Board[0][0] == myBoard.Board[1][0] and myBoard.Board[0][0] == myBoard.Board[2][0] or
        myBoard.Board[0][1] == myBoard.Board[1][1] and myBoard.Board[0][1] == myBoard.Board[2][1] or
        myBoard.Board[0][2] == myBoard.Board[1][2] and myBoard.Board[0][2] == myBoard.Board[2][2] or

        myBoard.Board[0][0] == myBoard.Board[1][1] and myBoard.Board[1][1] == myBoard.Board[2][2] or
        myBoard.Board[0][2] == myBoard.Board[1][1] and myBoard.Board[1][1] == myBoard.Board[2][0]
    )


def drawBoard():
    for i in range(0,3):
        for j in  range(0,3):
            bl = blok()
            bl.i = i
            bl.j = j
            bl.b = Button(window, text="",height = 8,width = 20,command=partial(changeText,bl.i,bl.j),font=("Courier",16)).grid(column = j,row = i)
            #b = Button(window, text="",height = 8,width = 20,command=partial(changeText,bl.i,bl.j),font=("Courier",16)).grid(column = j,row = i)
            buttons.append(bl)

def resetGame():
    buttons.clear()
    p1.isHisRound = True
    p1.winner = False
    p2.isHisRound = False
    p2.winner = False
    window.update() 
    myBoard.reset()
    drawBoard()

Button(window, text="Restart Game",height = 8,width = 20,command=resetGame).grid(column = 2,row = 14)
drawBoard()
window.resizable(False, False)
window.mainloop()