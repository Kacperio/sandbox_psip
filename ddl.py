## Tutaj odbywają się rzeczy trochę tajemne

import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String
from faker import Faker
import random
from dml import User



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

Base = sqlalchemy.orm.declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

# ## Create

lista_mulow: list = []
fake = Faker()

for item in range(100):
    lista_mulow.append(
        User(
            name = fake.name(),
            location = f'POINT({random.uniform(14,24)} {random.uniform(49,55)})'
        )
    )


session.add_all(lista_mulow)
session.commit()

## Read

muls_form_db = session.query(User).all()
muls_form_db = session.query(User).filter(User.name=='Zdziuchu')

for user in muls_form_db:
    if user.name == 'Zdziuchu':
        user.name = 'Jachu'



session.flush()
connection.close()
engine.dispose()
