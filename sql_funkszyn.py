import sqlalchemy.orm
from dotenv import load_dotenv
from geoalchemy2 import Geometry
# import os
from sqlalchemy import Column, Integer, String
from utils import get_coords
from dane import users_list
from dml import db_params

load_dotenv()
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

def aktulizajszyn(listeczka, db_params):
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

def tabelko_tworca_i_dodanie(db_params):
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

def show_sql():
    muls_form_db = session.query(User).all()

    for user in muls_form_db:
        print(user.name)

# tabelko_tworca()
# calkowita_zaglada(db_params)
# stol_kreajszyn()
# show_sql()