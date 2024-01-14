from datetime import datetime

from app.dao.item_dao import get_items_by_dt
from app.utils.app_error import MissingMandatoryFieldError
from app.utils.constant import PRICE_FORMATTER, DATE_FORMATTER, SEARCH_ITEM_REQUEST_MANDATORY_FIELDS
from app.utils.request_validation_utils import check_mandatory_fields


def calculate_total_price(items):
    return sum(float(item.price) for item in items)


def map_items_response_dto(items_data):
    filtered_items = [
        item.to_json()
        for item in items_data
    ]
    total_price = calculate_total_price(items_data)

    return {"items": filtered_items, "total_price": PRICE_FORMATTER.format(total_price)}


def get_items_by_last_updated_dt(request):
    try:
        check_mandatory_fields(request, SEARCH_ITEM_REQUEST_MANDATORY_FIELDS)

        dt_from = datetime.strptime(request["dt_from"], DATE_FORMATTER)
        dt_to = datetime.strptime(request["dt_to"], DATE_FORMATTER)

        items_data = get_items_by_dt(dt_from, dt_to)

        return map_items_response_dto(items_data)

    except (MissingMandatoryFieldError, ValueError, Exception) as e:
        return {'error': str(e)}
