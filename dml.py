## nalezy dodac ectation

import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String
# from utils import get_coords
from dane import users_list


load_dotenv()

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    database=os.getenv('POSTGRES_DB'),
    port=os.getenv('POSTGRES_PORT')
)

engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()
Session = sessionmaker(bind=engine)
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

def tabelko_tworca():
    Base = sqlalchemy.orm.declarative_base()
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


def add_sgl():
    # Base = sqlalchemy.orm.declarative_base()
    # Base.metadata.create_all(engine)
    
    dodajek = []
    name = input('Pod1aj imię: ')
    nick = input('Podaj ksyweczke: ')
    post = int(input('Ile wstawił postuf: '))
    melina = input('Podaj meline: ')
    dodajek.append({"name": name, "nick": nick, "posts": post, 'city':melina})

    qq =[]
    siti = get_coords(melina)
    qq.append(
        User(
            name = name,
            nick = nick,
            posts = post,
            city = melina,
            location = f'POINT({siti[1]} {siti[0]})'
            )
        )
    session.add_all(qq)
    session.commit
    