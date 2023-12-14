## nalezy dodac ectation

import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String
from faker import Faker
import random

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

class User(Base):
    __tablename__ = 'ojojoj'

    id = Column(Integer(),primary_key=True)
    name = Column(String(100),nullable=True)
    location = Column('geom', Geometry(geometry_type='POINT', srid=4326), nullable=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
