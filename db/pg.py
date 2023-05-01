import psycopg2
import json
with open('config.json') as json_data_file:
    config = json.load(json_data_file)['pgSql']

def connect():
    conn = psycopg2.connect(
        dbname=config['database'],
        user=config['username'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
    )
    return conn

def execute_query(conn, query, params=None):
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        result = cursor.fetchall()
    return result

def execute_insert(conn, query, params=None):
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
    except psycopg2.Error as e:
        print("PG SQL ENCOUNTERED AN ERROR")
