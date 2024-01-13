import unittest
from unittest.mock import patch, ANY

from app.services.item_creator import create_or_update_item


class TestUpdateItemToDb(unittest.TestCase):

    def setUp(self):
        self.mock_item_json = {
            "name": "TV1111",
            "category": "Home Use",
            "price": "663333.222222225"
        }

    @patch('app.services.item_creator.format_price', return_value="10.50")
    @patch('app.services.item_creator.item_exists', return_value=True)
    @patch('app.services.item_creator.update_item', return_value=123)
    def test_update_existing_item_called(self, mock_update_item, mock_item_exists, mock_format_price):
        new_item = self.mock_item_json
        result = create_or_update_item(new_item)

        self.assertEqual(result, {'id': 123})
        mock_update_item.assert_called_once_with(ANY)

    @patch('app.services.item_creator.format_price', return_value="10.50")
    @patch('app.services.item_creator.item_exists', return_value=False)
    @patch('app.services.item_creator.create_item', return_value=123)
    def test_insert_new_item_called(self, mock_insert_new_item, mock_item_exists, mock_format_price):
        new_item = self.mock_item_json
        result = create_or_update_item(new_item)

        self.assertEqual(result, {'id': 123})
        mock_insert_new_item.assert_called_once_with(ANY)

    @patch('app.services.item_creator.ItemValidationService')
    @patch('app.services.item_creator.update_item')
    @patch('app.services.item_creator.create_item')
    def test_validation_failure(self, mock_create_item, mock_update_item, mock_validation_service):
        mock_validation_service.return_value.validate_item.side_effect = ValueError("Invalid item")

        request_data = {
            'name': 'Sample Item',
            'price': '50.00',
        }

        result = create_or_update_item(request_data)

        mock_create_item.assert_not_called()
        mock_update_item.assert_not_called()

        self.assertIn('error', result)
        self.assertEqual(result['error'], 'Invalid item')


if __name__ == '__main__':
    unittest.main()
