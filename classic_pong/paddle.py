from turtle import Turtle

# Paddle basic settings - move up and down 20 pixels
WIDTH = 20
HEIGHT = 100

BODY_COUNT = int(HEIGHT / WIDTH)

class paddle(Turtle):
    # render paddle right
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(BODY_COUNT, 1)
        self.penup()
        self.goto(x,y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + WIDTH)

    def down(self):
        self.goto(self.xcor(), self.ycor() - WIDTH)
