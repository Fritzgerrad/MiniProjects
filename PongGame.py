import turtle
import os 
import winsound
wn = turtle.Screen()
wn.title("Pong by Fritzgerrad")
wn.bgcolor("lime")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#SCORE
score_a = 0
score_b = 0 

# Paddle A
paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("blue")
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("blue")
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("brown")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5 # This means that the ball movees 2 pixels in the x-direction every time
ball.dy = -0.5 # This means that the ball moves 2 pixels in the y - direction every time
# as a result of dx and dy both having a value of 2, the ball moves 2 pixels diagonally.

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER A: 0  PLAYER B: 0",align = "center", font= ("Helvetica",24,"normal"))



#Function
def paddle_a_up():
    y = paddle_a.ycor() #get the y cordinate of the ball
    y += 20  #increase the y by 20
    paddle_a.sety(y) #set the y cordinate to the new y

def paddle_a_down():
    y = paddle_a.ycor() #get the y cordinate of the ball
    y -= 20  #decrease the y by 20
    paddle_a.sety(y) #set the y cordinate to the new y

def paddle_b_up():
    y = paddle_b.ycor() #get the y cordinate of the ball
    y += 20  #increase the y by 20
    paddle_b.sety(y) #set the y cordinate to the new y

def paddle_b_down():
    y = paddle_b.ycor() #get the y cordinate of the ball
    y -= 20  #decrease the y by 20
    paddle_b.sety(y) #set the y cordinate to the new y



#Keyboard Binding

wn.listen() #ask the code to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #tells the computer to call the function paddle_up when the user presses "w" on the keyboard
wn.onkeypress(paddle_a_down, "s") #tells the computer to call the function paddle_up when the user presses "s" on the keyboard
wn.onkeypress(paddle_b_up, "Up") #tells the computer to call the function paddle_up when the user presses "Up" on the keyboard
wn.onkeypress(paddle_b_down, "Down") #tells the computer to call the function paddle_up when the user presses "Down" on the keyboard

#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    #This block tells the ball to bounce back when it gets to the top end of the window

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    #This block tells the ball to bounce back when it gets to the bottom end of the window

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*= -1
        score_a +=1
        pen.clear()
        pen.write("PLAYER A:  {}  PLAYER B:  {}".format(score_a,score_b),align = "center", font= ("Helvetica",24,"normal"))
        winsound.PlaySound("Basketball-crowd-cheering-at-a-game-215.wav", winsound.SND_ASYNC)


    #This block tells the ball to return to the center when it gets to the right end of the window

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1 
        pen.clear()
        pen.write("PLAYER A:  {}  PLAYER B:  {}".format(score_a,score_b),align = "center", font= ("Helvetica",24,"normal"))
        winsound.PlaySound("Basketball-crowd-cheering-at-a-game-215.wav", winsound.SND_ASYNC)
    #This block tells the ball to return to the center when it gets to the left end of the window

    #Getting the ball to bounce of the paddles
   
    if (ball.xcor() > 340  and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("Fast-whoosh-metal-crowbar-2-142.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340  and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("Fast-whoosh-metal-crowbar-2-142.wav", winsound.SND_ASYNC)

    #Adding Scoring System
