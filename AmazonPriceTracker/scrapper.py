from bs4 import BeautifulSoup
import requests



class Scrapper:
    def __init__(self):
        self.headers = {
            "User-Agent": "CCBot/2.0(https://commoncrawl.org/faq/)",
            "Accept-Language": "en-US,en;q=0.5"
        }

    def get_item_price(self, webpage):
        response = requests.get(webpage, headers=self.headers)
        webpage_data = response.text
        soup = BeautifulSoup(webpage_data, "html.parser")
        whole_price = soup.find(name="span", class_="a-price-whole").get_text().strip(".")
        fraction_price = soup.find(name="span", class_="a-price-fraction").get_text()
        whole_price = float(whole_price)
        fraction_price = float(fraction_price)/100
        total_price = float(whole_price + fraction_price)
        return total_price