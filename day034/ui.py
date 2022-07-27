from time import clock_getres
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
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
            text="Place holder", 
            font=("Ariel", 18, "italic"), 
            fill=THEME_COLOR,
            )

        true_img = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day034/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day034/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()