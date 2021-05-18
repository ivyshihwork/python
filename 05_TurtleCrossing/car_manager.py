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
global cars
cars=[]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[randint(0, len(COLORS)-1)])
        self.shape("square")
        self.shapesize(1, CAR_LENGTH/CAR_WIDTH)
        #self.setheading(270)
        self.penup()
        new_y = randint(-300 +CAR_WIDTH/2 +50 , 300- CAR_WIDTH/2-50)
        # too_close = [new_y - car.ycor() <=10 or car.ycor() - new_y <=10 for car in cars]
        # print(f"too_close before: {too_close}")
        # while len(too_close)  == [True]:
        #     too_close = [ abs(new_y - car.ycor())<=CAR_WIDTH+MOVE_INCREMENT or abs(car.ycor() - new_y) <=CAR_WIDTH+MOVE_INCREMENT for car in cars]
        #     new_y = randint(-300 +CAR_WIDTH/2 +50 , 300- CAR_WIDTH/2-50)
        # print(f"too_close after: {too_close}")
        self.goto(250, new_y)
        self.move()

    def move(self):
        self.clear()
        self.goto(self.xcor() - MOVE_INCREMENT, self.ycor())
