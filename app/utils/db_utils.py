import mysql.connector
import os


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
