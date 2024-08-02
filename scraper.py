import requests
from bs4 import BeautifulSoup


url = "https://www.cnbc.com/finance/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
