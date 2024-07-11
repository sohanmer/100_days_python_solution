import os
import pandas
import random
import smtplib
import datetime as dt


birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.to_dict(orient="records")
birthday_templates = os.listdir("letter_templates")
my_email = "test@gmail.com"
password="password1234"

date = dt.datetime.now().day
month = dt.datetime.now().month

for birthday in birthdays:
    if birthday['month'] == month and birthday['day'] == date:
        template = random.choice(birthday_templates)
        with open(f"letter_templates/{template}") as letter:
            letter = letter.read()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="test@gmail.com",
                msg=f"Subject:Happy birthday!!\n\n{letter.replace('[NAME]', birthday['name'])}"
            )
