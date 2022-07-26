import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "kriotinfo@gmail.com"
MY_PASS = ""  #ADD PASSWORD HERE FOR ACCOUNT USE

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("/home/kriot/Code/100daysofcode_personal/day032/birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"/home/kriot/Code/100daysofcode_personal/day032/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASS)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
