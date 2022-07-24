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
current_word = {}
unknown_dic = {}

try:
    data = pandas.read_csv("/home/kriot/Code/100daysofcode_personal/day031/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("/home/kriot/Code/100daysofcode_personal/day031/data/french_words.csv")
    unknown_dic = original_data.to_dict("records")
else:
    unknown_dic = data.to_dict("records")

def choose_word():
    global current_word, flip_timer, unknown_dic
    window.after_cancel(flip_timer)
    current_word = random.choice(unknown_dic)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card) 
     
def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(title_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=current_word["English"])

def is_known():
    unknown_dic.remove(current_word)
    data = pandas.DataFrame(unknown_dic)
    data.to_csv("/home/kriot/Code/100daysofcode_personal/day031/data/words_to_learn.csv", index=False)
    choose_word()

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day031/images/card_front.png")
card_back_img = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day031/images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day031/images/wrong.png")
right_image = PhotoImage(file="/home/kriot/Code/100daysofcode_personal/day031/images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=choose_word)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

choose_word()

window.mainloop()
