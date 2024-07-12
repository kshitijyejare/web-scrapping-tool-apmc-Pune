from bs4 import BeautifulSoup
import bs4
import requests
import openpyxl
import pandas as pd

baseurl = 'http://www.puneapmc.org/rates.aspx'

r = requests.get('http://www.puneapmc.org/history.aspx?id=Rates3997')
soup = BeautifulSoup(r.content,'lxml')

productlist = soup.find_all('div',class_='item')

print(productlist)
