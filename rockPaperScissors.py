import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock, Paper Scissors")

playerScore = 0
cpuScore = 0
playerChoice = ""
cpuChoice = ""

choices = {
    0:"rock",
    1:"paper",
    2:"scissors"
}

# This strcuture defines who wins each round
# The top layer is the players choice
# The 2nd layer is the CPUs choice and if that results in a:
# 1=win  0=draw -1=loss
rules = {
    0: {
        0:0,
        1:-1,
        2:1
    },
    1: {
        0:1,
        1:0,
        2:-1
    },
    2: {
        0:-1,
        1:1,
        2:0
    }    
}

def resetGame():
    rockBtn["state"] = "active"
    paperBtn["state"] = "active"
    scissorsBtn["state"] = "active"
    playerScoreLbl.config(text="Player   ")
    CpuScoreLbl.config(text="CPU")
    gameLbl.config(text="")

def disableBtns():
    rockBtn["state"] = "disable"
    paperBtn["state"] = "disable"
    scissorsBtn["state"] = "disable"

def playersMove(int playerChoice):
    cpuChoice = random.randint(0, 2)
    roundResultInt = rules[playerChoice][cpuChoice]
    if roundResultInt == 1:
        roundResult = "Player wins"
