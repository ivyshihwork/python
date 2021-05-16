from turtle import Turtle

# Paddle basic settings
WIDTH = 20
HEIGHT = 100

BODY_COUNT = int(HEIGHT / WIDTH)

class paddle(Turtle):
    # render paddle right
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=BODY_COUNT, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto(x,y)

    def up(self):
        self.goto(self.xcor(), self.ycor() + WIDTH)

    def down(self):
        self.goto(self.xcor(), self.ycor() - WIDTH)
