"""
Day 031 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 7/24/2022
Capstone project: Flash Card application
"""

from tkinter import *
from tkinter import font
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("day031/data/french_words.csv")
data_dic = data.to_dict('records')

def choose_word():
    current_word = random.choice(data_dic)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_word["French"])

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="day031/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="day031/images/wrong.png")
right_image = PhotoImage(file="day031/images/right.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=choose_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=choose_word)
right_button.grid(row=1, column=1)

choose_word()

window.mainloop()