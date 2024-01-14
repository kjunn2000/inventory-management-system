from app.models.item import Item
from app.utils.db_utils import get_database_connection

SELECT_ITEM_BY_NAME = "SELECT * FROM t_product_item WHERE name = %s"
UPDATE_ITEM_QUERY = "UPDATE t_product_item SET price=%s, last_updated_dt=NOW() WHERE name=%s;"
INSERT_ITEM_QUERY = "INSERT INTO t_product_item (name, category, price, last_updated_dt) VALUES (%s, %s, %s, NOW());"
SELECT_ALL_ITEMS_QUERY = "SELECT id, name, category, price, last_updated_dt FROM t_product_item"
SELECT_ITEMS_BY_DT_WHERE_CLAUSE_QUERY = " WHERE last_updated_dt BETWEEN %s AND %s"
SELECT_ITEMS_BY_CATEGORY_WHERE_CLAUSE_QUERY = " WHERE category = %s"


def item_exists(name):
    with get_database_connection() as (_, cursor):
        cursor.execute(SELECT_ITEM_BY_NAME, (name,))
        return cursor.fetchone() is not None


def update_item(new_item):
    with get_database_connection() as (connection, cursor):
        update_values = (new_item.price, new_item.name)
        cursor.execute(UPDATE_ITEM_QUERY, update_values)

        cursor.execute(SELECT_ITEM_BY_NAME, (new_item.name,))
        result = cursor.fetchone()

        connection.commit()

        return result[0]


def create_item(new_item):
    with get_database_connection() as (connection, cursor):
        insert_values = (new_item.name, new_item.category, new_item.price)
        cursor.execute(INSERT_ITEM_QUERY, insert_values)

        connection.commit()

        return cursor.lastrowid


def extract_items_from_cursor(cursor_results):
    return [Item(id, name, category, price, last_updated) for id, name, category, price, last_updated in cursor_results]


def get_items():
    with get_database_connection() as (_, cursor):
        cursor.execute(SELECT_ALL_ITEMS_QUERY)
        return extract_items_from_cursor(cursor.fetchall())


def get_items_by_dt(dt_from, dt_to):
    with get_database_connection() as (_, cursor):
        cursor.execute(f"{SELECT_ALL_ITEMS_QUERY}{SELECT_ITEMS_BY_DT_WHERE_CLAUSE_QUERY}", (dt_from, dt_to))
        return extract_items_from_cursor(cursor.fetchall())


def get_items_by_category(category):
    with get_database_connection() as (_, cursor):
        cursor.execute(f"{SELECT_ALL_ITEMS_QUERY}{SELECT_ITEMS_BY_CATEGORY_WHERE_CLAUSE_QUERY}", (category,))
        return extract_items_from_cursor(cursor.fetchall())
