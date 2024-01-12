from app.utils.db_utils import connect_to_database


class Item:
    def __init__(self, id, name, category, price, last_updated):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.last_updated = last_updated


def fetch_items_from_database(cursor, category):
    if category == "all":
        query = "SELECT id, name, category, price, last_updated_dt FROM t_product_item"
        cursor.execute(query)
    else:
        query = (
            "SELECT id, name, category, price, last_updated_dt FROM t_product_item "
            "WHERE category = %s"
        )
        cursor.execute(query, (category,))

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
        category = category_data.get("category", "all")

        connection = connect_to_database()
        cursor = connection.cursor()

        items_data = fetch_items_from_database(cursor, category)

        grouped_items = group_items_by_category(items_data)

        result = {"items": grouped_items}
        return result

    finally:
        cursor.close()
        connection.close()
