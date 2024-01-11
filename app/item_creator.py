import json
import os
import mysql.connector
from mysql.connector import Error
from models import item

def get_database_config():
    return {
        'host': os.environ.get('MYSQL_HOST', 'localhost'),
        'user': os.environ.get('MYSQL_USER', 'admin'),
        'password': os.environ.get('MYSQL_PASSWORD', 'password'),
        'database': os.environ.get('MYSQL_DATABASE', 'inventory_management')
    }

def format_price(price):
    try:
        price_float = float(price)
        formatted_price = "{:.2f}".format(price_float)
        return formatted_price
    except ValueError:
        raise ValueError("Invalid price format")

def item_exists(cursor, name):
    select_query = "SELECT * FROM t_product_item WHERE name = %s"
    cursor.execute(select_query, (name,))
    return cursor.fetchone() is not None

def update_existing_item(cursor, new_item):
    update_query = "UPDATE t_product_item SET price=%s, last_updated_dt=NOW() WHERE name=%s;"
    update_values = (new_item.price, new_item.name)
    cursor.execute(update_query, update_values)

def insert_new_item(cursor, new_item):
    insert_query = "INSERT INTO t_product_item (name, category, price, last_updated_dt) VALUES (%s, %s, %s, NOW());"
    insert_values = (new_item.name, new_item.category, new_item.price)
    cursor.execute(insert_query, insert_values)

def update_item_to_db(new_item, connection, cursor):
    try:
        new_item.price = format_price(new_item.price)

        if item_exists(cursor, new_item.name):
            update_existing_item(cursor, new_item)
        else:
            insert_new_item(cursor, new_item)

        connection.commit()

        return cursor.lastrowid

    except Error as e:
        print(e)
        raise e


def create_or_update_item(request):
    try:
        new_item = item.Item(**request)
        db_config = get_database_config()

        with mysql.connector.connect(**db_config) as connection, connection.cursor() as cursor:
            item_id = update_item_to_db(new_item, connection, cursor)

        return json.dumps({'id': item_id})
    
    except (Error, ValueError) as e:
        return json.dumps({'error': str(e)})