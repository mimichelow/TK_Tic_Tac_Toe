import tkinter.messagebox
from tkinter import *
import random

# ----------------------------------------------Set up UI
window = Tk()
window.minsize(width=350, height=420)
window.config(padx=5, pady=20)
window.title("Tic-Tac-Toe")

EMPTY_SLOT = PhotoImage(file="empty.png")
X_SLOT = PhotoImage(file="X.png")
O_SLOT = PhotoImage(file="O.png")

canvas = Canvas(width=350, height=350)

board_img = PhotoImage(file="board.png")

title = Label(text="Lets play Tic-Tac-Toe")
title.grid(row=1)
canvas.create_image(160, 160, image=board_img)
canvas.grid(row=2)

board = []
boardbutton = []

for x in range(9):
    board.append(0)


# ---------------------------------Sets up functions for each button
def fun1():
    if board[0] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[0].configure(image=X_SLOT)
        board[0] = 1
        AIPlay()


def fun2():
    if board[1] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[1].configure(image=X_SLOT)
        board[1] = 1
        AIPlay()


def fun3():
    if board[2] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[2].configure(image=X_SLOT)
        board[2] = 1
        AIPlay()


def fun4():
    if board[3] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[3].configure(image=X_SLOT)
        board[3] = 1
        AIPlay()


def fun5():
    if board[4] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[4].configure(image=X_SLOT)
        board[4] = 1
        AIPlay()


def fun6():
    if board[5] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[5].configure(image=X_SLOT)
        board[5] = 1
        AIPlay()


def fun7():
    if board[6] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[6].configure(image=X_SLOT)
        board[6] = 1
        AIPlay()


def fun8():
    if board[7] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[7].configure(image=X_SLOT)
        board[7] = 1
        AIPlay()


def fun9():
    if board[8] != 0:
        tkinter.messagebox.showerror(title="Error", message="This spot is already taken.")
    else:
        boardbutton[8].configure(image=X_SLOT)
        board[8] = 1
        AIPlay()


# Checks if player has won
def playerwin():
    for slot in range(3):
        if sum(board[slot * 3:slot + 3]) == 3 or sum(board[slot:9:3]) == 3:
            return True
    if sum(board[0:9:4]) == 3 or sum(board[2:7:2]) == 3:
        return True
    return False


# Checks if a certain move would win
def wouldwin(pos):
    if sum(board[pos % 3:9:3]) == -2 or sum(board[int(pos / 3)*3:int(pos / 3)*3 + 3]) == -2:
        return True
    elif pos in [0, 4, 8] and sum([slot for slot in board[0:8:4]]) == -2:
        return True
    elif pos in [2, 4, 6] and sum([slot for slot in board[2:7:2]]) == -2:
        return True
    else:
        return False


# Checks if a certain move would lose
def wouldlose(pos):
    if sum(board[pos % 3:9:3]) == 2 or sum(board[int(pos / 3)*3:int(pos / 3)*3 + 3]) == 2:
        return True
    elif pos in [0, 4, 8] and sum([slot for slot in board[0:8:4]]) == 2:
        return True
    elif pos in [2, 4, 6] and sum([slot for slot in board[2:7:2]]) == 2:
        return True
    else:
        return False


# Returns the game to a default state
def gamerestart():
    for slot in range(9):
        board[slot] = 0
    for button in boardbutton:
        button.configure(image=EMPTY_SLOT)


# Removes game functionality
def gameblock():
    for button in boardbutton:
        button.configure(command="None")


# Checks if player wins, or moves for the CPU, first to win, then to block a win, then randomly
def AIPlay():
    if playerwin():
        print("playerwon")
        if tkinter.messagebox.askyesno(title="Game over", message="You win! Good Job! Do you wish to play again?"):
            gamerestart()
        else:
            gameblock()
    else:
        emptyspaces = [y for y in list(range(9)) if board[y] == 0]
        random.shuffle(emptyspaces)
        for slot in emptyspaces:
            if wouldwin(slot):
                board[slot] = -1
                boardbutton[slot].configure(image=O_SLOT)
                if tkinter.messagebox.askyesno(title="Game over", message="I Win! You Lose! Do you wish to play again?"):
                    gamerestart()
                else:
                    gameblock()
                return True
        if len(emptyspaces) == 0:
            if tkinter.messagebox.askyesno(title="Game over", message="It´s a tie. Do you wish to play again?"):
                gamerestart()
            else:
                gameblock()
            return True
        for slot in emptyspaces:
            if wouldlose(slot):
                board[slot] = -1
                boardbutton[slot].configure(image=O_SLOT)
                return True
        emptyspaces = random.choice(emptyspaces)
        board[emptyspaces] = -1
        boardbutton[emptyspaces].configure(image=O_SLOT)


function = [fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8, fun9]
temp = 0

for xtemp in (5, 115, 225):
    for ytemp in (5, 115, 225):
        boardbutton.append(
            Button(canvas, image=EMPTY_SLOT, command=function[temp], highlightthickness=0, borderwidth=0))
        boardbutton[temp].place(x=ytemp, y=xtemp)
        temp += 1

quitbutton = Button(text="Exit", command=window.destroy)

quitbutton.grid(row=3)
window.mainloop()
