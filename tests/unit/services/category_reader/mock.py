def mock_format_grouped_items_return():
    return [
        {"category": "Electronics", "total_price": "499.99", "count": 1}
    ]


def mock_group_items_by_category_return():
    return [{"category": "Electronics", "total_price": 499.99, "count": 1}]


def mock_get_items_by_category_return():
    return [
        {"item_id": 1, "name": "TV", "category": "Electronics", "price": 499.99}
    ]
