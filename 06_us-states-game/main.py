from turtle import Turtle, Screen
import os
import pandas
import csv

dirname = os.path.dirname(__file__)
img_file = os.path.join(dirname, 'blank_states_img.gif')
state_file = os.path.join(dirname, '50_states.csv')

screen = Screen()
screen.title("US States Game")
screen.bgpic(img_file)

TOTAL = 50
right_answer = 0
right_guesses = []

state_coors = pandas.read_csv(state_file)

state_names = [ state.lower() for state in state_coors.state.to_list() ]

def writeState(state,x, y):
    name=Turtle()
    name.hideturtle()
    name.color("black")
    name.penup()
    name.goto(x, y)
    name.write(f"{state}", False, 'center',  ("Courier", 12, "normal"))

def get_mouse_click_coor(x,y):
    print(x,y)

answer = screen.textinput(title="Guess the state", prompt="Enter the name of the state: ").lower()

while len(right_guesses) < 50:

    new_title = f"{right_answer}/{TOTAL} Guessed"


    if answer in state_names:
        right_answer += 1
        new_title = f"{right_answer}/{TOTAL} has been quessed."
        state_info = state_coors[state_coors.state.str.lower() == answer]
        state_name = state_info.state
        state_x = int(state_info.x)
        state_y = int(state_info.y)
        right_guesses.append(state_name)
        writeState(state_name, state_x, state_y)

    answer = screen.textinput(title=new_title, prompt="Enter another state name: ").lower()
