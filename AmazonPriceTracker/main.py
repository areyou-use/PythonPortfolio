import os
from dotenv import load_dotenv

from scrapper import Scrapper
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("PRICE_TRACKER_EMAIL")
PASSWORD = os.getenv("PRICE_TRACKER_PASSWORD")
SMTP = os.getenv("PRICE_TRACKER_SMTP")

website = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

def send_mail():
    with smtplib.SMTP(SMTP) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="arektest@onet.pl",
                            msg=f"Subject:Price alert\n\nPrice below 100$\n\n{website}")
    print(f"Mail sent. Price: {item_price}")

sc = Scrapper()

# item_price = sc.get_item_price("https://appbrewery.github.io/instant_pot/")
item_price = sc.get_item_price(website)

if item_price < 100:
    send_mail()
else:
    print(f"Item price: {item_price}")