import os
from contextlib import contextmanager

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

from app.utils.db_constant import ENV_MYSQL_HOST, ENV_MYSQL_USER, ENV_MYSQL_PASSWORD, ENV_MYSQL_DATABASE
from app.utils.error_message import DB_CONNECTION_ERROR

load_dotenv()


def connect_to_database():
    return mysql.connector.connect(
        host=os.getenv(ENV_MYSQL_HOST),
        user=os.getenv(ENV_MYSQL_USER),
        password=os.getenv(ENV_MYSQL_PASSWORD),
        database=os.getenv(ENV_MYSQL_DATABASE),
    )


@contextmanager
def get_database_connection():
    connection = None
    cursor = None
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        yield connection, cursor
    except Error as e:
        e.message = f"{DB_CONNECTION_ERROR}: {e}"
        raise e
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
