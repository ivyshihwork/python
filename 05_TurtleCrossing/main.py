import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import cars
from scoreboard import Scoreboard

# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Ivy Shih's Turtle Crossing Capstone Project")
screen.tracer(0)

#Setting up
player = Player()
score = Scoreboard(-280,250)
MOVE_INCREMENT = 10
counter = 0


def CarGenerator(numberofCars):
    for car in range(0, numberofCars-1):
        cars.append(CarManager())

def detectCollision():
    bang=False
    for car in cars:
        if player.distance(car) <= 30:
            bang=True
    return bang

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

game_is_on = True

CarGenerator(randint(1,7))

while game_is_on:

    if player.ycor() >= 280:
        score.add()
        player.reset()

    for car in cars:
        if car.xcor() < -350:
            cars.remove(car)
        else:
            car.move()

    if counter == 6:
        CarGenerator(randint(1,7))
        counter = 0

    if detectCollision():
        score.game_over()
        game_is_on = False

    time.sleep(0.1)
    screen.update()
    counter += 1

screen.exitonclick()
