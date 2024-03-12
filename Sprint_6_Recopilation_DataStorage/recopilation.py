import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
r = requests.get(URL)
soup = BeautifulSoup(r.text,'lxml')

headings = soup.find('tr',attrs={'style':'text-align: right;'})

columns_name = [head.get_text() for head in headings.find_all('th')]

info = soup.find('tbody')

data = []

for row in info.find_all('tr'):
    rows = [r.get_text() for r in row.find_all('td')]
    data.append(rows)
    
weather_records = pd.DataFrame(columns=columns_name,data=data)
print(weather_records)