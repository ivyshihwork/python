from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# car size is 20px high by 40px
CAR_WIDTH = 20
CAR_LENGTH = 2 * CAR_WIDTH

# Screen size is 600* 600 - -300 to 300 ,
# No cars should be generated in the top and bottom 50px of the screen
cars = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.shape("square")
        self.shapesize(1, CAR_LENGTH/CAR_WIDTH)
        #self.setheading(270)
        self.penup()
        self.goto(250, randint(-300 +CAR_WIDTH/2 +50 , 300- CAR_WIDTH/2-50))
        self.move()

    def move(self):
        self.clear()
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())
