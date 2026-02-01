import unittest
from unittest.mock import MagicMock, patch

import requests  # Добавляем импорт модуля requests

from src.external_api import convert_to_rubles


class ExternalAPITest(unittest.TestCase):
    @patch('src.external_api.requests.get')
    def test_convert_to_rubles_rub(self, mock_get):
        # Транзакция в рублях
        transaction = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'RUB'}
            }
        }
        result = convert_to_rubles(transaction)
        self.assertEqual(result, 100.0)

    @patch('src.external_api.requests.get')
    def test_convert_to_rubles_usd(self, mock_get):
        # Эмуляция успешного ответа от API
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'RUB': 70}}  # Курс USD-RUB равен 70
        mock_get.return_value = mock_response

        # Транзакция в долларах
        transaction = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'USD'}
            }
        }
        result = convert_to_rubles(transaction)
        self.assertEqual(result, 7000.0)

    @patch('src.external_api.requests.get')
    def test_convert_to_rubles_http_error(self, mock_get):
        # Эмуляция ошибки 403
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()
        mock_get.return_value = mock_response

        # Транзакция в евро
        transaction = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'EUR'}
            }
        }
        result = convert_to_rubles(transaction)
        self.assertIsNone(result)
