import unittest
from unittest.mock import patch

from app.services.category_reader import validate_input


class TestCategoryInputFunctions(unittest.TestCase):

    @patch('app.services.category_reader.ItemValidationService.validate_category')
    def test_validate_input_valid_category(self, mock_validate_category):
        category = {"category": "Electronics"}

        validate_input(category)

        mock_validate_category.assert_called_once_with(category="Electronics")

    @patch('app.services.category_reader.ItemValidationService.validate_category',
           side_effect=ValueError("Invalid category"))
    def test_validate_input_invalid_category(self, mock_validate_category):
        category = {"category": "InvalidCategory"}

        with self.assertRaises(ValueError) as context:
            validate_input(category)

        self.assertEqual(str(context.exception), "Invalid category")
        mock_validate_category.assert_called_once_with(category="InvalidCategory")

    @patch('app.services.category_reader.ItemValidationService.validate_category',
           side_effect=ValueError("Validation error"))
    def test_validate_input_validation_error(self, mock_validate_category):
        category = {"category": "A" * 51}  # Category with more than 50 characters

        with self.assertRaises(ValueError) as context:
            validate_input(category)

        self.assertEqual(str(context.exception), "Validation error")
        mock_validate_category.assert_called_once_with(category="A" * 51)
