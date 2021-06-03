'''
Flashy is a flash card learning app.
'''

import tkinter
import os
import pandas
import random

#------------------------ SET UP ---------------------------

BACKGROUND_COLOR = "#B1DDC6"

dirname = os.path.dirname(__file__)
card_front_img = os.path.join(dirname, 'images/card_front.png')
card_back_img = os.path.join(dirname, 'images/card_back.png')
right_img = os.path.join(dirname, 'images/right.png')
wrong_img = os.path.join(dirname, 'images/wrong.png')
data_file = os.path.join(dirname, 'data/french_words.csv')
to_learn_file = os.path.join(dirname, 'data/words_to_learn.csv')

#------------------------ Read Data --------------------------
try:
    with open(data_file, 'r') as df:
        all_data = pandas.read_csv(df)
except (FileNotFoundError):
    messagebox.showinfo(title="Error", message=f"Flash Card word file\n({data_file})\nis not found.")
else:
    xlate_dict = all_data.to_dict()

    lang= list(xlate_dict.keys())[0]
    xlate = list(xlate_dict.keys())[1]

    xlate_dict = all_data.to_dict(orient='records') # [{'French': 'partie', 'English': 'part'},


#------------------------ Generate random word --------------------------
def next_card():
    global all_data,lang, xlate, random_word, flip_timer
    random_word = random.choice(xlate_dict)
    canvas.itemconfig(lang_word,text=random_word[lang])
    # Flip card to front
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_side, image=front_img)
    canvas.itemconfig(lang_text, text=lang, fill='black')
    canvas.itemconfig(lang_word, text=random_word[lang], fill='black')
    flip_timer = window.after(3000, flip_card)

#------------------------ flip card ---------------------------

def flip_card():
    # Flip card to the back
    canvas.itemconfig(card_side, image=back_img)
    canvas.itemconfig(lang_text, text=xlate, fill='white')
    canvas.itemconfig(lang_word, text=random_word[xlate], fill='white')

#------------------------ flip card ---------------------------

def check_button():
    global xlate_dict, to_learn_file
    xlate_dict.remove(random_word)
    df = pandas.DataFrame(xlate_dict)
    df.to_csv(to_learn_file)
    next_card()


#------------------------ UI Setup ----------------------------

window = tkinter.Tk()
window.title('Flashy')
window.config(padx=20,pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

front_img = tkinter.PhotoImage(file=card_front_img)
back_img = tkinter.PhotoImage(file=card_back_img)
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
card_side = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

lang_text = canvas.create_text(400, 150, text=lang, fill='black', font=('Ariel', 40, 'italic'))

random_word = random.choice(xlate_dict)
lang_word = canvas.create_text(400, 263, text=random_word[lang], fill='Black', font=('Ariel', 60, 'bold'))

w_img = tkinter.PhotoImage(file=wrong_img)
wrong_button = tkinter.Button(image=w_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

r_img = tkinter.PhotoImage(file=right_img)
right_button = tkinter.Button(image=r_img, highlightthickness=0, command=check_button)
right_button.grid(column=1, row=1)



window.mainloop()
