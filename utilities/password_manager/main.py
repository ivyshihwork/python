'''
Password Manager

written by Ivy Shih     ivy.shih.work@gmail.com

'''

import tkinter
from tkinter import messagebox
import os
import string
import random
# import pyperclip
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
    #pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Trigger by Add button, separate data fields by |
def save_info():
    website_info = website_entry.get()
    url_info = url_entry.get()
    id_info = id_entry.get()
    password_info = password_entry.get()

    new_entry = {
        website_info.lower():{
            'url': url_info,
            'id': id_info,
            'password': password_info,
        }
    }

    if len(website_info) == 0 or len(url_info) ==0 or len(id_info) == 0 or len(password_info) == 0:
        messagebox.showerror(title='Error', message="Do not leave any field empty!")
    else:
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

        messagebox.showinfo(title="Success", message=f"A entry has been added/updated to:\n{data_file}." )
        website_entry.delete(0,tkinter.END)
        url_entry.delete(0,tkinter.END)
        id_entry.delete(0,tkinter.END)
        password_entry.delete(0, tkinter.END)

# ---------------------------- Search --------------------------------- #

def search():
    website_info = website_entry.get()

    try:
        with open (data_file, 'r') as df:
            data = json.load(df)
    except (FileNotFoundError, NameError,):
        messagebox.showinfo(title="Warning", message="No data file is found.\nPlease add some data first." )
    except (json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Warning", message="No website has been entered on file." )
    else:
        if website_info.lower() in data:
            url_info = data[website_info.lower()]['url']
            id_info = data[website_info.lower()]['id']
            password_info = data[website_info.lower()]['password']
            id_entry.delete(0,tkinter.END)
            url_entry.delete(0,tkinter.END)
            password_entry.delete(0, tkinter.END)
            id_entry.insert(0, id_info)
            url_entry.insert(0, url_info)
            password_entry.insert(0, password_info)
        else: # if 'id_info' not in locals():
            messagebox.showinfo(title="Warning", message=f"No record exists for entered website." )


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

website_label = tkinter.Label(text="Website Name:")
website_label.grid(column=0, row=1)

website_entry = tkinter.Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = tkinter.Button(text='Search', width=14, command=search)
search_button.grid(column=2, row=1)

url_label = tkinter.Label(text="Website URL:")
url_label.grid(column=0, row=2)

url_entry = tkinter.Entry(width=35)
url_entry.grid(column=1,row=2, columnspan=2)

id_label = tkinter.Label(text="Username/Email:")
id_label.grid(column=0,row=3)

id_entry = tkinter.Entry(width=35)
id_entry.grid(column=1, row=3, columnspan=2)

password_label = tkinter.Label(text='Password:')
password_label.grid(column=0, row=4)

password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=4)

password_button = tkinter.Button(text='Generate Password', command=pw_gen)
password_button.grid(column=2, row=4)

add_button = tkinter.Button(text='Add/Update',width=36, command=save_info)
add_button.grid(column=1, row=5,columnspan=2)


window.mainloop()
