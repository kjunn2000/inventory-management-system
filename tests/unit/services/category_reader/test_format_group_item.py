import unittest

from app.services.category_reader import format_price, format_grouped_items


class TestFormatGroupItem(unittest.TestCase):

    def test_format_price_integer(self):
        result = format_price(10)
        self.assertEqual(result, "10.00")

    def test_format_price_float(self):
        result = format_price(15.75)
        self.assertEqual(result, "15.75")

    def test_format_price_long_decimal(self):
        result = format_price(30.75555555555555)
        self.assertEqual(result, "30.76")

    def test_format_grouped_items_empty_list(self):
        grouped_items = []
        result = format_grouped_items(grouped_items)
        self.assertEqual(result, [])

    def test_format_grouped_items_single_item(self):
        grouped_items = [{'category': 'Electronics', 'total_price': 10.50, 'count': 1}]
        result = format_grouped_items(grouped_items)
        expected_result = [{'category': 'Electronics', 'total_price': "10.50", 'count': 1}]
        self.assertEqual(result, expected_result)

    def test_format_grouped_items_multiple_items(self):
        grouped_items = [
            {'category': 'Electronics', 'total_price': 30.75, 'count': 2},
            {'category': 'Furniture', 'total_price': 5.75, 'count': 1},
            {'category': 'Clothing', 'total_price': 30.75555555555555, 'count': 3}
        ]
        result = format_grouped_items(grouped_items)
        expected_result = [
            {'category': 'Electronics', 'total_price': "30.75", 'count': 2},
            {'category': 'Furniture', 'total_price': "5.75", 'count': 1},
            {'category': 'Clothing', 'total_price': "30.76", 'count': 3}
        ]
        self.assertEqual(result, expected_result)
