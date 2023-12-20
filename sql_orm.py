from dane import users_list
from dml import db_params
from utils import get_coords
import folium
from sqlalchemy import Sequence, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from geoalchemy2 import Geometry

engine = create_engine(db_params)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users_of_users"
    
    id = Column(Integer(), Sequence("user_id_seq"),primary_key=True)
    name = Column(String(100),nullable=True)
    nick = Column(String(100),nullable=True)
    posts = Column(Integer(),nullable=True)
    city = Column(String(100),nullable=True)
    location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)
    
    def __repr__(self):
        return "<User(name='%s', nick='%s', posts='%s', city='%s', geom='%s')>" % (
            self.name,
            self.posts,
            self.nick,
            self.city,
            self.location
        )
        
Base.metadata.create_all(engine)

def GUI_orm():
    while True:
        print('\nWitajze księciuniuniu\n'
            f'0: mam dosc wychodze\n'
            f'1: luknij użytkowników\n'
            f'2: dodaj jakieś lamusika\n'
            f'3: usuń frajeróf\n'
            f'4. modyfikuj waćpanów\n'
            f'5. noc oczyszczenia \n'
            f'6. pokaż jedną z melin \n'
            f'7. Wielki Pejżarz Meliński \n'
            f'8. dodanie kilku znanych mordek \n')
        wyb = int(input('podaj docelową funkcja: '))
        print(f'wybrano {wyb}: \n')

        match wyb:
            case 0:
                print('\nSajonara')
                session.flush()
                engine.dispose()
                break
            case 1:
                print('Wyswietlam listeczkę')
                select_all_sql()
            case 2:
                print('Dodawajszyn')
                insert_sql()
            case 3:
                print('Usuwajszyn')
                delete_sql()
            case 4:
                print('Modyfikacjion')
                update_sql()
            case 5:
                print('Nikt nie przetrwał')
                clean_table()
            case 6:
                print('Rysuj mape ćwoka:')
                user = input('Podaj jego godności superbohatera (nick): ')
                muls_form_db = session.query(User).filter(User.nick == user)
                for mul in muls_form_db:
                    cc = mul.city
                    nn = mul.name
                    get_map_of_single(cc, nn)
            case 7:
                print('Było cieżko, ale się udała')
                get_map_of_all()
            case 8:
                print('Impreze czas zacząć')
                refill_db()

### Query/funkszyn

def insert_sql():
    aa = input('Wskaż jego melinę: ')
    siti = get_coords(aa)

    add_user =User(
        name = input('Podaj godność: '),
        nick = input('Podaj ksyweczkę: '),
        posts = input('Podaj liczbę postów: '),
        city = aa,
        location=f'POINT({siti[1]} {siti[0]})'
    )
    session.add(add_user)
    session.commit()

def select_all_sql():
    muls_form_db = session.query(User).all()
    if muls_form_db == []:
        print('Nie ma NIKOGO do zabawy')
    else:
        for user in muls_form_db:
            print(f"Użytkownik {user.name} mający bazę w {user.city} zaśmiecił tablicę {user.posts} wpisami o niczym")
            
def delete_sql():
    outer = input('Imię śwoka do wyaotowania: ')
    muls_form_db = session.query(User).filter(User.name == outer)

    tp_list =[]
    
    for user in muls_form_db:
        if user.name == outer:
            tp_list.append(user)
    print('znaleziono takich uzytkownikuw:')
    print('0 usuwa wszystkich')
    
    for numerek, user_to_be_removed in enumerate(tp_list):
        print(numerek+1, user_to_be_removed)
    numer = int(input('wybierz kościa do wyautowania: '))
    
    if numer == 0:
        for user in tp_list:
            session.delete(user)
    else:
        aa = tp_list[numer-1]
        session.delete(aa)
    
    session.commit()
    
def update_sql():
    outer = input('Ksyweczkę lamusika do podmianki: ')
    muls_form_db = session.query(User).all()
    for user in muls_form_db:
        if user.nick == outer:
            user.name = input('Podaj nową godność: ')
            user.nick = input('Podaj nową ksyweczkę: ')
            user.posts = input('Podaj aktualną liczbę postów: ')
            user.city = input('Wskaż jego melinę: ')
            user.location = f'POINT({get_coords(user.city)[1]} {get_coords(user.city)[0]})'
    session.commit()

def refill_db():
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
    
def clean_table():
    muls_form_db = session.query(User).all()
    for mul in muls_form_db:
        session.delete(mul) 
    session.commit()

### Maps

def get_map_of_single(city, name):
    siti = get_coords(city)
    mapa = folium.Map(location=siti, tiles='OpenStreetMap', zoom_start=14)
    folium.Marker(location=siti, popup=f"Melina osobliwości\n{name}").add_to(mapa)

    mapa.save(f'map_{name}.html')
    print('\nWydano')

def get_map_of_all():
    mapa = folium.Map(location=[52.3, 21.0] , tiles='OpenStreetMap', zoom_start=7)
    
    muls_form_db = session.query(User).all()
    for user in muls_form_db:
        aa = get_coords(user.city)
        folium.Marker(location=aa, popup=f"Gdzień tu campi\n{user.name}").add_to(mapa)
    print('\nWydrukowano')
    mapa.save(f'mapeeeczka.html')
