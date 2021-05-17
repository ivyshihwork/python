import time
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

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")
screen.onkeypress(player.left, "Left")
screen.onkeypress(player.right, "Right")

game_is_on = True

while game_is_on:
    if player.ycor() >= 280:
        score.add()
        player.reset()
    time.sleep(0.1)
    screen.update()
