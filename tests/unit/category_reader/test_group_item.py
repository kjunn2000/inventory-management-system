import unittest
from unittest.mock import Mock

from app.services.category_reader import calculate_total_price, group_items_by_category


class TestGroupItemFunction(unittest.TestCase):

    def test_calculate_total_price_empty_list(self):
        items = []
        result = calculate_total_price(items)
        self.assertEqual(result, 0.0)

    def test_calculate_total_price_single_item(self):
        items = [Mock(price='10.50')]
        result = calculate_total_price(items)
        self.assertEqual(result, 10.50)

    def test_calculate_total_price_multiple_items(self):
        items = [Mock(price='10.50'), Mock(price='5.75'), Mock(price='20.25')]
        result = calculate_total_price(items)
        self.assertEqual(result, 36.50)

    def test_group_items_by_category_empty_list(self):
        items_data = []
        result = group_items_by_category(items_data)
        self.assertEqual(result, [])

    def test_group_items_by_category_single_item(self):
        item_mock = Mock(category='Electronics', price='10.50')
        items_data = [item_mock]
        result = group_items_by_category(items_data)
        expected_result = [{'category': 'Electronics', 'total_price': 10.50, 'count': 1}]
        self.assertEqual(result, expected_result)

    def test_group_items_by_category_multiple_items(self):
        items_data = [
            Mock(category='Electronics', price='10.50'),
            Mock(category='Furniture', price='5.75'),
            Mock(category='Electronics', price='20.25')
        ]
        result = group_items_by_category(items_data)
        expected_result = [
            {'category': 'Electronics', 'total_price': 30.75, 'count': 2},
            {'category': 'Furniture', 'total_price': 5.75, 'count': 1}
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
