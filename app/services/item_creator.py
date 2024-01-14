from app.dao.item_dao import item_exists, update_item, create_item
from app.models import new_item_dto
from app.services.item_validation_service import ItemValidationService
from app.utils.app_error import MissingMandatoryFieldError
from app.utils.constant import PRICE_FORMATTER, CREATE_UPDATE_REQUEST_MANDATORY_FIELDS
from app.utils.error_message import INVALID_PRICE_FORMAT
from app.utils.request_validation_utils import check_mandatory_fields


def format_price(price):
    try:
        price_float = float(price)
        formatted_price = PRICE_FORMATTER.format(price_float)
        return formatted_price
    except ValueError:
        raise ValueError(INVALID_PRICE_FORMAT)


def create_or_update_item(request):
    validation_service = ItemValidationService()

    try:
        check_mandatory_fields(request, CREATE_UPDATE_REQUEST_MANDATORY_FIELDS)

        validation_service.validate_item(**request)

        new_item = new_item_dto.NewItemDto(**request)
        new_item.price = format_price(new_item.price)

        item_id = update_item(new_item) \
            if item_exists(new_item.name) \
            else create_item(new_item)

        return {'id': item_id}

    except (MissingMandatoryFieldError, ValueError, Exception) as e:
        return {'error': str(e)}
