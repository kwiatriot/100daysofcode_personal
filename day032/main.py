"""
Day 032 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 7/25/2022
Sending a custom birthday message to people on their birthday
"""

import datetime as dt
import pandas
import random
import smtplib

# Setting up our global veribles
MY_EMAIL = "kriotinfo@gmail.com"
MY_PASS = ""  #ADD PASSWORD HERE FOR ACCOUNT USE

# Creating a tuple to store todays date
today = (dt.datetime.now().month, dt.datetime.now().day)
# Reading the data from the CSV into a pandas dataframe
data = pandas.read_csv("/home/kriot/Code/100daysofcode_personal/day032/birthdays.csv")
# Creating the data structure to search from
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
# Finding if a birthday exsists today from the data, choose a random email from the templates
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"/home/kriot/Code/100daysofcode_personal/day032/letter_templates/letter_{random.randint(1,3)}.txt"
    # Open the file and replace with the custom name
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    # Send custom email to the birthday person
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
