import unittest
from unittest.mock import patch, ANY

from app.services.item_creator import create_or_update_item
from app.utils.app_error import MissingMandatoryFieldError


class TestUpdateItemToDb(unittest.TestCase):

    def setUp(self):
        self.mock_item_json = {
            "name": "TV1111",
            "category": "Home Use",
            "price": "663333.222222225"
        }

    @patch('app.services.item_creator.check_mandatory_fields')
    @patch('app.services.item_creator.format_price', return_value="10.50")
    @patch('app.services.item_creator.item_exists', return_value=True)
    @patch('app.services.item_creator.update_item', return_value=123)
    def test_update_existing_item_called(self, mock_update_item, mock_item_exists, mock_format_price,
                                         mock_check_mandatory_fields):
        new_item = self.mock_item_json

        result = create_or_update_item(new_item)

        self.assertEqual(result, {'id': 123})
        mock_update_item.assert_called_once_with(ANY)

    @patch('app.services.item_creator.check_mandatory_fields')
    @patch('app.services.item_creator.format_price', return_value="10.50")
    @patch('app.services.item_creator.item_exists', return_value=False)
    @patch('app.services.item_creator.create_item', return_value=123)
    def test_insert_new_item_called(self, mock_insert_new_item, mock_item_exists, mock_format_price,
                                    mock_check_mandatory_fields):
        new_item = self.mock_item_json

        result = create_or_update_item(new_item)

        self.assertEqual(result, {'id': 123})
        mock_insert_new_item.assert_called_once_with(ANY)

    @patch('app.services.item_creator.check_mandatory_fields')
    @patch('app.services.item_creator.ItemValidationService')
    @patch('app.services.item_creator.update_item')
    @patch('app.services.item_creator.create_item')
    def test_format_validation_failure(self, mock_create_item, mock_update_item, mock_validation_service,
                                       mock_check_mandatory_fields):
        mock_validation_service.return_value.validate_item.side_effect = ValueError("Invalid item")
        new_item = self.mock_item_json

        result = create_or_update_item(new_item)

        mock_create_item.assert_not_called()
        mock_update_item.assert_not_called()
        self.assertIn('error', result)
        self.assertEqual(result['error'], 'Invalid item')

    @patch("app.services.item_creator.ItemValidationService")
    @patch("app.services.item_creator.check_mandatory_fields")
    def test_create_or_update_item_missing_field(self, mock_check_mandatory_fields, mock_item_validation_service):
        request = {
            "name": "item_name",
            "category": "item_category",
            # "price" is missing
        }
        mock_check_mandatory_fields.side_effect = (
            MissingMandatoryFieldError("Missing or empty value in mandatory field: price"))

        result = create_or_update_item(request)

        self.assertEqual(result, {'error': 'Missing or empty value in mandatory field: price'})
