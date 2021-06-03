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

    # lang_words = all_data[lang].tolist()
    # xlate_words = all_data[xlate].tolist()


#------------------------ Generate random word --------------------------
def generate_lang_word():
    global all_data,lang, xlate
    random_lang = all_data[lang].tolist()[random.randint(0, len(all_data[xlate].tolist())-1 )]
    
    canvas.itemconfig(lang_word,text=random_lang)


#------------------------ UI Setup ---------------------------

window = tkinter.Tk()
window.title('Flashy')
window.config(padx=20,pady=20, bg=BACKGROUND_COLOR)

front_img = tkinter.PhotoImage(file=card_front_img)
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

lang_text = canvas.create_text(400, 150, text=lang, fill='black', font=('Ariel', 40, 'italic'))

new_rand = all_data[lang].tolist()[random.randint(0, len(all_data[xlate].tolist())-1 )]
lang_word = canvas.create_text(400, 263, text=new_rand, fill='Black', font=('Ariel', 60, 'bold'))

w_img = tkinter.PhotoImage(file=wrong_img)
wrong_button = tkinter.Button(image=w_img, highlightthickness=0, command=generate_lang_word)
wrong_button.grid(column=0, row=1)

r_img = tkinter.PhotoImage(file=right_img)
right_button = tkinter.Button(image=r_img, highlightthickness=0, command=generate_lang_word)
right_button.grid(column=1, row=1)



window.mainloop()
