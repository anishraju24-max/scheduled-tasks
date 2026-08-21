##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="anish284111@gmail.com", password="yjfm aigw wntc gwsl")
        connection.sendmail(from_addr="anish284111@gmail.com", to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday!\n\n{contents}")


