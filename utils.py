from  dane import users_list
from bs4 import BeautifulSoup
import requests
import folium

def add_sql(lamus):
    sql_query = sqlalchemy.text(f"INSERT INTO public.my_table(name) VALUES ('{lamus}');")
    connection.execute(sql_query)
    connection.commit()

def remove_sql(lamus):
    sql_query = sqlalchemy.text(f"DELETE FROM public.my_table WHERE name = '{lamus}';")
    connection.execute(sql_query)
    connection.commit()

def updage_sql(outout,inin):
    sql_query = sqlalchemy.text(f"UPDATE public.my_table SET name='{inin}' WHERE name='{outout}';")
    connection.execute(sql_query)
    connection.commit()
# TODO funkcje wyżej rozwinąć do postaci domyślnej bazy, dodać elementy, dodać do analicznych (je też uzupełnić)

def add_user_to(users_list:list) -> None:
    name = input('Pod1aj imię: ')
    nick = input('Podaj ksyweczke: ')
    post = int(input('Ile wstawił postuf: '))
    city = input('Podaj meline: ')
    users_list.append({"name": name, "nick": nick, "posts": post, 'city':city})

def remove_user_from(users_list:list) -> None:
    tp_list =[]
    name = input('kogo chcesz wykopac :')
    for user in users_list:
        if user['name']== name:
            tp_list.append(user)
    print('znaleziono takich uzytkownikuw:')
    print('0 usuwa wszystkich')
    for numerek, user_to_be_removed in enumerate(tp_list):
        print(numerek+1, user_to_be_removed)
    numer = int(input('wybierz kościa do wyautowania: '))
    if numer == 0:
        for user in tp_list:
            users_list.remove(user)
    else:
        users_list.remove(tp_list[numer-1])

def show_users_from(users_list:list) -> None:
    for user in users_list:
        # print(user['nick'], 'dodal tyle ', user['posts'], 'postuf')
        print(f'dodal {user["name"]} tyle {user["posts"]} postuf')

def GUI(users_list):
    while True:
        print('\nWitajze ksieciuniuniu\n'
            f'0: mam dosc wychodze\n'
            f'1: wyswietl uytkownikow\n'
            f'2: dodaj ich\n'
            f'3: usun frajerof\n'
            f'4. modyfikuj wacpanuw\n'
            f'5. mapa ćwoka\n'
            f'6. pejzarz mułów')
        wyb = int(input('podaj docelowa funkcja '))
        print('wybrano', wyb)

        match wyb:
            case 0:
                print('\nsajonara')
                break
            case 1:
                print('wyswietlam liste')
                show_users_from(users_list)
            case 2:
                print('dodawanie')
                add_user_to(users_list)
            case 3:
                print('usuwanie')
                remove_user_from(users_list)
            case 4:
                print('modyfikacjion')
                update_user(users_list)
            case 5:
                print('rysuj mape ćwoka:')
                user = input('podaj jego godności: ')
                for item in users_list:
                    if item['name'] == user:
                        get_map_of_single(item)
            case 6:
                print('Wielki pejzarz wszsytkich mółów')
                get_map_of(users_list)

def update_user(users_list: list[dict, dict]) -> None:
    nick_of_user = input('Podaj nick użytkownika do modyfikacji ')
    print(f'Wpisano {nick_of_user}')
    for user in users_list:
        if user['nick'] == nick_of_user:
            print('znaleziono')
            new_name = input('Podaj nowe imię użytkownika ')
            user['name'] = new_name
            new_nick = input('Podaj nowy nick użytkownika ')
            user['nick'] = new_nick
            new_posts = input('Podaj nową ilość postów ')
            user['posts'] = new_posts

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
    folium.Marker(location=siti, popup=f"Melina osobliwości\n{user['name']}").add_to(mapa)

    mapa.save(f'map_{user["name"]}.html')
    print('\nWydano')

def get_map_of(users):

    mapa = folium.Map(location=[52.3, 21.0] , tiles='OpenStreetMap', zoom_start=7)
    
    for user in users:
        aa = get_coords(city=user['city'])
        folium.Marker(location=aa, popup=f"HALABARDAAAA\n{user['name']}").add_to(mapa)
    print('\nWydrukowano')
    mapa.save(f'mapeeeczka.html')

def pogoda_z(town:str):
    
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{town}"
    return requests.get(url).json()
