from app.utils.app_error import MissingMandatoryFieldError
from app.utils.error_message import MISSING_MANDATORY_FIELD_ERROR


def check_mandatory_fields(request, mandatory_fields):
    for field in mandatory_fields:
        if field not in request or request[field] is None or not request[field]:
            raise MissingMandatoryFieldError(f"{MISSING_MANDATORY_FIELD_ERROR}{field}")
    return True
