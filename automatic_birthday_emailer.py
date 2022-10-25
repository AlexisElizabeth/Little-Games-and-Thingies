import smtplib
import datetime as dt
from random import randint
import pandas

MY_EMAIL = "alexisepaluch@gmail.com"
MY_PASSWORD = "ejmbrijioikahovr"

birthday_dataframe = pandas.read_csv("birthdays.csv")
birthday_list_of_dictionaries = birthday_dataframe.to_dict(orient="records")

now = dt.datetime.now()
month_today = now.month
day_today = now.day

for person in birthday_list_of_dictionaries:
    if person["month"] == month_today and person["day"] == day_today:
        with open(f"letter_templates/letter_{randint(1,3)}.txt", "r") as letter:
            contents = letter.read()
            contents = contents.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: Happy Birthday!\n\n{contents}")

            
            
          ------------------------
birthdays.csv

name,email,year,month,day
Alexis,alexis.paluch@yahoo.com,1978,10,25
Mom,dianne.paluch@gmail.com,1949,9,21
