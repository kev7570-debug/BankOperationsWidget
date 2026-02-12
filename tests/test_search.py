import unittest

from src.search import process_bank_search


class TestSearchFunctions(unittest.TestCase):
    def test_process_bank_search(self):
        # Исходные данные для тестирования
        data = [
            {'description': 'Перевод организации'},
            {'description': 'Покупка продуктов'},
            {'description': 'Перевод зарплаты'}
        ]

        # Тестирование нахождения точного соответствия
        result = process_bank_search(data, 'организации')
        self.assertEqual(result, [{'description': 'Перевод организации'}])

        # Тестирование частичного совпадения
        result = process_bank_search(data, 'продук')
        self.assertEqual(result, [{'description': 'Покупка продуктов'}])

        # Тестирование чувствительности к регистру
        result = process_bank_search(data, 'ОРГАНИЗАЦИИ')
        self.assertEqual(result, [{'description': 'Перевод организации'}])

        # Тестирование отсутствия совпадений
        result = process_bank_search(data, 'машины')
        self.assertEqual(result, [])

        # Тестирование пустого списка данных
        result = process_bank_search([], 'любое слово')
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
