from datetime import datetime

from app.dao.item_dao import get_items_by_dt
from app.utils.constant import PRICE_FORMATTER, DATE_FORMATTER


def calculate_total_price(items):
    return sum(float(item.price) for item in items)


def map_items_response_dto(items_data):
    filtered_items = [
        item.to_json()
        for item in items_data
    ]
    total_price = calculate_total_price(items_data)

    return {"items": filtered_items, "total_price": PRICE_FORMATTER.format(total_price)}


def get_items_by_last_updated_dt(date_range):
    try:
        dt_from = datetime.strptime(date_range["dt_from"], DATE_FORMATTER)
        dt_to = datetime.strptime(date_range["dt_to"], DATE_FORMATTER)

        items_data = get_items_by_dt(dt_from, dt_to)

        return map_items_response_dto(items_data)

    except (Exception, ValueError) as e:
        return {'error': str(e)}
