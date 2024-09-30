import unittest

from unittest.mock import patch, MagicMock
from src.database import Database

class TestDatabaseConnection(unittest.TestCase):
    @patch("src.database.sqlite3.connect")
    def test_connect_to_db_success(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.side_effect = [('save',), ('character',), ('translation',)]

        db = Database()
        self.assertIsNotNone(db.conn)
        mock_connect.assert_called_once_with('gamedata.db')

if __name__ == "__main__":
    unittest.main()