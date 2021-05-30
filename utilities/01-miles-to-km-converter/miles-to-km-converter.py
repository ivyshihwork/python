import tkinter

window = tkinter.Tk()
window.title('Mileage To KM Converter')
window.minsize(width=450, height=50)
window.config(padx=10, pady=10)

miles = 0
km = 0

# Entry box
def process_input():
    global miles, km
    miles = input_box.get()
    km=float(miles) * 1.60934
    label2.config(text=km)


input_box = tkinter.Entry(width=5)
input_box.insert(0, miles)
input_box.grid(column=1, row=0)

# label
label0 = tkinter.Label(text="mile(s) ")
label0.grid(column=2,row=0)

label1 = tkinter.Label(text="equals to")
label1.grid(column=3,row=0)

label2 = tkinter.Label(text=0)
label2.grid(column=4,row=0)

label3 = tkinter.Label(text='km')
label3.grid(column=5,row=0)

# button
button = tkinter.Button(text="Calculate", command=process_input)
button.grid(column=6,row=0)

window.mainloop()
