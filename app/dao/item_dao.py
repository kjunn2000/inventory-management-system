from app.models.item import Item
from app.utils.db_utils import execute_query, fetch_all
from app.utils.db_utils import get_database_connection


def item_exists(name):
    with get_database_connection() as (_, cursor):
        select_query = "SELECT * FROM t_product_item WHERE name = %s"
        cursor.execute(select_query, (name,))
        return cursor.fetchone() is not None


def update_item(new_item):
    with get_database_connection() as (connection, cursor):
        update_query = "UPDATE t_product_item SET price=%s, last_updated_dt=NOW() WHERE name=%s;"
        update_values = (new_item.price, new_item.name)
        cursor.execute(update_query, update_values)

        select_query = "SELECT id FROM t_product_item WHERE name = %s"
        cursor.execute(select_query, (new_item.name,))

        result = cursor.fetchone()

        connection.commit()

        return result[0]


def create_item(new_item):
    with get_database_connection() as (connection, cursor):
        insert_query = "INSERT INTO t_product_item (name, category, price, last_updated_dt) VALUES (%s, %s, %s, NOW());"
        insert_values = (new_item.name, new_item.category, new_item.price)
        cursor.execute(insert_query, insert_values)

        connection.commit()

        return cursor.lastrowid


def get_items():
    with get_database_connection() as (_, cursor):
        query = (
            "SELECT id, name, category, price, last_updated_dt FROM t_product_item "
        )

        execute_query(cursor, query)
        return [Item(id, name, category, price, last_updated) for id, name, category, price, last_updated in
                fetch_all(cursor)]


def get_items_by_dt(dt_from, dt_to):
    with get_database_connection() as (_, cursor):
        query = (
            "SELECT id, name, category, price, last_updated_dt FROM t_product_item "
            "WHERE last_updated_dt BETWEEN %s AND %s"
        )
        parameters = (dt_from, dt_to)

        execute_query(cursor, query, parameters)
        return [Item(id, name, category, price, last_updated) for id, name, category, price, last_updated in
                fetch_all(cursor)]


def get_items_by_category(category):
    with get_database_connection() as (_, cursor):
        query = (
            "SELECT id, name, category, price, last_updated_dt FROM t_product_item "
            "WHERE category = %s"
        )
        parameters = (category,)

        execute_query(cursor, query, parameters)
        return [Item(id, name, category, price, last_updated) for id, name, category, price, last_updated in
                fetch_all(cursor)]
