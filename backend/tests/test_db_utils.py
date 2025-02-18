import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from dotenv import load_dotenv
# Add parent directory to system path
sys.path.append(os.path.abspath('../'))
from db_utils import connect_to_db, TEST_DB_NAME


load_dotenv()  # Load variables from .env file


class TestDatabaseConnection(unittest.TestCase):
    @patch("mysql.connector.connect")
    def test_connect_to_db_success(self, mock_connect):
        """Test successful DB connection"""
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        connection = connect_to_db(TEST_DB_NAME)
        self.assertIsNotNone(connection)
        mock_connect.assert_called_with(
            host= os.getenv('HOST'),
            user= os.getenv('USER'),
            password= os.getenv('PASSWORD'),
            database=TEST_DB_NAME,
            auth_plugin="mysql_native_password"
        )

    @patch("mysql.connector.connect", side_effect=Exception("Connection error"))
    def test_connect_to_db_failure(self, mock_connect):
        """Test database connection failure"""
        with self.assertRaises(Exception) as context:
            connect_to_db("test_db")
        self.assertIn("Connection error", str(context.exception))

if __name__ == "__main__":
    unittest.main()