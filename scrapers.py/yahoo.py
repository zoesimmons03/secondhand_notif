from bs4 import BeautifulSoup as bs
import requests as r
from currency_converter import CurrencyConverter as cc
import re
import scraper_funcs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def yahoo_url(keyword, category, page):
    if category == 'pass':
        return f'https://buyee.jp/paypayfleamarket/search?keyword={keyword}'
    return f'https://buyee.jp/paypayfleamarket/search?keyword={keyword}&category_id={scraper_funcs.category_dict[category][0]}'


def parse_html(urll):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'}
    listing_list = []
    c = cc()


    options = Options()
    options.add_argument("--headless")  # comment this out to see browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(urll)
    time.sleep(3)  # Wait for JavaScript to load listings

    soup = bs(driver.page_source, 'html.parser')
    driver.quit()

    listings = soup.select('li.list')
    for listing in listings:
        try:
            a_link = listing.find('a')['href']
            img_link = (listing.find("img", class_="thumbnail"))['src'].text.strip()
            item_name = listing.find("img", class_="thumbnail")['alt'].text.strip()
            price = listing.find('p', class_='price-fx')
            usd_price = price.text.strip().replace('(', '').replace(')','')

            listing_list.append({'link': link, 'img_link':img_link, 'item_name': item_name, 'yen_price': usd_price})
        except Exception as e:
            print(f'error pasing a listing: {e}')
            continue
    return listing_list


ok = parse_html('https://buyee.jp/paypayfleamarket/search?keyword=ppfm&category_id=13457')
print(ok)