from turtle import Turtle, Screen
# from typing import List, Any

# from ball import ball
from paddle import paddle
# from scoreboard import Scoreboard

import time

# Create Screen
screen = Screen()
width = 800
height = 600
screen.setup(width, height)
screen.bgcolor('black')
screen.title("Ivy Shih's Classic Pong Game")
screen.tracer(0)

WIDTH = 20
HEIGHT = 100
RIGHT_X = 350
RIGHT_Y = 0
#ball = ball()
#score = Scoreboard()

rPaddle = paddle()
rPaddle.goto(350,0)

lPaddle = paddle()
lPaddle.goto(-350,0)


screen.listen()
screen.onkey(rPaddle.up, "Up")
screen.onkey(rPaddle.down, "Down")
screen.onkey(lPaddle.up, "a")
screen.onkey(lPaddle.down, "z")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
