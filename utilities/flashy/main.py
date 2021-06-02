'''
Flashy is a flash card learning app.  
'''

import tkinter
import os

#------------------------ SET UP ---------------------------

BACKGROUND_COLOR = "#B1DDC6"

dirname = os.path.dirname(__file__)
card_front_img = os.path.join(dirname, 'images/card_front.png')
card_back_img = os.path.join(dirname, 'images/card_back.png')
right_img = os.path.join(dirname, 'images/right.png')
wrong_img = os.path.join(dirname, 'images/wrong.png')
data_file = os.path.join(dirname, 'data/french_words.csv')


#------------------------ UI Setup ---------------------------

window = tkinter.Tk()
window.title('Flashy')
window.config(padx=20,pady=20, bg=BACKGROUND_COLOR)

front_img = tkinter.PhotoImage(file=card_front_img)
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

lang = canvas.create_text(400, 150, text="French", fill='black', font=('Ariel', 40, 'italic'))
lang_word = canvas.create_text(400, 263, text='trouve', fill='Black', font=('Ariel', 60, 'bold'))

w_img = tkinter.PhotoImage(file=wrong_img)
wrong_button = tkinter.Button(image=w_img)
wrong_button.grid(column=0, row=1)

r_img = tkinter.PhotoImage(file=right_img)
right_button = tkinter.Button(image=r_img)
right_button.grid(column=1, row=1)



window.mainloop()
