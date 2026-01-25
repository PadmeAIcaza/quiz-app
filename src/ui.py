from tkinter import *
from quiz_brain import QuizBrain

BG = "#DDF7E3"
FONT = ('Times New Roman', 20, 'italic')

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzzzler')
        self.window.config(padx=20, pady=20, bg=BG)

        # Text
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question = self.canvas.create_text(150, 125, width=280, text="Question", fill='black', font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Label
        self.score_label = Label(self.window, text='Score: ', font=FONT, bg=BG, fg = 'black')
        self.score_label.grid(row=0, column=1)

        # Buttons
        self.true = PhotoImage(file='../images/T.png')
        self.true_button = Button(self.window, image=self.true, bg=BG)
        self.true_button.grid(row=2, column=0)

        self.false = PhotoImage(file='../images/F.png')
        self.false_button = Button(self.window, image=self.false, bg=BG)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)