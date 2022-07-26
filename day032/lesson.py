"""
Day 032 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 7/25/2022
Sending email(smtplib) and managing dates (datetime)
"""

# ------------------- LESSON -------------------------------------------------- #

# import smtplib

# my_email = "kriotinfo@gmail.com"
# password = ""  ADD PASSWORD HERE FOR ACCOUNT USE

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection. sendmail(
#         from_addr=my_email, 
#         to_addrs="kriotinfo@yahoo.com", 
#         msg="Subject:Hello\n\nI sent you this email from a small python program that I wrote! Its only 20 lines but its the start of learning how email is sent via code!"
#         )

# import datetime as dt

# now = dt.datetime.now()
# # now has a type of a datetime object, but has methods to pull out the different time formats
# year = now.year
# # year has a type of int

# # Creating a datetime object manually
# date_of_birth = dt.datetime(year=1982, month=2, day=8)
# print(date_of_birth)

# ------------------- LESSON -------------------------------------------------- #

# Send a motivation quote every Monday

import smtplib
import datetime as dt
import random

MY_EMAIL = "kriotinfo@gmail.com"
MY_PASS = ""  #ADD PASSWORD HERE FOR ACCOUNT USE

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 0:
    with open("/home/kriot/Code/100daysofcode_personal/day032/quotes.txt", "r") as file:
        quotes_data = file.readlines()
        quote_otd = quotes_data[random.randint(0, 101)]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection. sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="kriotinfo@yahoo.com", 
            msg=f"Subject:Quote of the day\n\nHere is your quote for the day!\n\n{quote_otd}"
            )