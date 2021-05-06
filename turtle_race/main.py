from turtle import Turtle, Screen
from random import randint

screen = Screen()
width=500
height=400
screen.setup(width, height)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
turtle = {}
inc = int(height/(len(colors)+1))
x = int(width / 2 - width + 20)
start_pos = int(height/2 - height +20)

bet = None

while bet not in colors:
    bet = screen.textinput("Make your bet", "Which color of turtle will win?").lower()

# Create Turtles
for color in colors:
    turtle[color]=Turtle(shape='turtle')
    turtle[color].color(color)
    turtle[color].penup()
    start_pos += inc
    turtles.append([color, x, start_pos])

# Position turtles in the starting line
for t in turtles:
    turtle[t[0]].goto(t[1], t[2])

# Turtle race starts - check for first one gets to the end.
furthest = 0
winner = ''
destination = int(width / 2) - 20
while furthest < destination:
    for color in colors:
        tp = [item for item in turtles if item[0] == color]
        tmp = tp[0]
        pace = randint(1,11)
        tmp[1] += pace
        turtle[color].goto(tmp[1], tmp[2])
        if furthest < tmp[1]:
            furthest = tmp[1]
        if tmp[1] >= destination:
            winner = color
            break

if winner != bet:
    print(f"You have lost!  The winner is {winner} turtle!")
else:
    print(f"You have won!  The winner is {winner} turtle")

screen.exitonclick()
