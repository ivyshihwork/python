
import tkinter
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = '✔'
count = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    # clear checkmarks, and restart countdown
    global reps
    reps=0
    window.after_cancel(running_timer)
    label_title.config(text='Timer', fg=GREEN)
    canvas.itemconfig(timer, text="00:00")
    label_runs.config(text=f'{int(reps/2) * checkmark}')


# ---------------------------- TIMER MECHANISM ------------------------------- #
# 25 min work, 5 min break  x3, then 25 min work, 20 min break
# 1, 3, 5, 7 -> 25 min, 2, 4, 6 -> 5 min, 8-> 20 min

def start_countdown():
    global reps
    reps+=1
    if reps <= 8:
        if reps %2 != 0 :   # 1, 3, 5, 7
            label_title.config(text='Work', fg=GREEN)
            countdown(WORK_MIN * 60)
        elif reps % 8 == 0: #8
            label_title.config(text='Break', fg=RED)
            countdown(LONG_BREAK_MIN * 60)
        elif reps %2 == 0:  # 2,4, 6
            label_title.config(text='Break', fg=PINK)
            countdown(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def raise_above_all(win):
    win.attributes('-topmost', 1)
    win.attributes('-topmost', 0)

def countdown(count):
    global reps, window, checkmark
    min = int(count / 60)
    sec = count % 60
    if min < 10:
        min = "0" + str(min)
    if sec == 0 or sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer, text=f"{min}:{sec}")
    if count >0:
        global running_timer
        running_timer = window.after(1000, countdown, count -1)
    if count == 0:
        raise_above_all(window)
        if reps % 2 ==0 :
            label_runs.config(text=f'{int(reps /2 )* checkmark}')
        start_countdown()

# ---------------------------- UI SETUP ------------------------------- #
dirname = os.path.dirname(__file__)
img_file = os.path.join(dirname, 'tomato.png')

window = tkinter.Tk()
window.title("Pomodoro")
window.minsize(width=300, height=300)
window.config(padx=20,pady=20, bg=YELLOW)
running_timer = window.after(1000, countdown, count -1)

# Center the image
tomato_img = tkinter.PhotoImage(file = img_file)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)

# Labels
label_title = tkinter.Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, 'normal'))
label_title.grid(column=1, row=1)

label_runs = tkinter.Label(text='', fg=GREEN, bg=YELLOW)
label_runs.grid(column=1, row=4)

# Buttons

start_button = tkinter.Button(text="Start", command=start_countdown)
start_button.grid(column=0, row=3)

reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.grid(column=2, row=3)

window.mainloop()
