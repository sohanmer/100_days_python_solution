import smtplib
import datetime as dt


quote_counter = 0
my_email = "test@gmail.com"
password="password1234"


with open("quotes.txt") as quotes:
    quotes = quotes.readlines()

weekday = dt.datetime.now().weekday()
if weekday == 0:
    quote = quotes[quote_counter]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="test@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
    quote_counter += 1
