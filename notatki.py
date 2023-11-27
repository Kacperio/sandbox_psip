from bs4 import BeautifulSoup
import requests
import re

miasteczka = ['Kutno', 'Warszawa', 'Zamość']
# city = input('Podaj nazwę jakiejś dziury: ')
# city = 'Kutno'

def get_coords(city:str)->list[float,float]:

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_htlm = BeautifulSoup(response.text,'html.parser')

    res_h_lat = response_htlm.select('.latitude')[1].text # . bo class
    res_h_lat = float(res_h_lat.replace(',','.'))

    # print(res_h_lat[23:-7])
    # lt = re.sub("(\<).*?(\>)", repl='', string=res_h_lat, count=0, flags=0)

    res_h_lon = response_htlm.select('.longitude')[1].text # . bo class
    res_h_lon = float(res_h_lon.replace(',','.'))

    return [res_h_lat,res_h_lon]

for xx in miasteczka:
    print(get_coords(xx))