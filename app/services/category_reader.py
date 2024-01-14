from app.dao.item_dao import get_items, get_items_by_category
from app.services.item_validation_service import ItemValidationService
from app.utils.app_error import MissingMandatoryFieldError
from app.utils.constant import ALL_CATEGORIES, PRICE_FORMATTER, SEARCH_CATEGORY_REQUEST_MANDATORY_FIELDS
from app.utils.request_validation_utils import check_mandatory_fields


def validate_input(category):
    item_validation_service = ItemValidationService()
    item_validation_service.validate_category(**category)


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


def format_price(price):
    return PRICE_FORMATTER.format(price)


def format_grouped_items(grouped_items):
    for group in grouped_items:
        group['total_price'] = format_price(group['total_price'])

    return grouped_items


def aggregate_items_by_category(request):
    try:
        check_mandatory_fields(request, SEARCH_CATEGORY_REQUEST_MANDATORY_FIELDS)

        validate_input(request)

        category = request.get("category", ALL_CATEGORIES)

        items_data = get_items() if category == ALL_CATEGORIES \
            else get_items_by_category(category)

        grouped_items = group_items_by_category(items_data)
        formatted_items = format_grouped_items(grouped_items)

        return {"items": formatted_items}

    except (MissingMandatoryFieldError, ValueError, Exception) as e:
        return {'error': str(e)}
