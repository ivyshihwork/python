import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
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

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

game_is_on = True
cm = CarManager()
cars = cm.cars
cm.createCars(randint(1,7))

while game_is_on:

    if player.ycor() >= 280:
        score.add()
        player.reset()

    for car in cars:
        if car.xcor() < -350:
            cars.remove(car)
        else:
            cm.move(car)

    if counter == 6:
        cm.createCars(randint(1,5))
        counter = 0

    if cm.detectCollision(player):
        score.game_over()
        game_is_on = False

    time.sleep(0.1)
    screen.update()
    counter += 1

screen.exitonclick()
