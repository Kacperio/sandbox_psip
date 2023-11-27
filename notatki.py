from bs4 import BeautifulSoup
import requests

adres_URL = f'https://pl.wikipedia.org/wiki/Kutno'

response = requests.get(url=adres_URL)
BeautifulSoup(response.text,'html.parsel')