from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep


SCREEN_HEIGHT=600
SCREEN_WIDTH=800

screen = Screen()
screen.bgcolor('black')
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Ivy Shih's Classic Pong Game")
screen.tracer(0)

# Display objects on the screen
WIDTH = 20
HEIGHT = 100
x_pos = 350
y_pos = 0

rPaddle = Paddle(x_pos, y_pos)
lPaddle = Paddle(-x_pos, y_pos)
ball = Ball(0, 0)

score = Scoreboard(-50, 230)
ball.random_direction()

screen.listen()
screen.onkeypress(rPaddle.up, "Up")
screen.onkeypress(rPaddle.down, "Down")
screen.onkeypress(lPaddle.up, "w")
screen.onkeypress(lPaddle.down, "s")

game_is_on = True

while game_is_on:
    # Let the ball to automatically bounce off the top/bottom plus the ball size
    if ball.ycor() >=  SCREEN_HEIGHT / 2 - WIDTH or ball.ycor() <= -SCREEN_HEIGHT / 2 + WIDTH:
        ball.bounceY()

    # Detect collision with paddles and bounce accordingly
    if  ball.distance(rPaddle) < HEIGHT/2 + WIDTH / 2 and ball.xcor() > 320 or ball.distance(lPaddle) < HEIGHT/2 + WIDTH / 2 and ball.xcor() < -320:
        ball.bounceX()
        if ball.speed > 0:
            ball.speed -= 0.01

    # # if the ball is missed, reset the position and bounce the ball to the other player
    xPos = ball.xcor()
    if xPos > 340:
        ball.reset()
        score.addLeft()

    if ball.xcor() < -340:
        ball.reset()
        score.addRight()

    # If anyone's score is 5, game is OVER
    if score.lscore == 5 or score.rscore == 5:
        score.game_over()
        game_is_on = False

    screen.update()
    sleep(ball.speed)
    ball.move()


screen.exitonclick()
