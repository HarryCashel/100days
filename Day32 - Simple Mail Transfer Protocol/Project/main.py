import smtplib
import datetime
import pandas
import random

# CONSTANTS
MY_EMAIL = "cashel.harry101@gmail.com"
MY_PASSWORD = "wy(L*,Yj+F"

# set current day
day = datetime.datetime.today()
today_date = day.day
today_month = day.month

# import csv file
birthday_data = pandas.read_csv("birthdays.csv")

names = birthday_data["name"].tolist()

# check if any birthdays today
for name in names:

    check = (birthday_data[birthday_data.name == name])
    email = list(check.email)[0]
    # print(int(check.month))
    if int(check.month) == today_month and int(check.day) == today_date:
        person = name


# if True create personalised letter from a random letter
letter_choice = random.randint(1, 3)
with open(f"letter_{letter_choice}.txt") as letter:
    content = letter.read()

# save email contents to file (Not needed)
file_with_name = content.replace("[NAME]", person)
with open(f"letter_to_{person}", mode="w") as file:
    file.write(file_with_name)


# email to person
if person:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday\n\n{file_with_name}"
        )
