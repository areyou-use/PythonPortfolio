"""
Web scraper that checks product's a price and sends an email notification below a specific threshold
"""

import os
from dotenv import load_dotenv

from scrapper import Scrapper
import smtplib

load_dotenv()

SOURCE_EMAIL = os.getenv("PRICE_TRACKER_SOURCE_EMAIL")
PASSWORD = os.getenv("PRICE_TRACKER_PASSWORD")
SMTP = os.getenv("PRICE_TRACKER_SMTP")
TARGET_EMAIL = os.getenv("PRICE_TRACKER_TARGET_EMAIL")

website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
price_threshold = 100

def send_mail():
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=SOURCE_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SOURCE_EMAIL,
                            to_addrs=TARGET_EMAIL,
                            msg=f"Subject:Price alert\n\nPrice below 100$\n\n{website}")
    print(f"Mail sent. Price: {item_price}")

sc = Scrapper()
item_price = sc.get_item_price(website)

if item_price < price_threshold:
    send_mail()
else:
    print(f"Item price: {item_price}")