
import smtplib

# Our email address
my_email = "cashel.harry101@gmail.com"
password = "wy(L*,Yj+F"


# Our connection
# Using the keyword with will automatically close the connection after the code in the indent runs
with smtplib.SMTP("smtp.gmail.com") as connection:

    # Open connection with tls
    connection.starttls()

    # Log in to email provider
    connection.login(user=my_email, password=password)

    # Send mail
    connection.sendmail(from_addr=my_email,
                        to_addrs="cashel.harry101@yahoo.com",
                        msg="Subject: Wassup\n\nThis is the body of my email")

# Close connection
# connection.close()


# Return email

yahoo_email = "cashel.harry101@yahoo.com"
yahoo_password = "lzikmvibgcmgziam"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=yahoo_email,
                     password=yahoo_password,)
    connection.sendmail(from_addr=yahoo_email,
                        to_addrs=my_email,
                        msg="Subject: Thanks\n\nThanks for your email.")
