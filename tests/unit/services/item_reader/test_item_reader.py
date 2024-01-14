from datetime import datetime
from unittest import TestCase
from unittest.mock import patch, Mock

from app.services.item_reader import get_items_by_last_updated_dt, calculate_total_price, map_items_response_dto
from app.utils.app_error import MissingMandatoryFieldError


class TestItemReader(TestCase):

    def setUp(self):
        self.mock_items_data = [
            {'id': 1, 'name': 'TV', 'category': 'Electronics', 'price': 599.99,
             'last_updated_dt': '2024-01-05 12:30:00'},
            {'id': 2, 'name': 'Bookshelf', 'category': 'Furniture', 'price': 149.99,
             'last_updated_dt': '2024-01-10 15:45:00'},
        ]

        self.expected_response = [
            {'id': 1, 'name': 'TV', 'category': 'Electronics', 'price': 599.99,
             'last_updated_dt': '2024-01-05 12:30:00'},
            {'id': 2, 'name': 'Bookshelf', 'category': 'Furniture', 'price': 149.99,
             'last_updated_dt': '2024-01-10 15:45:00'},
        ]

    @patch("app.services.item_reader.check_mandatory_fields")
    def test_input_dt_invalid(self, mock_check_mandatory_fields):
        input_data = {
            "dt_from": "2024-01-01",
            "dt_to": "2024-01-30"
        }

        response = get_items_by_last_updated_dt(input_data)

        expected_error_message = {
            "error": "time data '2024-01-01' does not match format '%Y-%m-%d %H:%M:%S'"
        }
        self.assertEqual(response, expected_error_message)

    @patch("app.services.item_reader.check_mandatory_fields")
    def test_get_items_by_last_updated_dt_missing_field(self, mock_check_mandatory_fields):
        request = {
            "dt_from": "2022-01-01",
            # "dt_to" is missing
        }
        mock_check_mandatory_fields.side_effect = MissingMandatoryFieldError(
            "Missing or empty value in mandatory field: dt_to")

        result = get_items_by_last_updated_dt(request)

        self.assertEqual(result, {'error': 'Missing or empty value in mandatory field: dt_to'})

    @patch("app.services.item_reader.check_mandatory_fields")
    @patch('app.services.item_reader.get_items_by_dt')
    @patch('app.services.item_reader.map_items_response_dto')
    def test_retrieve_items_with_total_price_success(self, mock_map_items_response_dto, mock_get_items_by_dt,
                                                     mock_check_mandatory_fields):
        input_data = {
            "dt_from": "2024-01-01 00:00:00",
            "dt_to": "2024-01-31 23:59:59"
        }
        mock_get_items_by_dt.return_value = self.mock_items_data
        mock_map_items_response_dto.return_value = self.expected_response

        result = get_items_by_last_updated_dt(input_data)

        mock_get_items_by_dt.assert_called_once_with(datetime(2024, 1, 1, 0, 0),
                                                     datetime(2024, 1, 31, 23, 59, 59))
        mock_map_items_response_dto.assert_called_once_with(self.mock_items_data)
        self.assertEqual(result, self.expected_response)

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

    @patch('app.services.item_reader.calculate_total_price', return_value=0.00)
    def test_map_items_response_dto_empty_list(self, mock_calculate_total_price):
        items_data = []

        result = map_items_response_dto(items_data)

        expected_result = {"items": [], "total_price": "0.00"}
        self.assertEqual(result, expected_result)
        mock_calculate_total_price.assert_called_once_with(items_data)

    @patch('app.services.item_reader.calculate_total_price', return_value=10.50)
    def test_map_items_response_dto_single_item(self, mock_calculate_total_price):
        items_data = [Mock(to_json=lambda: {'id': 1, 'price': '10.50'})]

        result = map_items_response_dto(items_data)

        expected_result = {"items": [{'id': 1, 'price': '10.50'}], "total_price": "10.50"}
        self.assertEqual(result, expected_result)
        mock_calculate_total_price.assert_called_once_with(items_data)

    @patch('app.services.item_reader.calculate_total_price', return_value=36.50)
    def test_map_items_response_dto_multiple_items(self, mock_calculate_total_price):
        items_data = [
            Mock(to_json=lambda: {'id': 1, 'price': '10.50'}),
            Mock(to_json=lambda: {'id': 2, 'price': '5.75'}),
            Mock(to_json=lambda: {'id': 3, 'price': '20.25'})
        ]

        result = map_items_response_dto(items_data)

        expected_result = {
            "items": [{'id': 1, 'price': '10.50'}, {'id': 2, 'price': '5.75'}, {'id': 3, 'price': '20.25'}],
            "total_price": "36.50"
        }
        self.assertEqual(result, expected_result)
        mock_calculate_total_price.assert_called_once_with(items_data)
