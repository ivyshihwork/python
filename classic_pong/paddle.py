from turtle import Turtle

WIDTH = 20
HEIGHT = 100
x_pos = 350
y_pos = 0

PADDLE_LENGTH = HEIGHT / WIDTH

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(PADDLE_LENGTH, 1)
        self.speed('fastest')
        self.penup()
        self.goto(x, y)

    def up(self):
        if self.ycor() <= 222:
            self.goto(self.xcor(), self.ycor() + WIDTH)

    def down(self):
        if self.ycor() >= -222:
            self.goto(self.xcor(), self.ycor() - WIDTH)
