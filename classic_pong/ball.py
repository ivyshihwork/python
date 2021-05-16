from turtle import Turtle
from random import randint

WIDTH = 20
HEIGHT = 20
BODY_COUNT = int(HEIGHT / WIDTH)
PACE = 20

class ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x,y)

    def setDirection(self):
        direction=randint(0, 360)
        self.setheading(direction)
        print(direction)

    def move(self):
        self.forward(PACE)

    def bounce(self):
        self.setheading(360 - self.heading())
