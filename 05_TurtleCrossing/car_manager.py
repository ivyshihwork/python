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
#global cars
#cars=[]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []

    def move(self, car):
        car.clear()
        car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())

    def createCar(self):
        new_car = Turtle("square")
        new_car.color(COLORS[randint(0, len(COLORS)-1)])
        new_car.shapesize(1, CAR_LENGTH/CAR_WIDTH)
        new_car.penup()
        new_y = randint(-300 +CAR_WIDTH/2 +50 , 300- CAR_WIDTH/2-50)
        new_car.goto(250, new_y)
        self.cars.append(new_car)

    def createCars(self, number):
        for num in range(0, number):
            self.createCar()

    def detectCollision(self, target):
        bang=False
        for car in self.cars:
            if target.distance(car) <= 28:
                bang=True
        return bang
