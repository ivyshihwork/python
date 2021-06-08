import tkinter
import os
import quiz_brain

THEME_COLOR = "#375362"
dirname = os.path.dirname(__file__)
right = os.path.join(dirname, 'images/true.png')
wrong = os.path.join(dirname, 'images/false.png')

class QuizInterface:
    def __init__(self, qb: quiz_brain.QuizBrain):
        self.quizbrain = qb
        self.window = tkinter.Tk()
        self.window.title('10 Trivia Questions')
        self.window.config(padx=20,pady=20, bg="#375362")

        self.score_txt = tkinter.Label(text=f'Score: {self.quizbrain.score}/{self.quizbrain.question_number+1}', fg='white', bg=THEME_COLOR)
        self.score_txt.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg='white' ,highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="", fill=THEME_COLOR, font=('Arial', 25, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        self.true_img = tkinter.PhotoImage(file=right)
        self.true_button = tkinter.Button(image=self.true_img,highlightthickness=0, command=self.true_clicked)
        self.true_button.grid(column=0, row=3)

        self.false_img = tkinter.PhotoImage(file=wrong)
        self.false_button = tkinter.Button(image=self.false_img, highlightthickness=0, command=self.false_clicked)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quizbrain.still_has_questions():
            q_text = self.quizbrain.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text='You have reached the end of quiz.')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_clicked(self):
        self.feedback(self.quizbrain.check_answer('True'))

    def false_clicked(self):
        self.feedback(self.quizbrain.check_answer('False'))

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
            self.quizbrain.score += 1
        else:
            self.canvas.config(bg='red')
        self.score_txt.config(text=f'Score: {self.quizbrain.score}/{self.quizbrain.question_number}')
        self.window.after(1000, self.get_next_question)
