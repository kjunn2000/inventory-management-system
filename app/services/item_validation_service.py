from app.utils.constant import MAX_NAME_LENGTH, MAX_PRICE_LENGTH, MAX_CATEGORY_LENGTH


class ItemValidationService:

    @staticmethod
    def validate_length(attribute, max_length):
        return len(attribute) <= max_length

    def validate_name(self, name):
        if not self.validate_length(name, MAX_NAME_LENGTH):
            raise ValueError(f"Name length must be at most {MAX_NAME_LENGTH} characters.")

    def validate_category(self, category):
        if not self.validate_length(category, MAX_CATEGORY_LENGTH):
            raise ValueError(f"Category length must be at most {MAX_CATEGORY_LENGTH} characters.")

    def validate_price(self, price):
        if not self.validate_length(price, MAX_PRICE_LENGTH):
            raise ValueError(f"Price length must be at most {MAX_PRICE_LENGTH} characters.")

    def validate_item(self, name, category, price):
        self.validate_name(name)
        self.validate_category(category)
        self.validate_price(price)