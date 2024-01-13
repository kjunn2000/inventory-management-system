import unittest
from unittest.mock import patch

from app.services.category_reader import aggregate_items_by_category, ALL_CATEGORIES


class TestAggregateItemsFunction(unittest.TestCase):

    @patch('app.services.category_reader.validate_input', return_value=None)
    @patch('app.services.category_reader.get_items', return_value=[{"item_id": 1, "name": "TV", "price": 499.99}])
    @patch('app.services.category_reader.group_items_by_category',
           return_value=[{"category": "Electronics", "total_price": 499.99, "count": 1}])
    @patch('app.services.category_reader.format_grouped_items',
           return_value=[{"category": "Electronics", "total_price": "499.99", "count": 1}])
    def test_get_aggregate_items_success(self, mock_format_grouped_items, mock_group_items_by_category,
                                         mock_get_items, mock_validate_input):
        category_data = {"category": "Electronics"}

        result = aggregate_items_by_category(category_data)

        self.assertEqual(result, {"items": [{"category": "Electronics", "total_price": "499.99", "count": 1}]})

    @patch('app.services.category_reader.validate_input')
    @patch('app.services.category_reader.get_items')
    @patch('app.services.category_reader.group_items_by_category')
    @patch('app.services.category_reader.format_grouped_items')
    def test_aggregate_items_by_category_all_categories(self, mock_format_grouped_items,
                                                        mock_group_items_by_category,
                                                        mock_get_items,
                                                        mock_validate_input):
        category = {"category": ALL_CATEGORIES}

        aggregate_items_by_category(category)

        mock_validate_input.assert_called_once_with(category)
        mock_get_items.assert_called_once()
        mock_group_items_by_category.assert_called_once_with(mock_get_items.return_value)
        mock_format_grouped_items.assert_called_once_with(mock_group_items_by_category.return_value)

    @patch('app.services.category_reader.validate_input')
    @patch('app.services.category_reader.get_items_by_category')
    @patch('app.services.category_reader.group_items_by_category')
    @patch('app.services.category_reader.format_grouped_items')
    def test_aggregate_items_by_category_specific_category(self, mock_format_grouped_items,
                                                           mock_group_items_by_category, mock_get_items_by_category,
                                                           mock_validate_input):
        category = {"category": "Electronics"}

        aggregate_items_by_category(category)

        mock_validate_input.assert_called_once_with(category)
        mock_get_items_by_category.assert_called_once_with("Electronics")
        mock_group_items_by_category.assert_called_once_with(mock_get_items_by_category.return_value)
        mock_format_grouped_items.assert_called_once_with(mock_group_items_by_category.return_value)

    @patch('app.services.category_reader.validate_input', side_effect=ValueError("Invalid category"))
    def test_aggregate_items_by_category_invalid_category(self, mock_validate_input):
        category = {"category": "InvalidCategory"}

        result = aggregate_items_by_category(category)

        mock_validate_input.assert_called_once_with(category)
        self.assertEqual(result, {'error': "Invalid category"})

    @patch('app.services.category_reader.validate_input')
    @patch('app.services.category_reader.get_items', side_effect=ValueError("Error fetching items"))
    def test_aggregate_items_by_category_validation_and_fetch_error(self, mock_get_items, mock_validate_input):
        category = {"category": ALL_CATEGORIES}

        result = aggregate_items_by_category(category)

        mock_validate_input.assert_called_once_with(category)
        mock_get_items.assert_called_once()
        self.assertEqual(result, {'error': "Error fetching items"})


if __name__ == '__main__':
    unittest.main()
