from turtle import Turtle
from random import randint

WIDTH = 20
HEIGHT = 20
BODY_COUNT = int(HEIGHT / WIDTH)
PACE = 10

class ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(x,y)

    def setDirection(self):
        self.setheading(randint(0, 360))

    def move(self):
        self.forward(PACE)

    def bounce(self):
        pass;
