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

def refresh():
    global playerScore
    global cpuScore
    playerScoreLbl.config(text="Player Score:"+str(playerScore))
    cpuScoreLbl.config(text="CPU Score:"+str(cpuScore))
    # cpuChoiceLbl.config(text="")
    # roundResultLbl.config(text="")

def disableBtns():
    rockBtn["state"] = "disable"
    paperBtn["state"] = "disable"
    scissorBtn["state"] = "disable"

def playersMove(playerChoice):
    cpuChoice = random.randint(0, 2)
    cpuChoiceLbl.config(text="CPU picks "+choices[cpuChoice])
    roundResultInt = rules[playerChoice][cpuChoice]
    if roundResultInt == 1:
        roundResult = "Player wins"
        global playerScore
        playerScore += 1
    elif roundResultInt == -1:
        roundResult = "CPU wins!"
        global cpuScore
        cpuScore += 1
    else:
        roundResult = "Draw"
    roundResultLbl.config(text=roundResult)
    refresh()

# Labels, Frames & Buttons
tk.Label(window,
      text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="blue").pack(pady=20)     

scoreFrame = tk.Frame(window)
scoreFrame.pack()
roundFrame = tk.Frame(window)
roundFrame.pack()

# Score Frame
playerScoreLbl = tk.Label(scoreFrame,
                       text="Player Score:"+str(playerScore),
                       font=10)
cpuScoreLbl = tk.Label(scoreFrame,
                       text="CPU Score:"+str(cpuScore),
                       font=10)

# Round Frame
cpuChoiceLbl = tk.Label(roundFrame,
                        text="",
                        font=10)
playerScoreLbl.pack(side=tk.LEFT)
cpuScoreLbl.pack(side=tk.LEFT)
cpuChoiceLbl.pack(side=tk.LEFT)
roundResultLbl = tk.Label(window,
                       text="",
                       font="normal 20 bold",
                       bg="white",
                       width=15,
                       borderwidth=2,
                       relief="solid")
roundResultLbl.pack(pady=20)
frame = tk.Frame(window)
frame.pack()

rockBtn = tk.Button(frame, text="Rock",
                 font=10, width=7,
                 command=lambda: playersMove(0))
paperBtn = tk.Button(frame, text="Paper",
                 font=10, width=7,
                 command=lambda: playersMove(1))
scissorBtn = tk.Button(frame, text="Scissor",
                 font=10, width=7,
                 command=lambda: playersMove(2))
rockBtn.pack(side=tk.LEFT, padx=10)
paperBtn.pack(side=tk.LEFT, padx=10)
scissorBtn.pack(padx=10)

# MAIN
window.mainloop()