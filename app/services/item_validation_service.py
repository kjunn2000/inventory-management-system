from app.utils.constant import MAX_NAME_LENGTH, MAX_CATEGORY_LENGTH, MAX_PRICE_LENGTH
from app.utils.error_message import INVALID_NAME_LENGTH, INVALID_CATEGORY_LENGTH, INVALID_PRICE_LENGTH


class ItemValidationService:

    @staticmethod
    def validate_length(attribute, max_length, error_message):
        if not len(attribute) <= max_length:
            raise ValueError(error_message)

    def validate_name(self, name):
        self.validate_length(name, MAX_NAME_LENGTH, INVALID_NAME_LENGTH)

    def validate_category(self, category):
        self.validate_length(category, MAX_CATEGORY_LENGTH, INVALID_CATEGORY_LENGTH)

    def validate_price(self, price):
        self.validate_length(price, MAX_PRICE_LENGTH, INVALID_PRICE_LENGTH)

    def validate_item(self, name, category, price):
        self.validate_name(name)
        self.validate_category(category)
        self.validate_price(price)
