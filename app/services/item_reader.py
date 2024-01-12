from datetime import datetime

from app.utils.db_utils import execute_query, connect_to_database, fetch_all


class Item:
    def __init__(self, id, name, category, price, last_updated):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.last_updated = last_updated


def fetch_items_from_database(cursor, dt_from, dt_to):
    query = (
        "SELECT id, name, category, price, last_updated_dt FROM t_product_item "
        "WHERE last_updated_dt BETWEEN %s AND %s"
    )
    parameters = (dt_from, dt_to)

    execute_query(cursor, query, parameters)
    return [Item(id, name, category, price, last_updated) for id, name, category, price, last_updated in
            fetch_all(cursor)]


def calculate_total_price(items):
    return sum(float(item.price) for item in items)


def get_items_by_last_updated_dt(date_range):
    try:
        with connect_to_database() as connection, connection.cursor() as cursor:
            dt_from = datetime.strptime(date_range["dt_from"], "%Y-%m-%d %H:%M:%S")
            dt_to = datetime.strptime(date_range["dt_to"], "%Y-%m-%d %H:%M:%S")

            items_data = fetch_items_from_database(cursor, dt_from, dt_to)

            filtered_items = [
                {"id": item.id, "name": item.name,
                 "category": item.category, "price": item.price}
                for item in items_data
            ]
            total_price = calculate_total_price(items_data)

            result = {"items": filtered_items,
                      "total_price": "{:.2f}".format(total_price)}
            return result

    except Exception as e:
        print(f"Error: {e}")
