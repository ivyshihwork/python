from turtle import Turtle, Screen
from random import randint

PACE = 10

class Ball(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x,y)
        self.xPace = PACE
        self.yPace = PACE
        self.speed = 0.1

    def random_direction(self):
        self.seth(randint(0, 360 -1))

    def move(self):
        new_x = self.xcor() + self.xPace
        new_y = self.ycor() + self.yPace
        self.goto(new_x, new_y)

    def bounceY(self):
        self.yPace *= -1

    def bounceX(self):
        self.xPace *= -1

    def reset(self):
        self.goto(0,0)
        self.bounceX()
        self.speed = 0.1
