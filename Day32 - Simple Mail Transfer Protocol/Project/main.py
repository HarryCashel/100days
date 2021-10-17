import datetime as dt
import smtplib

EMAIL = "cashel.harry101@gmail.com"
PASSWORD = "wy(L*,Yj+F"

# current datetime info
now = dt.datetime.now()

# get current day of week
day = now.weekday()

# conditional to send email
while True:
    if day == 6:
        with open("quotes.txt", "r") as file:
            import random

            data = file.readlines()
            quote = random.choice(data)

        # connection
        with smtplib.SMTP("smtp.gmail.com") as connection:
            # open connection with tls
            connection.starttls()

            # log into email provider
            connection.login(user=EMAIL, password=PASSWORD)

            # send mail
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject:Motivational Quote\n\n{quote}"
            )
