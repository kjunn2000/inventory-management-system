import unittest
from unittest.mock import patch

from app.services.item_validation_service import ItemValidationService
from app.utils.constant import MAX_NAME_LENGTH, MAX_CATEGORY_LENGTH, MAX_PRICE_LENGTH


class TestItemValidationService(unittest.TestCase):
    def setUp(self):
        self.validation_service = ItemValidationService()

    def test_validate_name_valid(self):
        name = "Product Name"
        self.assertIsNone(self.validation_service.validate_name(name))

    def test_validate_name_invalid(self):
        name = "A" * (MAX_NAME_LENGTH + 1)
        with self.assertRaises(ValueError) as context:
            self.validation_service.validate_name(name)
        expected_error_message = f"Name length must be at most {MAX_NAME_LENGTH} characters."
        self.assertEqual(str(context.exception), expected_error_message)

    def test_validate_category_valid(self):
        category = "Electronics"
        self.assertIsNone(self.validation_service.validate_category(category))

    def test_validate_category_invalid(self):
        category = "B" * (MAX_CATEGORY_LENGTH + 1)
        with self.assertRaises(ValueError) as context:
            self.validation_service.validate_category(category)
        expected_error_message = f"Category length must be at most {MAX_CATEGORY_LENGTH} characters."
        self.assertEqual(str(context.exception), expected_error_message)

    def test_validate_price_valid(self):
        price = "123.45"
        self.assertIsNone(self.validation_service.validate_price(price))

    def test_validate_price_invalid(self):
        price = "1234567890123456789.00"
        with self.assertRaises(ValueError) as context:
            self.validation_service.validate_price(price)
        expected_error_message = f"Price length must be at most {MAX_PRICE_LENGTH} characters."
        self.assertEqual(str(context.exception), expected_error_message)

    def test_validate_item_valid(self):
        name = "Product Name"
        category = "Electronics"
        price = "123.45"
        with patch.object(ItemValidationService, 'validate_name'), \
                patch.object(ItemValidationService, 'validate_category'), \
                patch.object(ItemValidationService, 'validate_price'):
            self.validation_service.validate_item(name, category, price)

    def test_validate_item_invalid(self):
        name = "A" * (MAX_NAME_LENGTH + 1)
        category = "B" * (MAX_CATEGORY_LENGTH + 1)
        price = "12345678901234567890"
        with self.assertRaises(ValueError):
            self.validation_service.validate_item(name, category, price)
