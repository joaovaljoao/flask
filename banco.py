import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() 

RDS_HOST = os.getenv('RDS_HOST')
RDS_USER = os.getenv('RDS_USER')
RDS_DB = os.getenv('RDS_DB')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')
RDS_PORT = os.getenv('RDS_PORT')

def connect():
    return psycopg2.connect(
        host=RDS_HOST,
        user=RDS_USER,
        database = RDS_DB,
        password=RDS_PASSWORD,
        port=RDS_PORT
    )

conn = connect()

def get_collumns_name(table_name):
    with conn.cursor() as cur:
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        collumns = cur.fetchall()
    return [i[0] for i in collumns]
    
def get_all():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM servidores")
        users = cur.fetchall()
    return users

def get_center(centro):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM servidores where uorg_lotacao_atual = %s", (centro, ))
        users = cur.fetchall()
    return users

if __name__ == '__main__':
    for one in get_all():
        print(one)
    
