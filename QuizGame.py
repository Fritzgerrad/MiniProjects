print("WELCOME TO MY QUIZ")

playing = input("Do yo want to play? ")

if playing == "NO":
    quit()

score = 0

def marker(question, ans):
    question = question.lower()
    ans = ans.lower()
    
    if question == ans:
        global score
        score+=1

qOne = input("Who invented Java? ")
marker(qOne, "james gosling")

qtwo = input("Is Java an Object Oriented Program? ")
marker(qtwo, "yes")

qthree = input("What is one foundations of OOP? ")
marker(qthree, "encapsulation")

qfour = input("Who is the greatest football player of all time? ")
marker(qfour, "Ronaldo")

qfive = input("What is the greates Football Team of all time? ")
marker(qfive, "Manchester United")

print("Your score is ", score,"/5")