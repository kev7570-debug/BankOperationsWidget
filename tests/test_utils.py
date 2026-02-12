# tests/test_utils.py

import unittest
from unittest.mock import MagicMock, patch

from src.utils import read_json


class UtilsTest(unittest.TestCase):
    @patch('src.utils.os.path.exists')
    @patch('src.utils.open')
    def test_read_json_valid(self, mock_open, mock_exists):
        # Имитация корректного файла JSON
        mock_exists.return_value = True
        mock_file = MagicMock()
        mock_file.read.return_value = """[
            {"id": 1, "state": "EXECUTED"},
            {"id": 2, "state": "CANCELED"}
        ]"""
        mock_open.return_value.__enter__.return_value = mock_file

        result = read_json('valid.json')
        self.assertEqual(len(result), 2)

    @patch('src.utils.os.path.exists')
    def test_read_json_file_not_found(self, mock_exists):
        # Имитация отсутствующего файла
        mock_exists.return_value = False
        result = read_json('missing.json')
        self.assertEqual(result, [])

    @patch('src.utils.os.path.exists')
    @patch('src.utils.open')
    def test_read_json_invalid_json(self, mock_open, mock_exists):
        # Имитация файла с некорректным JSON
        mock_exists.return_value = True
        mock_file = MagicMock()
        mock_file.read.return_value = "{invalid_json"
        mock_open.return_value.__enter__.return_value = mock_file

        result = read_json('invalid.json')
        self.assertEqual(result, [])
