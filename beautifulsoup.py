import requests
from bs4 import BeautifulSoup

# URL
url = f"https://www.cnbc.com/world/?region=world"

# Connecting to URL with GET
response = requests.get(url)

# Converting response content into a soup
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

