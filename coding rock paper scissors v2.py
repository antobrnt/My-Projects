import tkinter as tk
import random

result_message = ""
userscore = 0
machinescore = 0
choices = ["rock", "paper", "scissors"]
userchoice = ""

window = tk.Tk()
window.title("Rock Paper Scissors")
window.configure(bg="#9589db")
window.geometry("400x300")

title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

message_Label = tk.Label(window, text="Make your choice!", font=("Helvetica", 12), bg="#f0f0f0")
message_Label.pack(pady=10)

button_style = {
    "font": ("Helvetica", 12),
    "width": 12,
    "padx": 5,
    "pady": 5,
    "bg": "#4CAF50",      # greenish
    "fg": "white",
    "activebackground": "#45a049",
    "relief": "raised"
}

def rock_clicked():
    global userchoice, machinechoice, userscore, machinescore, result_message
    userchoice = "rock"
    machinechoice = random.choice(choices)

    if userchoice == machinechoice:
        result_message = f"It's a tie! You both chose {userchoice}."
    elif (userchoice == "rock" and machinechoice == "scissors") or \
         (userchoice == "paper" and machinechoice == "rock") or \
         (userchoice == "scissors" and machinechoice == "paper"):
        result_message = f"You chose {userchoice}. The machine chose {machinechoice}. You win!"
        userscore += 1
    else:
        result_message = f"You chose {userchoice}. The machine chose {machinechoice}. You lose!"
        machinescore += 1

    message_Label.config(text=f"{result_message}\nScore: You {userscore} - Machine {machinescore}")

def paper_clicked():
    global userchoice, machinechoice, userscore, machinescore, result_message
    userchoice = "paper"
    machinechoice = random.choice(choices)

    if userchoice == machinechoice:
        result_message = f"It's a tie! You both chose {userchoice}."
    elif (userchoice == "rock" and machinechoice == "scissors") or \
         (userchoice == "paper" and machinechoice == "rock") or \
         (userchoice == "scissors" and machinechoice == "paper"):
        result_message = f"You chose {userchoice}. The machine chose {machinechoice}. You win!"
        userscore += 1
    else:
        result_message = f"You chose {userchoice}. The machine chose {machinechoice}. You lose!"
        machinescore += 1

    message_Label.config(text=f"{result_message}\nScore: You {userscore} - Machine {machinescore}")

def scissors_clicked():
    global userchoice, machinechoice, userscore, machinescore, result_message
    userchoice = "scissors"
    machinechoice = random.choice(choices)

    if userchoice == machinechoice:
        result_message = f"It's a tie! You both chose {userchoice}."
    elif (userchoice == "rock" and machinechoice == "scissors") or \
         (userchoice == "paper" and machinechoice == "rock") or \
         (userchoice == "scissors" and machinechoice == "paper"):
        result_message = f"You chose {userchoice}. The machine chose {machinechoice}. You win!"
        userscore += 1
    else:
        result_message = f"You chose {userchoice}. The machine chose {machinechoice}. You lose!"
        machinescore += 1

    message_Label.config(text=f"{result_message}\nScore: You {userscore} - Machine {machinescore}")

buttons_frame = tk.Frame(window, bg="#f0f0f0")
buttons_frame.pack(pady=20)

rock_button = tk.Button(buttons_frame, text="Rock", command=rock_clicked, **button_style)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(buttons_frame, text="Paper", command=paper_clicked, **button_style)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=scissors_clicked, **button_style)
scissors_button.grid(row=0, column=2, padx=5)

window.mainloop()
