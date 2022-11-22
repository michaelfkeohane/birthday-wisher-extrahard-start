##################### Extra Hard Starting Project ######################
import pandas as df
import random
import datetime as dt
import smtplib

my_email = "keoclantest@gmail.com"
my_password = "sqkxwtcdixxgmroq"
now = dt.datetime.now()
data = df.read_csv("birthdays.csv")
letters = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

for ind in data.index:`
    if (now.month == data['month'][ind]) and (now.day == data['day'][ind]):
        print(f"Match: {data['name'][ind]}")
        with open(random.choice(letters)) as letter:
            contents = letter.read()
        new_contents = contents.replace("[NAME]", data['name'][ind])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            print(f"Sending Email to {data['name'][ind]}")
            connection.sendmail(from_addr=my_email, to_addrs=data['email'][ind], msg="Subject:Happy Birthday"
                                                                                              f"\n\n{new_contents}")