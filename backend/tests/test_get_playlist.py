import unittest
from unittest.mock import patch, MagicMock
import sys
import os
# Add parent directory to system path
sys.path.append(os.path.abspath('../'))
from db_utils import get_playlist, TEST_DB_NAME

class TestPlaylist(unittest.TestCase):
    @patch("db_utils.connect_to_db")
    def test_get_playlist_success(self, mock_connect_to_db):
        """Test retrieving playlist data"""
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('Inhaler', 'A Question Of You', 5), 
                                            ('Lola Young', 'Messy', 3), 
                                            ('Doechii', 'DENIAL IS A RIVER', 2), 
                                            ('Central Cee', 'GBP', 1), 
                                            ('Chappell Roan', 'Pink Pony Club', 1), 
                                            ('Chrystal', 'The Days (NOTION Remix)', 1), 
                                            ('Confidence Man & Sweely', 'All My People', 1), 
                                            ('Kendrick Lamar & SZA', 'Luther', 1), 
                                            ('Lady Gaga', 'Abracadabra', 1), 
                                            ('PAWSA & The Adventures Of Stevie V', 'Dirty Cash (Money Talks)', 1)]
        mock_db.cursor.return_value = mock_cursor
        mock_connect_to_db.return_value = mock_db

        result = get_playlist(TEST_DB_NAME)
        self.assertEqual(result, 
        [('Inhaler', 'A Question Of You', 5), 
         ('Lola Young', 'Messy', 3), 
         ('Doechii', 'DENIAL IS A RIVER', 2), 
         ('Central Cee', 'GBP', 1), 
         ('Chappell Roan', 'Pink Pony Club', 1), 
         ('Chrystal', 'The Days (NOTION Remix)', 1), 
         ('Confidence Man & Sweely', 'All My People', 1), 
         ('Kendrick Lamar & SZA', 'Luther', 1), 
         ('Lady Gaga', 'Abracadabra', 1), 
         ('PAWSA & The Adventures Of Stevie V', 'Dirty Cash (Money Talks)', 1)]
        )

if __name__ == "__main__":
    unittest.main()
