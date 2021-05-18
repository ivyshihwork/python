from turtle import Turtle
from random import randint


class Food(Turtle):
    # render itself on screen, and when snake touches it, it disappears
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.7,0.7)
        self.color('blue')
        self.speed('fastest')
        self.move()

    def move(self):
        self.goto(randint(-200, 200), randint(-200, 200))
