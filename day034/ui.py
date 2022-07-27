from cgitb import text
from tkinter import *
from turtle import st
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.quiz_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text="Place holder", 
            font=("Ariel", 18, "italic"), 
            fill=THEME_COLOR,
            )

        true_img = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day034/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.select_true)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day034/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.select_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You have reached the end!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def select_true(self):
        self.ui_response(self.quiz.check_answer("True"))

    def select_false(self):
        self.ui_response(self.quiz.check_answer("False"))

    def ui_response(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
