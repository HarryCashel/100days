from datetime import datetime
import pandas
import random
import smtplib

# CONSTANTS
MY_EMAIL = "cashel.harry101@gmail.com"
MY_PASSWORD = "wy(L*,Yj+F"

# get today's datetime object, store month + day in tuple
today = datetime.now()
day_month = (today.month, today.day)

# import csv data and create dictionary

data = pandas.read_csv("birthdays.csv")
# print(data)
birthday_dictionary = {(key["month"], key["day"]): key for (index, key) in data.iterrows()}

if day_month in birthday_dictionary:
    birthday_person = birthday_dictionary[day_month]
    birthday_name = birthday_person["name"]
    birthday_email = birthday_person["email"]
    print(type(birthday_name))
    file_path = f"letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday\n\n{content}"
        )
