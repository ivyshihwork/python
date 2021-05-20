from turtle import Turtle, Screen
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'blank_states_img.gif')

screen = Screen()
screen.title("US States Game")
screen.bgpic(filename)
#screen.addshape(filename)

screen.listen()
screen.exitonclick()
