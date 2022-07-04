import random
from tkinter import *
import tkinter.font as font
import time
#from PIL import ImageTk, Image

rps = Tk()
rps.geometry("500x500")
rps.title("ROCK PAPER SCISSORS")
user = ""
comp = ""
ans  = ""
bg_image = PhotoImage(file = "stop_img.png") 
rps.config(bg=bg_image)
myFont = font.Font(size=30)
intro = Label(rps, text = "Choose One")
#bg =  PhotoImage(file = "rps.jpg")
def mojifycomp(object):

    if object == "scissors":
        return "Computer chose: ✂"
    if object == "paper":
        return "Computer chose: 🧾"
    if object == "rock":
        return "Computer chose: 🗿"

    else:
        return object

def compChose():
    global comp
    comp_play = random.randint(1,3)
    if comp_play == 1:
        comp = "rock"

    if comp_play == 2:
        comp = "paper"

    if comp_play == 3:
        comp = "scissors"
    Label(rps,text = mojifycomp(comp), font = "poppins").pack(pady=10)


def setRock():
    global user
    user = "rock"
    compChose()
    decide()
    Label(rps,text = mojify(user), font = "poppins").pack(pady=10)
    Label(rps,text = ans, font = "poppins").pack(pady=10)['font']=myFont
   

def setPaper():
    global user
    user = "paper"
    compChose()
    decide()
    Label(rps,text = mojify(user), font = "poppins").pack(pady=10)
    Label(rps,text = ans, font = "poppins").pack(pady=10)['font']=myFont
    

def setScissors():
    global user
    user = "scissors"
    compChose()
    decide()
    Label(rps,text = mojify(user), font = "poppins").pack(pady=10)
    Label(rps,text = ans, font = "poppins").pack(pady=10)['font']=myFont
   

def mojify(object):

    if object == "scissors":
        return "You chose: ✂"
    if object == "paper":
        return "You chose: 🧾"
    if object == "rock":
        return "You chose: 🗿"

    else:
        return object

def decide():
    global ans
    if comp == "rock":
        if user == "paper":
            ans = "PAPER COVERS ROCK, YOU WIN"

        if user == "rock":
            ans = "ITS A TIE"

        if user == "scissors":
            ans = "ROCK BREAKS SCISSORS, COMPUTER WINS"

    elif comp == "scissors":
        if user == "paper":
            ans = "SCISSORS CUTS PAPER, COMPUTER WINS"

        if user == "rock":
            ans = "ROCK BREAKS SCISSORS, YOU WIN"

        if user == "scissors":
            ans = "IT'S A TIE"

    elif comp =="paper":
        if user == "paper":
            ans = "IT'S A TIE"

        if user == "rock":
            ans = "PAPER COVERS ROCK, COMPUTER WINS"

        if user == "scissors":
            ans = "SCISSORS CUTS PAPER, YOU WIN"
    

Label(rps,text = "ROCK PAPER SCISSORS GAME", font = "poppins").pack(pady=10)

rock = Button(rps,text='🗿',command=setRock,bg = "brown")
#rock.invoke()
rock.pack(pady=7)
rock['font']=myFont

paper = Button(rps,text='🧾',command=setPaper,bg="#f5f5f0")
paper.pack(pady=7)
paper['font']=myFont

scissors = Button(rps,text='✂',command=setScissors, bg = "#B0C4DE",relief = "sunken")
scissors.pack(pady=7)
scissors['font']=myFont


Label(rps,text = mojify(user), font = "poppins").pack(pady=10)

print("user is", user)
print("comp is ",comp)
rps.mainloop()

