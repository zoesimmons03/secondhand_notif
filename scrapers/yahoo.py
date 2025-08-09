from bs4 import BeautifulSoup as bs
import requests as r
from currency_converter import CurrencyConverter
import re
from scraper_funcs import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def yahoo_url(keyword, category='pass', page=10):
    if category == 'pass':
        return f'https://buyee.jp/paypayfleamarket/search?keyword={keyword}'
    return f'https://buyee.jp/paypayfleamarket/search?keyword={keyword}&category_id={category_dict[category][0]}'


def yahoo_parse(url):

    listings = []
    c = CurrencyConverter()

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")


    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)

    html = driver.page_source
    driver.quit()

    try:
        pattern = r'"impressions"\s*:\s*({.*?})\s*\}\s*\)\s*\-\->'  # better scoped
        match = re.search(pattern, html, re.DOTALL)
        if match:
            impressions_json = match.group(1)
            impressions_data = json.loads(impressions_json)
            items = impressions_data.get("items", [])
            print(f"Found {len(items)} items in JSON data")
            print(items)
            for item in items:
                pass
                name = item['name']
                price = item['price']
                usd_price = c.convert(price, 'JPY', 'USD')
                link = f"https://buyee.jp/paypayfleamarket/item/{item['id']}?conversionType=service_page_search"
                listings.append({'name': name, 'usd': f'${usd_price:.2f}', 'yen_price': f'{price} YEN', 'link': link})
        else:
            print("❌ No JSON match found in HTML.")
    except Exception as e:
        print(f"❌ Error parsing JSON from KO block: {e}")
    return listings



url = yahoo_url('hysteric glamour', category='pass', page=10)
listings = yahoo_parse(url)
for list in listings:
    print(list)