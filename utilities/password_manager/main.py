import tkinter
from tkinter import messagebox
import os
import string
import random
import pyperclip
import json

dirname = os.path.dirname(__file__)
img_file = os.path.join(dirname, 'logo.png')
data_file = os.path.join(dirname, 'password_info.json')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pw_gen():

    password_list = []

    password_list += [random.choice(string.ascii_letters) for _ in range(random.randint(8, 10)) ]
    password_list += [ random.choice(string.punctuation) for _ in range(random.randint(2, 4)) ]
    password_list += [ random.choice(string.digits) for _ in range(random.randint(2, 4)) ]

    random.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0,tkinter.END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Trigger by Add button, separate data fields by |
def save_info():
    website_info = website_entry.get()
    id_info = id_entry.get()
    password_info = password_entry.get()
    #new_entry = website_info + ' | ' + id_info + ' | ' + password_info + '\n'
    new_entry = {
        website_info.lower():{
            'id': id_info,
            'Password': password_info,
        }
    }

    if len(website_info) == 0 or len(id_info) == 0 or len(password_info) == 0:
        messagebox.showerror(title='Error', message="Do not leave any field empty!")
    else:
        # ok_to_save = messagebox.askokcancel(title='Confirmation', message=f"New entry has:\n\n\tWebsite={website_info}\n\tEmail={id_info}\n\tPassword={password_info}\n\nIs it okay to save?\n")
        # if ok_to_save == True:
        #     with open(data_file, 'w+') as df:
        #         df.write(new_entry)
        #     website_entry.delete(0,tkinter.END)
        #     password_entry.delete(0, tkinter.END)
        #     messagebox.showinfo(title="Success", message="A entry has been added to password_info.txt." )
        # else:
        #     messagebox.showinfo(title="Action Cancelled", message="Data is not saved.\n")
        try:
            df = open (data_file, 'r')
            data = json.load(df)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_entry
        else:
            data.update(new_entry)
            df.close()
        finally:
            with open(data_file, 'w') as df2:
                json.dump(data, df2, indent=4)

        messagebox.showinfo(title="Success", message="A entry has been added to password_info.txt." )
        website_entry.delete(0,tkinter.END)
        id_entry.delete(0,tkinter.END)
        password_entry.delete(0, tkinter.END)

# ---------------------------- Search --------------------------------- #

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
# website_entry = tkinter.Entry(width=21)
# website_entry.grid(column=1, row=1)
website_entry.focus()

# search_button = tkinter.Button(text='Search', width=14)
# search_button.grid(column=2, row=1)

id_label = tkinter.Label(text="Email/Username:")
id_label.grid(column=0,row=2)

id_entry = tkinter.Entry(width=35)
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
