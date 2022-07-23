"""
Day 030 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 7/23/2022
Updates to the password manager application. Adding the use of JSON data.
"""

from ast import Try
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    user_data = user_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": user_data,
            "password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data  = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updatating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# --------------------------- SEARCH PASSWORD ------------------------- #
def find_password():
    website_data = website_entry.get()

    if len(website_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the Website field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                search_results  = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="No File Found", message="No Data File Found.")
        else:
            if website_data in search_results:
                email = search_results[website_data]["email"]
                password = search_results[website_data]["password"]
                messagebox.showinfo(title=f"Search Results for {website_data}", message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Search Error", message=f"No deatails for the {website_data} website exists.")
        finally:
                website_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
background_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry boxes
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
user_entry = Entry(width=40)
user_entry.insert(END, string="someEmail@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
