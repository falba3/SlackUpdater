import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

# Loading API KEY
load_dotenv()
API_KEY = os.getenv("API_KEY")

# URL
bible_id = "65eec8e0b60e656b-01"
url = f"https://api.scripture.api.bible/v1/bibles/{bible_id}"

# Connecting to URL with GET
response = requests.get(url, headers={'api-key': API_KEY})
print(response.content)


# # soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
