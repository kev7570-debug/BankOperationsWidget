import unittest

from src.statistics import process_bank_operations


class TestBankOperations(unittest.TestCase):
    def test_process_bank_operations(self):
        # Исходные данные для тестирования
        data = [
            {'description': 'Перевод организации'},
            {'description': 'Покупка продуктов'},
            {'description': 'Перевод зарплаты'},
            {'description': 'Перевод организации'},
            {'description': 'Перевод организации'}
        ]

        # Тестирование стандартного набора данных
        categories = ['Перевод организации', 'Покупка продуктов']
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {'ПЕРЕВОД ОРГАНИЗАЦИИ': 3, 'ПОКУПКА ПРОДУКТОВ': 1})

        # Тестирование чувствительности к регистру
        categories = ['перевод организации', 'покупка продуктов']
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {'ПЕРЕВОД ОРГАНИЗАЦИИ': 3, 'ПОКУПКА ПРОДУКТОВ': 1})

        # Тестирование отсутствия совпадений
        categories = ['Отзыв средств']
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {})

        # Тестирование пустого списка данных
        result = process_bank_operations([], categories)
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()
