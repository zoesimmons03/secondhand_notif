from bs4 import BeautifulSoup as bs
import requests as r
from currency_converter import CurrencyConverter as cc
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import os
from dotenv import load_dotenv, dotenv_values
from scrapers import *
from utils import *

load_dotenv()

env_path = os.path.join(os.path.dirname(__file__), '.env')
sql_conn = {**dotenv_values(env_path)}

def parse_pgs():
    keyword = input('what 2 search?')
    category = input(f'What category?\nOptions:\n{[({key}) for key in scraper_funcs.category_dict.keys]}')
    ask = input("enter 'y' to set # of pages to browse thru? (default 10)")
    
    pgs = 10
    if ask == 'y':
        pgs = int(input('how many pages u want me 2 browse thru?'))

    m_listings = []
    r_listings = []
    y_listings = []
    for pg in range(1, pgs+1):    
        m_url = mercari_url(keyword, category, pg)
        r_url = rakuma_url(keyword, category, pg)
        y_url = yahoo_url(keyword, category, pg)


    for pg in range(1, pgs+1):
        m_listings.append(mercari_parse(m_url))
        r_listings.append(rakuma_parse(r_url))
        y_listings.append(yahoo_parse(y_url))
    return [m_listings, y_listings, r_listings]

def parse_n_add():    
    listings = parse_pgs()    
    for site in listings:
        for list in site:
            add_listing(list)
            print('all new listings added')


parse_n_add()