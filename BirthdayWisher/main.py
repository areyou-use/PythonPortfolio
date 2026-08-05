"""
Script that checks birthday dates in csv and sends an email with birthday wishes
"""

import pandas, datetime, os, random, smtplib, os
from dotenv import load_dotenv

load_dotenv()

SOURCE_EMAIL = os.getenv("WISHER_SOURCE_EMAIL")
PASSWORD = os.getenv("WISHER_PASSWORD")

today_raw = datetime.datetime.now()
today = (today_raw.month, today_raw.day)
df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

def send_wishes():
    if today in birthdays_dict.keys():
        random_letter_filename = "LetterTemplates/" + random.choice(os.listdir("LetterTemplates"))
        with open(random_letter_filename) as file:
            letter_text = file.read()
            current_name = birthdays_dict[today]["name"]
            letter_text = letter_text.replace("[NAME]", current_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SOURCE_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SOURCE_EMAIL,
                                to_addrs="arektest@onet.pl",
                                msg=f"Subject:Birthday wishes\n\n{letter_text}")
    else:
        print("No matching birthdays")