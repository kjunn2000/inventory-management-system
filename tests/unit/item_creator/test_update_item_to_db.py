import unittest
from unittest.mock import patch, ANY

from app.services.item_creator import create_or_update_item
from scripts.mock import getMockItemJson


class TestUpdateItemToDb(unittest.TestCase):

    @patch('app.services.item_creator.format_price', return_value="10.50")
    @patch('app.services.item_creator.item_exists', return_value=True)
    @patch('app.services.item_creator.update_existing_item', return_value=123)
    def test_update_existing_item_called(self, mock_update_existing_item, mock_item_exists, mock_format_price):
        new_item = getMockItemJson()
        create_or_update_item(new_item)
        mock_update_existing_item.assert_called_once_with(ANY)

    @patch('app.services.item_creator.format_price', return_value="10.50")
    @patch('app.services.item_creator.item_exists', return_value=False)
    @patch('app.services.item_creator.insert_new_item', return_value=123)
    def test_insert_new_item_called(self, mock_insert_new_item, mock_item_exists, mock_format_price):
        new_item = getMockItemJson()
        create_or_update_item(new_item)
        mock_insert_new_item.assert_called_once_with(ANY)


if __name__ == '__main__':
    unittest.main()
