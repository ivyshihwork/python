from turtle import Turtle, Screen
import os
import pandas
import csv

dirname = os.path.dirname(__file__)
img_file = os.path.join(dirname, 'blank_states_img.gif')
state_file = os.path.join(dirname, '50_states.csv')
states_to_learn = os.path.join(dirname, 'states_to_learn.csv')

screen = Screen()
screen.title("US State Name Guessing Game")
screen.bgpic(img_file)

TOTAL = 50
right_answer = 0
right_guesses = []

state_coors = pandas.read_csv(state_file)

state_names =  state_coors.state.to_list()

def writeState(state,x, y):
    name=Turtle()
    name.color("black")
    name.hideturtle()
    name.penup()
    name.goto(x, y)
    name.write(f"{state}", False, 'center',  ("Courier", 10, "normal"))

while len(right_guesses) < 50:

    new_title = f"{right_answer}/{TOTAL} Guessed"
    answer = screen.textinput(title=new_title, prompt="Enter another state name: ").title()

    if answer in state_names:
        right_answer += 1
        new_title = f"{right_answer}/{TOTAL} has been quessed."
        state_info = state_coors[state_coors.state == answer]
        state_name = state_info.state.values[0]
        state_x = int(state_info.x)
        state_y = int(state_info.y)
        right_guesses.append(state_name)
        writeState(state_name, state_x, state_y)
    elif answer == 'Exit':
        break

# generate a file of missing states upon exit
states_to_learn_list =  list(set(state_names) - set(right_guesses))
states_to_learn_list.sort()
df = pandas.DataFrame(states_to_learn_list, columns=['state'])
df.to_csv(states_to_learn)
