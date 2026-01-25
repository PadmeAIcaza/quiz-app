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
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, width=280, text="Question", fill='black', font=FONT)

        # Label
        self.score_label = Label(self.window, text='Score: 0', font=FONT, bg=BG, fg = 'black')
        self.score_label.grid(row=0, column=1)

        # Buttons
        self.true = PhotoImage(file='../images/T.png')
        self.true_button = Button(self.window, image=self.true, bg=BG, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false = PhotoImage(file='../images/F.png')
        self.false_button = Button(self.window, image=self.false, bg=BG, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            grade = (self.quiz.score/10) * 100
            self.canvas.itemconfig(self.question, text=f'Congrats! You\'ve finished the quiz with a {grade}%')

    def true_pressed(self):
       is_right = self.quiz.check_answer('True')
       self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='#A7D477')
        else:
            self.canvas.config(bg='#B33030')

        self.window.after(1000, self.get_next_question)


