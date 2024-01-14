import unittest
from unittest.mock import patch, Mock

from app.dao.item_dao import (
    item_exists,
    update_item,
    create_item,
    get_items,
    get_items_by_dt,
    get_items_by_category,
)
from app.models.item import Item


class TestItemDAO(unittest.TestCase):

    def setUp(self):
        self.mock_cursor = Mock()

    @patch("app.dao.item_dao.get_database_connection")
    def test_item_exists(self, mock_get_database_connection):
        mock_get_database_connection.return_value.__enter__.return_value = (None, self.mock_cursor)
        self.mock_cursor.fetchone.return_value = (1,)

        result = item_exists("test_item")

        self.assertTrue(result)

    @patch("app.dao.item_dao.get_database_connection")
    def test_item_not_exists(self, mock_get_database_connection):
        mock_get_database_connection.return_value.__enter__.return_value = (None, self.mock_cursor)
        self.mock_cursor.fetchone.return_value = None

        result = item_exists("test_item")

        self.assertFalse(result)

    @patch("app.dao.item_dao.get_database_connection")
    def test_update_item(self, mock_get_database_connection):
        mock_connection = Mock()
        mock_get_database_connection.return_value.__enter__.return_value = (mock_connection, self.mock_cursor)
        self.mock_cursor.fetchone.return_value = (1,)
        new_item = Mock(name="test_item", category="test_category", price=10)

        result = update_item(new_item)

        self.assertEqual(result, 1)

    @patch("app.dao.item_dao.get_database_connection")
    def test_create_item(self, mock_get_database_connection):
        mock_connection = Mock()
        mock_get_database_connection.return_value.__enter__.return_value = (mock_connection, self.mock_cursor)
        self.mock_cursor.lastrowid = 123
        new_item = Mock(name="test_item", category="test_category", price=10)

        result = create_item(new_item)

        self.assertEqual(result, 123)

    @patch("app.dao.item_dao.get_database_connection")
    def test_get_items(self, mock_get_database_connection):
        mock_connection = Mock()
        mock_get_database_connection.return_value.__enter__.return_value = (mock_connection, self.mock_cursor)
        self.mock_cursor.fetchall.return_value = [(1, "item1", "category1", 10, "2022-01-01")]

        result = get_items()

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Item)

    @patch("app.dao.item_dao.get_database_connection")
    def test_get_items_by_dt(self, mock_get_database_connection):
        mock_connection = Mock()
        mock_get_database_connection.return_value.__enter__.return_value = (mock_connection, self.mock_cursor)
        self.mock_cursor.fetchall.return_value = [(1, "item1", "category1", 10, "2022-01-01")]

        result = get_items_by_dt("2022-01-01", "2022-01-02")

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Item)

    @patch("app.dao.item_dao.get_database_connection")
    def test_get_items_by_category(self, mock_get_database_connection):
        mock_connection = Mock()
        mock_get_database_connection.return_value.__enter__.return_value = (mock_connection, self.mock_cursor)
        self.mock_cursor.fetchall.return_value = [(1, "item1", "category1", 10, "2022-01-01")]

        result = get_items_by_category("category1")

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], Item)
