#Site Indexs:
#yahoo fleamarket: 0
#mercari: 1
#rakuma: 2

import requests as requests
import re

def url_to_html(url):
    html = requests.get(url)
    return html

def convert_yen(yen):
    price = re.rub(r"[^\d]", '', yen)
    return int(price)


category_dict = {'all_fashion': [13457, 3088, 'pass', ],
                 'all_mens': [2495, 2, 10005],
                 'm_pants': [36624, 32, 562, ],
                 'm_tops': [36504, 30, 526, ], 
                 'm_shoes': [1740, 33, 572, ],
                 'm_accessories': [1695, 38, 606, ],
                 'm_jackets': [36583, 31, 539, ],
                 'all_womens': [2494, 1, 10001],
                 'w_pants': [36913, 13, 5, ],
                 'w_tops': [36861, 11, 1, ],
                 'w_shoes': [1729, 16, 4, ],
                 'w_accessories': [1667, 23, 13, ],
                 'w_jackets': [37052, 12, 2, ],
                 'w_skirts': [37073, 14, 6, ],
                 'w_dresses':[36887, 15, 3, ],
                 'w_bags': [1574, 20, 7,]}
