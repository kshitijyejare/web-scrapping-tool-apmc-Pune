from bs4 import BeautifulSoup
import bs4
import requests
import openpyxl
import pandas as pd

url = 'http://www.puneapmc.org/history.aspx?id=Rates3289'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get('http://www.puneapmc.org/history.aspx?id=Rates3289')
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

productlist = soup.find_all('div',class_='item')

print(productlist)
