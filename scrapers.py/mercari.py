from bs4 import BeautifulSoup as bs
import requests as r
from currency_converter import CurrencyConverter as cc
import re
import scraper_funcs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def mercari_url(keyword, category, page):
    if category == 'pass':
        return f'https://buyee.jp/mercari/search?keyword={keyword}&status=on_sale'
    return f'https://buyee.jp/mercari/search?keyword={keyword}&status=on_sale&lang=en&page=1&category_id={scraper_funcs.category_dict[category][1]}'


def parse_html(urll):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15'}
    listing_list = []
    html = r.get(urll, headers=headers)
    print(html.status_code)     # Should be 200
    print(html.url)             # Should be the final URL (not redirected to /error)
    print(html.text[:1500])   
    soup = bs(html.content, 'html.parser')
    c = cc()

    listings = soup.select('div', class_='simple_item_Ewdl1')
    for listing in listings:
        try:
            a_link = listing.find('a', class_='simple_container_llX1q')['href']
            link = a_link['href'] if link else None
            img_link = (listing.find('img', class_='cdn_container_T7Lek'))['src']
            item_name = listing.find("span", class_="simple_name__XMcbt").text.strip()
            yen_price = listing.find('span', class_='simple_price_h13DP').text.strip()
            yen = yen_price.split()
            yen = scraper_funcs.convert_yen(yen)
            usd = round(c.convert(yen, 'JPY', 'USD'), 2)
            print(f'lineksssssss:{link, img_link, item_name, yen_price, usd}')

            listing_list.append({'link': link, 'img_link':img_link, 'item_name': item_name, 'yen_price': usd})
        except Exception as e:
            print(f'error pasing a listing: {e}')
            continue
    return listing_list



print(f"hai {parse_html('https://buyee.jp/mercari/search?keyword=ppfm&status=on_sale')}")





def scrape_buyee_mercari(keyword):
    # Build search URL
    url = f"https://buyee.jp/mercari/search?keyword={keyword}&status=on_sale&lang=en"

    print(f'URL: {url}')

    # Set up headless Chrome
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36")


    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # Wait for JS content to load
    time.sleep(3)

    # Parse the rendered HTML
    soup = bs(driver.page_source, "html.parser")
    driver.quit()
    print(f'SOUP{soup.prettify()}')
    listings = soup.find_all("div", class_="simple_item_Ewdl1")
    print(f"Found {len(listings)} listings.")
    
    for listing in listings:
        try:
            name = listing.find("span", class_="simple_name__XMcbt")
            name = name.text.strip() if name and 'span' in name.attrs else None
            price = listing.find("span", class_="simple_price_h13DP")
            price = price.text.strip() if price and 'span' in name.attrs else None
            print(f"{name} - {price}")
        except Exception as e:
            print(f"Error parsing: {e}")

scrape_buyee_mercari("ppfm")