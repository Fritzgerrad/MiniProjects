import random
def mojify(object):

    if object == "scissors":
        return "✂"
    if object == "paper":
        return "🧾"
    if object == "rock":
        return "🗿"

    else:
        return object
def rps():
    user = ""
    comp = ""

    comp_play = random.randint(1,3)
    if comp_play == 1:
        comp = "rock"

    if comp_play == 2:
        comp = "paper"

    if comp_play == 3:
        comp = "scissors"

    user = input("Play your Hand \n")
    
    
    user = user.lower()
    comp = comp.lower()
    print(" User: ",mojify(user))
    print(" Computer: ",mojify(comp))
    #if user != "rock" or user!="paper" or user!="scissors":
        #print("PLEASE PLAY A CORRECT HAND")
       # rps()

    if comp == "rock":
        if user == "paper":
            print("PAPER COVERS ROCK, USER WINS")

        if user == "rock":
            print("ITS A TIE")

        if user == "scissors":
            print("ROCK BREAKS SCISSORS, COMPUTER WINS")

    elif comp == "scissors":
        if user == "paper":
            print("SCISSORS CUTS PAPER, COMPUTER WINS")

        if user == "rock":
            print("ROCK BREAKS SCISSORS, USER WINS")

        if user == "scissors":
            print("IT'S A TIE")

    elif comp =="paper":
        if user == "paper":
            print("IT'S A TIE")

        if user == "rock":
            print("PAPER COVERS ROCK, COMPUTER WINS")

        if user == "scissors":
            print("SCISSORS CUTS PAPER, USER WINS")

rps()
