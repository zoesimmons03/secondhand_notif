from bs4 import BeautifulSoup as bs
import requests as r
from currency_converter import CurrencyConverter as cc
import re
import scraper_funcs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

def rakuma_url(keyword, page=10, category='pass'):
    if category == 'pass':
        return f'https://buyee.jp/rakuma/search?keyword={keyword}&status=on_sale'
    return f'https://buyee.jp/rakuma/search?keyword={keyword}&status=on_sale&lang=en&page=1&category_id={scraper_funcs.category_dict[category][page]}'

def parse_pgs():
    keyword = input('what 2 search?')
    category = input(f'What category?\nOptions:\n{[print(f"{key}" for key in scraper_funcs.category_dict.keys)]}')
    ask = input("enter 'y' to set # of pages to browse thru? (default 10)")
    if ask == 'y':
        pgs = int(input('how many pages u want me 2 browse thru?'))
    rakuma_url(keyword, category, pgs=10)



    
def rakuma_parse(url):

    listings = []

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
            for item in items:
                name = item['name']
                price = item['price']
                link = f"https://buyee.jp/rakuma/item/{item['id']}?conversionType=service_page_search"
                listings.append({'name': name, 'yen_price': price, 'link': link})
        else:
            print("❌ No JSON match found in HTML.")
    except Exception as e:
        print(f"❌ Error parsing JSON from KO block: {e}")
    return listings


url = rakuma_url('liz lisa')
print(rakuma_parse(url))