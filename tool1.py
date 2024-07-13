from bs4 import BeautifulSoup
import bs4
import requests
import openpyxl
import pandas as pd

baseurl = 'http://www.puneapmc.org/rates.aspx'

r = requests.get('http://www.puneapmc.org/history.aspx?id=Rates3997')
soup = BeautifulSoup(r.content,'lxml')


# Now you can extract the data as needed
datex = soup.find_all('th')

print(datex)
