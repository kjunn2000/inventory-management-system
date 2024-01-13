import unittest
from unittest.mock import patch, MagicMock

from mysql.connector import Error

from app.utils.db_utils import connect_to_database, get_database_connection


class TestDatabaseUtils(unittest.TestCase):

    @patch('app.utils.db_utils.mysql.connector.connect', return_value=MagicMock())
    def test_connect_to_database_successful(self, mock_connect):
        with patch.dict('os.environ',
                        {'MYSQL_HOST': 'localhost', 'MYSQL_USER': 'test_user', 'MYSQL_PASSWORD': 'test_password',
                         'MYSQL_DATABASE': 'test_db'}):
            result = connect_to_database()

            mock_connect.assert_called_once_with(
                host='localhost',
                user='test_user',
                password='test_password',
                database='test_db'
            )

            self.assertIsInstance(result, MagicMock)

    @patch('app.utils.db_utils.mysql.connector.connect', side_effect=Error("Connection error"))
    def test_connect_to_database_error(self, mock_connect):
        with patch.dict('os.environ',
                        {'MYSQL_HOST': 'localhost', 'MYSQL_USER': 'test_user', 'MYSQL_PASSWORD': 'test_password',
                         'MYSQL_DATABASE': 'test_db'}):
            with self.assertRaises(Error):
                connect_to_database()

    @patch('app.utils.db_utils.connect_to_database')
    def test_get_database_connection_successful(self, mock_connect_to_database):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_to_database.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor

        with get_database_connection() as (connection, cursor):
            self.assertEqual(connection, mock_connection)
            self.assertEqual(cursor, mock_cursor)

    @patch('app.utils.db_utils.connect_to_database', side_effect=Error("Connection error"))
    def test_get_database_connection_error(self, mock_connect_to_database):
        with self.assertRaises(Error):
            with get_database_connection(): pass
