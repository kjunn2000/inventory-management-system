from app.utils.db_utils import get_database_connection


def item_exists(name):
    with get_database_connection() as (_, cursor):
        select_query = "SELECT * FROM t_product_item WHERE name = %s"
        cursor.execute(select_query, (name,))
        return cursor.fetchone() is not None


def update_existing_item(new_item):
    with get_database_connection() as (connection, cursor):
        update_query = "UPDATE t_product_item SET price=%s, last_updated_dt=NOW() WHERE name=%s;"
        update_values = (new_item.price, new_item.name)
        cursor.execute(update_query, update_values)

        select_query = "SELECT id FROM t_product_item WHERE name = %s"
        cursor.execute(select_query, (new_item.name,))

        result = cursor.fetchone()

        connection.commit()

        return result[0]


def insert_new_item(new_item):
    with get_database_connection() as (connection, cursor):
        insert_query = "INSERT INTO t_product_item (name, category, price, last_updated_dt) VALUES (%s, %s, %s, NOW());"
        insert_values = (new_item.name, new_item.category, new_item.price)
        cursor.execute(insert_query, insert_values)

        connection.commit()

        return cursor.lastrowid
