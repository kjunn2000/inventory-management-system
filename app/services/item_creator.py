from mysql.connector import Error

from app.dao.item_dao import item_exists, update_item, create_item
from app.models import new_item_dto
from app.services.item_validation_service import ItemValidationService


def format_price(price):
    try:
        price_float = float(price)
        formatted_price = "{:.2f}".format(price_float)
        return formatted_price
    except ValueError:
        raise ValueError("Invalid price format")


def create_or_update_item(request):
    validation_service = ItemValidationService()

    try:
        validation_service.validate_item(**request)

        new_item = new_item_dto.NewItemDto(**request)
        new_item.price = format_price(new_item.price)

        item_id = update_item(new_item) \
            if item_exists(new_item.name) \
            else create_item(new_item)

        return {'id': item_id}

    except (Error, ValueError) as e:
        return {'error': str(e)}
