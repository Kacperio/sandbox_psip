## Tutaj odbywają się rzeczy trochę tajemne

import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername='postgresql+psycopg2',
    username='postgres',
    password='123',
    host='localhost',
    database='postgres',
    port=5432
)

engine = sqlalchemy.create_engine(db_params)
connection = engine.connect()

lamus = 'stasiu'
mul = 'hajdun'


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

# updage_sql(mul, lamus)