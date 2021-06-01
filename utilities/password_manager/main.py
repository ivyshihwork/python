import tkinter
from tkinter import messagebox
import os
import string
import random

dirname = os.path.dirname(__file__)
img_file = os.path.join(dirname, 'logo.png')
data_file = os.path.join(dirname, 'password_info.txt')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pw_gen():

    letters = [ letter for letter in string.ascii_lowercase]
    numbers = [ num for num in string.digits ]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    num_letters = random.randint(8, 10)
    num_symbols = random.randint(2, 4)
    num_numbers = random.randint(2, 4)

    for char in range(num_letters):
        password_list.append(random.choice(letters))
        UPPER = random.randint(0, len(password_list)-1)
        password_list[UPPER]=password_list[UPPER].upper()

    for char in range(num_symbols):
        password_list += random.choice(symbols)

    for char in range(num_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ''.join(password_list)
    password_entry.delete(0,tkinter.END)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Trigger by Add button, separate data fields by |
def save_info():
    website_info = website_entry.get()
    id_info = id_entry.get()
    password_info = password_entry.get()
    new_entry = website_info + ' | ' + id_info + ' | ' + password_info + '\n'

    if website_info or id_info or password_info == None:
        messagebox.showerror(title='Error', message="Do not leave any field empty!")
    else:
        ok_to_save = messagebox.askokcancel(title='Confirmation', message=f"New entry has:\n\n\tWebsite={website_info}\n\tEmail={id_info}\n\tPassword={password_info}\n\nIs it okay to save?\n")
        if ok_to_save == True:
            with open(data_file, 'w+') as df:
                df.write(new_entry)
            website_entry.delete(0,tkinter.END)
            password_entry.delete(0, tkinter.END)
            messagebox.showinfo(title="Success", message="A entry has been added to password_info.txt." )
        else:
            messagebox.showinfo(title="Action Cancelled", message="Data is not saved.\n")

# ---------------------------- UI SETUP ------------------------------- #

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

website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

id_label = tkinter.Label(text="Email/Username:")
id_label.grid(column=0,row=2)

id_entry = tkinter.Entry(width=35)
id_entry.insert(0, "ivyshih@yahoo.com")
id_entry.grid(column=1, row=2, columnspan=2)

password_label = tkinter.Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = tkinter.Button(text='Generate Password', command=pw_gen)
password_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add',width=36, command=save_info)
add_button.grid(column=1, row=4,columnspan=2)


window.mainloop()
