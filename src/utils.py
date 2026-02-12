import json
import logging
import os

# Создаём логгер для модуля utils
logger_utils = logging.getLogger(__name__)  # Имя логгера будет совпадать с именем модуля
logger_utils.setLevel(logging.DEBUG)

# Создаём обработчик для записи логов в файл
logs_folder = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(logs_folder, exist_ok=True)
log_file_path = os.path.join(logs_folder, 'utils.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Устанавливаем форматер для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger_utils.addHandler(file_handler)


def read_json(file_path):
    """
    Читает JSON-файл и возвращает список словарей с данными о финансовых транзакциях.

    :param file_path: Путь к файлу JSON
    :return: Список словарей с данными о транзакциях или пустой список, если файл пуст или неверный
    """
    logger_utils.info(f"Начинаем чтение файла {file_path}")

    try:
        # Проверяем существование файла
        if not os.path.exists(file_path):
            logger_utils.error(f"Файл '{file_path}' не найден.")
            return []

        # Открываем файл с явным указанием кодировки utf-8
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()  # Убираем пробелы и символы переноса строки

            # Если файл пустой, возвращаем пустой список
            if not content:
                logger_utils.warning(f"Файл '{file_path}' пуст.")
                return []

            # Пробуем разобрать JSON
            transactions = json.loads(content)

            # Проверяем, является ли объект списком
            if isinstance(transactions, list):
                logger_utils.info(f"Успешно прочитано {len(transactions)} транзакций из файла {file_path}")
                return transactions
            else:
                logger_utils.error(f"Ошибка: файл '{file_path}' не содержит список транзакций.")
                return []

    except FileNotFoundError:
        logger_utils.error(f"Файл '{file_path}' не найден.")
        return []

    except json.JSONDecodeError:
        logger_utils.error(f"Ошибка: некорректный формат JSON в файле '{file_path}'.")
        return []

    except Exception as e:
        logger_utils.exception(f"Произошла ошибка при чтении файла '{file_path}': {e}")
        return []


# Пример вызова функции
file_path = r"C:\Users\User\PycharmProjects\Domashka\data\operations.json"
transactions = read_json(file_path)
print("Транзакции:", transactions)
