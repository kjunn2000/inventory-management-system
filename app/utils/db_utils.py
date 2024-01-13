import os
from contextlib import contextmanager

import mysql.connector
from mysql.connector import Error


def get_database_config():
    return {
        'host': os.environ.get('MYSQL_HOST', 'localhost'),
        'user': os.environ.get('MYSQL_USER', 'admin'),
        'password': os.environ.get('MYSQL_PASSWORD', 'password'),
        'database': os.environ.get('MYSQL_DATABASE', 'inventory_management')
    }


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="admin",
        password="password",
        database="inventory_management",
    )


def execute_query(cursor, query, parameters=None):
    if parameters:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)


def fetch_all(cursor):
    return cursor.fetchall()


@contextmanager
def get_database_connection():
    config = get_database_config()
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        yield connection, cursor
    except Error as e:
        print(f"Error connecting to the database: {e}")
        raise
    finally:
        cursor.close()
        connection.close()
