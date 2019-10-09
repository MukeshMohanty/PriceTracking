import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal

URL = 'https://www.amazon.in/dp/B07BS4TJ43?pf_rd_p=a6f71a32-439a-4911-a54a-eefc42a5e0a1&pf_rd_r=6M91EF4FTWYY5EBYS01F'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
deal_price = soup.find(id="priceblock_dealprice").get_text()

converted_price = sub(r'[^\d.]', '', price)
converted_deal_price = sub(r'[^\d.]', '', deal_price)
final_price = Decimal(converted_price)
final_deal_price = Decimal(converted_deal_price)

print(title.strip())
print(converted_price)
print(converted_deal_price)