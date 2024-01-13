import unittest

from app.services.item_creator import format_price


class TestFormatPrice(unittest.TestCase):

    def test_format_price_valid(self):
        result = format_price("10.5")
        self.assertEqual(result, "10.50")

    def test_format_price_invalid(self):
        with self.assertRaises(ValueError):
            format_price("invalid_price")

    def test_format_price_zero(self):
        result = format_price("0")
        self.assertEqual(result, "0.00")

    def test_format_price_negative(self):
        result = format_price("-15.75")
        self.assertEqual(result, "-15.75")

    def test_over_decimal_place_limit(self):
        result = format_price("15.75111111111")
        self.assertEqual(result, "15.75")
