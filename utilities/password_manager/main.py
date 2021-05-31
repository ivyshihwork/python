import tkinter
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

dirname = os.path.dirname(__file__)
img_file = os.path.join(dirname, 'logo.png')

window = tkinter.Tk()
window.title('Password Manager')
window.minsize(width=450, height=400)
window.config(padx=20,pady=20)

lock_img = tkinter.PhotoImage(file=img_file)
canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100,image=lock_img)
canvas.grid(column=1, row=0)

# fields - label and more

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = tkinter.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

id_label = tkinter.Label(text="Email/Username:")
id_label.grid(column=0,row=2)

id_input = tkinter.Entry(width=35)
id_input.grid(column=1, row=2, columnspan=2)

password_label = tkinter.Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = tkinter.Button(text='Generate Password')
password_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add',width=36)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()
