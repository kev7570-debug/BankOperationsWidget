import json
import os


def read_json(file_path):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к файлу JSON
    :return: Список словарей с данными о транзакциях или пустой список, если файл пуст или неверный
    """
    try:
        # Проверяем существование файла
        if not os.path.exists(file_path):
            print(f"Файл '{file_path}' не найден.")
            return []

        # Открываем файл с явным указанием кодировки utf-8
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()  # Убираем пробелы и символы переноса строки

            # Если файл пустой, возвращаем пустой список
            if not content:
                return []

            # Пробуем разобрать JSON
            transactions = json.loads(content)

            # Проверяем, является ли объект списком
            if isinstance(transactions, list):
                return transactions
            else:
                print(f"Ошибка: файл '{file_path}' не содержит список транзакций.")
                return []

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")  # Четкость сообщения
        return []

    except json.JSONDecodeError:
        print(f"Ошибка: некорректный формат JSON в файле '{file_path}'.")
        return []

    except Exception as e:
        print(f"Произошла ошибка при чтении файла '{file_path}': {e}")
        return []


# Пример вызова функции
file_path = r"C:\Users\User\PycharmProjects\Domashka\data\operations.json"
transactions = read_json(file_path)
print("Транзакции:", transactions)
