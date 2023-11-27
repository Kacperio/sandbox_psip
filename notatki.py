from bs4 import BeautifulSoup
import requests
import re
import folium


user = {'city':"Kutno", "name":"Kacperek", "nick":"hajdun", "posts":12}
miasteczka = ['Kutno', 'Warszawa', 'Zamość']
# city = input('Podaj nazwę jakiejś dziury: ')
# city = 'Kutno'

def get_coords(city:str)->list[float,float]:

    adres_URL = f'https://pl.wikipedia.org/wiki/{city}'

    response = requests.get(url=adres_URL)
    response_htlm = BeautifulSoup(response.text,'html.parser')

    res_h_lat = response_htlm.select('.latitude')[1].text # . bo class
    res_h_lat = float(res_h_lat.replace(',','.'))

    res_h_lon = response_htlm.select('.longitude')[1].text # . bo class
    res_h_lon = float(res_h_lon.replace(',','.'))

    return [res_h_lat,res_h_lon]


def get_map_of_single(user:str):
    siti = get_coords(user['city'])

    mapa = folium.Map(location=siti, tiles='OpenStreetMap', zoom_start=14)
    folium.Marker(location=siti, popup=f"HALABARDAAAA\n{user['name']}").add_to(mapa)

    mapa.save(f'mapka{user["name"]}.html')

def get_map_of(coords: list, lista_imion):
    mapa = folium.Map(location=[52.3, 21.0] , tiles='OpenStreetMap', zoom_start=7)
    
    for user in users:
        aa = get_coords(city=user['city'])
        folium.Marker(location=aa, popup=f"HALABARDAAAA\n{user['name']}").add_to(mapa)
    mapa.save(f'mapeeeczka.html')

from dane import users_list

get_map_of(users_list)

    # siti = get_coords(user['city'])
    # mapa = folium.Map(location=get_coords(siti), tiles='OpenStreetMap', zoom_start=7)

    # for xx in miasteczka:
    #     folium.Marker(location=get_coords(siti), popup="HALABARDAAAA").add_to(mapa)














