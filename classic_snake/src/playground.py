from turtle import Turtle, Screen
import time
# Moving snake
pace = 20


def forward():
    for turtle in turtles:
        if turtles.index(turtle) == 0:
            oldX = turtle[1]
            oldY = turtle[2]
            turtle[1] += pace
            turtle[0].goto(turtle[1], turtle[2])
        else:
            turtle[0].goto(oldX, oldY)
            tmpX = turtle[1]
            tmpY = turtle[2]
            turtle[1] = oldX
            turtle[2] = oldY
            oldX = tmpX
            oldY = tmpY


def backward():
    for turtle in turtles[::-1]:
        if turtles.index(turtle) == len(turtles)-1:
            oldX = turtle[1]
            oldY = turtle[2]
            turtle[1] -= pace
            turtle[0].goto(turtle[1], turtle[2])
        else:
            turtle[0].goto(oldX, oldY)
            tmpX = turtle[1]
            tmpY = turtle[2]
            turtle[1] = oldX
            turtle[2] = oldY
            oldX = tmpX
            oldY = tmpY

def up():
    #screen.update()
    for turtle in turtles:
        if turtles.index(turtle) == 0:
            oldX = turtle[1]
            oldY = turtle[2]
            turtle[0].left(90)
            turtle[2] += pace
            turtle[0].goto(turtle[1], turtle[2])
        else:
            turtle[0].goto(oldX, oldY)
            tmpX = turtle[1]
            tmpY = turtle[2]
            turtle[1] = oldX
            turtle[2] = oldY
            oldX = tmpX
            oldY = tmpY


def down():
    for turtle in turtles[::-1]:
        if turtles.index(turtle) == len(turtles) - 1:
            oldX = turtle[1]
            oldY = turtle[2]
            turtle[0].left(90)
            turtle[2] -= pace
            turtle[0].goto(turtle[1], turtle[2])
        else:
            turtle[0].goto(oldX, oldY)
            tmpX = turtle[1]
            tmpY = turtle[2]
            turtle[1] = oldX
            turtle[2] = oldY
            oldX = tmpX
            oldY = tmpY


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
#screen.tracer(0)

tim = Turtle()
tim.color('white')
tim.shape('square')
tim.resizemode('user')
ogLength = 3
curX = curY = 0
nextX = 20
turtles = []

for length in range(0, ogLength):
    newTurtle = Turtle()
    newTurtle.color('white')
    newTurtle.shape('square')
    newTurtle.penup()
    newTurtle.goto(curX, curY)
    turtles.append([newTurtle, curX, curY])
    curX -= nextX

screen.onkey(forward, 'd')
screen.onkey(backward, 'a')
screen.onkey(up, 'w')
screen.onkey(down, 's')
# #screen.onkey(clear, 'c')
screen.listen()


# def clear():
#     timmy.penup()
#     timmy.home()
#     timmy.clear()
#     timmy.pendown()

screen.exitonclick()

