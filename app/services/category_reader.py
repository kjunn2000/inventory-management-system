from app.dao.item_dao import get_items, get_items_by_category
from app.services.item_validation_service import ItemValidationService
from app.utils.constant import ALL_CATEGORIES, PRICE_FORMATTER


def validate_input(category):
    item_validation_service = ItemValidationService()
    item_validation_service.validate_category(**category)


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


def format_price(price):
    return PRICE_FORMATTER.format(price)


def format_grouped_items(grouped_items):
    for group in grouped_items:
        group['total_price'] = format_price(group['total_price'])

    return grouped_items


def aggregate_items_by_category(category_data):
    try:
        validate_input(category_data)

        category = category_data.get("category", ALL_CATEGORIES)

        items_data = get_items() if category == ALL_CATEGORIES \
            else get_items_by_category(category)

        grouped_items = group_items_by_category(items_data)
        formatted_items = format_grouped_items(grouped_items)

        return {"items": formatted_items}

    except (Exception, ValueError) as e:
        return {'error': str(e)}
