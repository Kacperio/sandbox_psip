from  dane import users_list
from bs4 import BeautifulSoup
import requests
import folium
import sqlalchemy.orm
from dotenv import load_dotenv
from geoalchemy2 import Geometry
import os
from sqlalchemy import Column, Integer, String
from dml import db_params

load_dotenv()
engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base = sqlalchemy.orm.declarative_base()



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
            f'6. pejzarz mułów\n'
            f'SQL wita\n'
            f'7. utwórz tabelke\n'
            f'8. wyczyść do zera baze\n'
            f'9. pierwsze uruchomienie -> tabella i danne (przykładowe) oczywiście\n')
        wyb = int(input('podaj docelowa funkcja '))
        print('wybrano', wyb)

        match wyb:
            case 0:
                print('\nsajonara')
                session.flush()
                connection.close()
                engine.dispose()
                break
            case 1:
                print('wyswietlam liste')
                show_sql(db_params)
            case 2:
                print('dodawanie')
                add_sql(users_list, db_params)
            case 3:
                print('usuwanie')
                remove_sql(users_list, db_params)
            case 4:
                print('modyfikacjion')
                updage_sql(users_list, db_params)
            case 5:
                print('rysuj mape ćwoka:')
                user = input('podaj jego godności: ')
                for item in users_list:
                    if item['name'] == user:
                        get_map_of_single(item)
            case 6:
                print('Wielki pejzarz wszsytkich mółów')
                get_map_of(users_list)
            case 7:
                print('Utworzono uber tabbelle')
                stol_kreajszyn(db_params)
            case 8:
                print('Fajnie było, ale się skończyło\nniezostało nic')
                calkowita_zaglada(db_params)
            case 9:
                print('Mosz, bo odczegoś trza zacząć')
                tabelko_tworca_i_dodanie(db_params)

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


### SQL

class User(Base):
    __tablename__ = 'list_of_muls'

    id = Column(Integer(),primary_key=True)
    posts = Column(Integer(),nullable=True)
    name = Column(String(100),nullable=True)
    nick = Column(String(100),nullable=True)
    city = Column(String(100),nullable=True)
    location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

def aktulizajszyn(listeczka, db_params):        ## raczej dublejszyn
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    
    cwok_list: list = []
    for cwok in listeczka:
        siti = get_coords(cwok['city'])
        cwok_list.append(
            User(
                name = cwok['name'],
                posts = cwok['posts'],
                nick = cwok['nick'],
                city = cwok['city'],
                location = f'POINT({siti[1]} {siti[0]})'
            )
        )
    session.add_all(cwok_list)
    session.commit()

def tabelko_tworca_i_dodanie( db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    
    Base = sqlalchemy.orm.declarative_base()

    class User(Base):
        __tablename__ = 'list_of_muls'

        id = Column(Integer(),primary_key=True)
        posts = Column(Integer(),nullable=True)
        name = Column(String(100),nullable=True)
        nick = Column(String(100),nullable=True)
        city = Column(String(100),nullable=True)
        location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    Base.metadata.create_all(engine)
    
    cwok_list: list = []

    for cwok in users_list:
        siti = get_coords(cwok['city'])
        cwok_list.append(
            User(
                name = cwok['name'],
                posts = cwok['posts'],
                nick = cwok['nick'],
                city = cwok['city'],
                location = f'POINT({siti[1]} {siti[0]})'
            )
        )
    session.add_all(cwok_list)
    session.commit()

def add_sql(listeczka, db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    
    name = input('Pod1aj imię: ')
    nick = input('Podaj ksyweczke: ')
    post = int(input('Ile wstawił postuf: '))
    melina = input('Podaj meline: ')
    listeczka.append({"name": name, "nick": nick, "posts": post, 'city':melina})
    loc = get_coords(melina)
    sql_query = sqlalchemy.text(f"INSERT INTO public.list_of_muls(name, nick, city, posts, geom) VALUES ('{name}', '{nick}', '{melina}', '{post}', 'POINT({loc[1]} {loc[0]})');")
    
    connection.execute(sql_query)
    connection.commit()

def remove_sql(listeczka, db_params):
    
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    
    tp_list =[]
    name = input('kogo chcesz wykopac :')
    for user in listeczka:
        if user['name']== name:
            tp_list.append(user)
    print('znaleziono takich uzytkownikuw:')
    print('0 usuwa wszystkich')
    for numerek, user_to_be_removed in enumerate(tp_list):
        print(numerek+1, user_to_be_removed)
    numer = int(input('wybierz kościa do wyautowania: '))
    if numer == 0:
        for user in tp_list:
            listeczka.remove(user)
            print(user)
            print(type(user))
            sql_query = sqlalchemy.text(f"DELETE FROM public.list_of_muls WHERE name = '{user['name']}';")
    else:
        aa = tp_list[numer-1]
        listeczka.remove(aa)
        print(type(aa))
        print(aa['city'])
        sql_query = sqlalchemy.text(f"DELETE FROM public.list_of_muls WHERE nick = '{aa['nick']}';")
    
    connection.execute(sql_query)
    connection.commit()

def updage_sql(listeczka, db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    
    nick_of_user = input('Podaj nick użytkownika do modyfikacji ')
    print(f'Wpisano {nick_of_user}')
    for user in listeczka:
        if user['nick'] == nick_of_user:
            print('znaleziono')
            new_name = input('Podaj nowe imię użytkownika ')
            user['name'] = new_name
            new_nick = input('Podaj nowy nick użytkownika ')
            user['nick'] = new_nick
            new_posts = input('Podaj nową ilość postów ')
            user['posts'] = new_posts
            new_citi = input('Podaj nową melinę spotkaniową ')
            user['city'] = new_citi
            loc = get_coords(new_citi)
    
    sql_query = sqlalchemy.text(f"UPDATE public.list_of_muls SET name='{new_name}', posts='{new_posts}', nick='{new_nick}', city='{new_citi}', geom='POINT({loc[1]} {loc[0]})' WHERE nick='{nick_of_user}';")
    
    connection.execute(sql_query)
    connection.commit()

def calkowita_zaglada(db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    
    sql_query = sqlalchemy.text(f"DELETE FROM public.list_of_muls WHERE name != 'ARMAGEDDDDON';")
    
    connection.execute(sql_query)
    connection.commit()
    
def stol_kreajszyn(db_params):
    engine = sqlalchemy.create_engine(db_params)
    Base = sqlalchemy.orm.declarative_base()

    class User(Base):
        __tablename__ = 'list_of_muls'

        id = Column(Integer(),primary_key=True)
        posts = Column(Integer(),nullable=True)
        name = Column(String(100),nullable=True)
        nick = Column(String(100),nullable=True)
        city = Column(String(100),nullable=True)
        location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

    Base.metadata.create_all(engine)

def show_sql(db_params):
    engine = sqlalchemy.create_engine(db_params)
    connection = engine.connect()
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    muls_form_db = session.query(User).all()

    for user in muls_form_db:
        print(f"Użytkownik {user.name} mający bazę w {user.city} zaśmiecił tablicę {user.posts} wpisami o niczym")

def baza_to_zmienna(db_params):
    engine = sqlalchemy.create_engine(db_params)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    
    working_list = []
    muls_form_db = session.query(User).all()

    for user in muls_form_db:
        name = user.name
        nick = user.nick
        post = user.posts
        city = user.city
        working_list.append({"name": name, "nick": nick, "posts": post, 'city':city}) 

    return working_list

