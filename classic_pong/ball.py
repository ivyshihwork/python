from turtle import Turtle
from random import randint

WIDTH = 20
HEIGHT = 20
BODY_COUNT = int(HEIGHT / WIDTH)
PACE = 10

class ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x,y)
        self.xPace = 10
        self.yPace = 10

    def setDirection(self):
        direction=randint(0, 360)
        self.setheading(direction)

    def move(self):
        #self.forward(PACE)
        new_x = self.xcor() + self.xPace
        new_y = self.ycor() + self.yPace
        self.goto(new_x, new_y)

    def bounceY(self):
        #self.setheading(360-self.heading())
        self.yPace *= -1

    def bounceX(self):
        self.xPace *= -1
