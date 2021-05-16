from turtle import Turtle, Screen
from ball import ball
from paddle import paddle
# from scoreboard import Scoreboard

from time import sleep

# Create Screen
screen = Screen()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("Ivy Shih's Classic Pong Game")
screen.tracer(0)

WIDTH = 20
HEIGHT = 100
RIGHT_X = 350
RIGHT_Y = 0

#score = Scoreboard()

ball = ball(0, 0)
rPaddle = paddle(350, 0)
lPaddle = paddle(-350, 0)

screen.listen()
screen.onkey(rPaddle.up, "Up")
screen.onkey(rPaddle.down, "Down")
screen.onkey(lPaddle.up, "a")
screen.onkey(lPaddle.down, "z")

#ball.setDirection()
ball.setheading(120)
distance = (int)(HEIGHT / 2 + WIDTH / 2)

game_is_on = True
paddle_bounce = 0
movecount = 0

while game_is_on:
    sleep(0.1)
    # Let the ball to automatically bounce off the top/bottom plus the ball size
    if ball.ycor() >= SCREEN_HEIGHT / 2 - WIDTH or ball.ycor() <= -SCREEN_HEIGHT / 2 + WIDTH:
        ball.bounceY()

    # Detect collision with paddles
    if  ball.distance(rPaddle) < HEIGHT/2 and ball.xcor() > 330 or ball.distance(lPaddle) < HEIGHT/2 and ball.xcor() <= -330:
        ball.bounceX()

    screen.update()
    ball.move()


screen.exitonclick()
