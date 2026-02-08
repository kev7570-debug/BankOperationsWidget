from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from src.data_reader import read_csv, read_excel


class TestDataReader(TestCase):

    @patch('builtins.open', new_callable=MagicMock)
    def test_read_csv_calls_open_and_dictreader(self, mock_open):
        """Проверка, что read_csv вызывает open и DictReader."""
        read_csv('some/path/to/file.csv')
        mock_open.assert_called_once_with('some/path/to/file.csv', 'r', newline='', encoding='utf-8-sig')

    @patch('pandas.read_excel', new_callable=MagicMock)
    def test_read_excel_calls_pandas_read_excel(self, mock_read_excel):
        """Проверка, что read_excel вызывает pandas.read_excel."""
        read_excel('some/path/to/file.xlsx')
        mock_read_excel.assert_called_once_with('some/path/to/file.xlsx')


if __name__ == '__main__':
    main()