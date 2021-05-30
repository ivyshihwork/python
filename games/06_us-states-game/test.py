import os
import pandas
import csv

dirname = os.path.dirname(__file__)
state_file = os.path.join(dirname, '50_states.csv')

state_coors = pandas.read_csv(state_file)
state='ohio'

state_info = state_coors[state_coors.state.str.lower() == state]
# state_name = state_info.values[0,0].lower()
# state_x = state_info.values[0,1]
# state_y = state_info.values[0,2]

state_name = state_info.state.values[0]
state_x = int(state_info.x)
state_y = int(state_info.y)

print(state_name)
print(state_x)
print(state_y)

# def rightState(guess_state):
#     if state_coors[state_coors.state.str.lower() == guess_state].state.values[0].lower() == guess_state:
#         global right_answer
#         right_answer += 1
#         return True
#     else:
#         return False
#
# right_answer = 0
#
# print(rightState(state))
#
#
# state_names = [ state.lower() for state in state_coors.state.to_list()]
# print(state_names)
