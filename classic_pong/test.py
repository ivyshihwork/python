from turtle import Turtle, Screen
from ball import ball
from paddle import paddle

screen = Screen()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("Ivy Shih's Classic Pong Game")
screen.tracer(0)


ball = ball(335, 60)
rPaddle = paddle(350, 0)
print(ball.distance(rPaddle))


screen.listen()

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
