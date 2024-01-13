from app.models.item import Item
from app.utils.constant import ALL_CATEGORIES
from app.utils.db_utils import connect_to_database

FETCH_ALL_ITEMS_QUERY = "SELECT id, name, category, price, last_updated_dt FROM t_product_item"
FETCH_CATEGORY_ITEMS_QUERY = (
    "SELECT id, name, category, price, last_updated_dt FROM t_product_item "
    "WHERE category = %s"
)


def fetch_items_from_database(cursor, category):
    query = FETCH_ALL_ITEMS_QUERY if category == ALL_CATEGORIES else FETCH_CATEGORY_ITEMS_QUERY
    parameters = (category,) if category != ALL_CATEGORIES else None

    cursor.execute(query, parameters)

    return [
        Item(id, name, category, price, last_updated)
        for id, name, category, price, last_updated in cursor.fetchall()
    ]


def calculate_total_price(items):
    return sum(float(item.price) for item in items)


def group_items_by_category(items_data):
    grouped_items = {}

    for item in items_data:
        item_category = item.category
        item_price = float(item.price)

        if item_category in grouped_items:
            grouped_items[item_category]['total_price'] += item_price
            grouped_items[item_category]['count'] += 1
        else:
            grouped_items[item_category] = {
                'category': item_category, 'total_price': item_price, 'count': 1}

    return list(grouped_items.values())


def aggregate_items_by_category(category_data):
    try:
        category = category_data.get("category", ALL_CATEGORIES)

        connection = connect_to_database()
        cursor = connection.cursor()

        items_data = fetch_items_from_database(cursor, category)

        grouped_items = group_items_by_category(items_data)

        return {"items": grouped_items}

    finally:
        cursor.close()
        connection.close()
