from turtle import Turtle, Screen
from typing import List, Any

from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

STOP = 295
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.segments[0].distance(food) < 20:
        score.add()
        food.move()
        snake.grow()

    # Collision with  wall
    # wall is 300 x 300 - can use 280
    if snake.segments[0].xcor() > STOP or snake.segments[0].xcor() < -STOP or snake.segments[0].ycor() > STOP or snake.segments[0].ycor() <= -STOP:
        game_is_on = False
        #score.game_over()
        score.resetScoreboard()
        snake.reset()

    # Detect collision with body
    if any( dist < 15 for dist in { snake.segments[0].distance(seg) for seg in snake.segments[1:]}):
        game_is_on = False
        #score.game_over()
        score.resetScoreboard()
        snake.reset()

screen.exitonclick()
