# import csv
#
# import pandas as pd
#
#
# def read_csv(file_path: str) -> list:
#     """
#     Читает финансовый CSV-файл и возвращает список словарей с транзакциями.
#
#     Args:
#         file_path (str): Путь к CSV-файлу.
#
#     Returns:
#         list: Список словарей с транзакциями.
#     """
#     transactions = []
#
#     with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             transactions.append(dict(row))
#
#     return transactions
#
#
# def read_excel(file_path: str) -> list:
#     """
#     Читает финансовый Excel-файл и возвращает список словарей с транзакциями.
#     Args:
#         file_path (str): Путь к Excel-файлу.
#
#     Returns:
#         list: Список словарей с транзакциями.
#     """
#     df = pd.read_excel(file_path)
#     records = df.where(df.notnull(), None).to_dict(orient='records')
#     return [record for record in records if any(record.values())]


# # src/data_reader.py
#
# import csv
# import pandas as pd
# import json
#
# def read_json(file_path: str) -> list:
#     """
#     Читает финансовый JSON-файл и возвращает список словарей с транзакциями.
#
#     Args:
#         file_path (str): Путь к JSON-файлу.
#
#     Returns:
#         list: Список словарей с транзакциями.
#     """
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return json.load(file)
#
# def read_csv(file_path: str) -> list:
#     """
#     Читает финансовый CSV-файл и возвращает список словарей с транзакциями.
#
#     Args:
#         file_path (str): Путь к CSV-файлу.
#
#     Returns:
#         list: Список словарей с транзакциями.
#     """
#     transactions = []
#     with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             transactions.append(dict(row))
#     return transactions
#
# def read_excel(file_path: str) -> list:
#     """
#     Читает финансовый Excel-файл и возвращает список словарей с транзакциями.
#
#     Args:
#         file_path (str): Путь к Excel-файлу.
#
#     Returns:
#         list: Список словарей с транзакциями.
#     """
#     df = pd.read_excel(file_path)
#     records = df.where(df.notnull(), None).to_dict(orient='records')
#     return [record for record in records if any(record.values())]


# src/data_reader.py

import csv
import json

import pandas as pd


def read_json(file_path: str) -> list:
    """
    Читает финансовый JSON-файл и возвращает список словарей с транзакциями.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        list: Список словарей с транзакциями.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv(file_path: str) -> list:
    """
    Читает финансовый CSV-файл и возвращает список словарей с транзакциями.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        list: Список словарей с транзакциями.
    """
    transactions = []
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
        # Используем ';' как разделитель полей
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # Трансформация данных
            operation_amount = {
                "amount": row.pop('amount', ''),
                "currency": {
                    "name": row.pop('currency_name', ''),
                    "code": row.pop('currency_code', '')
                }
            }
            row['operationAmount'] = operation_amount
            transactions.append(row)
    return transactions


def read_excel(file_path: str) -> list:
    """
    Читает финансовый Excel-файл и возвращает список словарей с транзакциями.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        list: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    records = df.where(df.notnull(), None).to_dict(orient='records')

    # Трансформация данных
    transformed_records = []
    for record in records:
        # Попытка принудительно перевести поля в строки
        operation_amount = {
            "amount": str(record.pop('amount', '')),
            "currency": {
                "name": str(record.pop('currency_name', '')),
                "code": str(record.pop('currency_code', ''))
            }
        }
        record['operationAmount'] = operation_amount
        # Преобразуем все поля в строки
        for key, value in record.items():
            if isinstance(value, float):
                record[key] = str(int(value)) if value.is_integer() else str(value)
        transformed_records.append(record)

    return transformed_records


def read_excel(file_path: str) -> list:
    """
    Читает финансовый Excel-файл и возвращает список словарей с транзакциями.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        list: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    records = df.where(df.notnull(), None).to_dict(orient='records')

    # Трансформация данных
    transformed_records = []
    for record in records:
        operation_amount = {
            "amount": record.pop('amount', ''),
            "currency": {
                "name": record.pop('currency_name', ''),
                "code": record.pop('currency_code', '')
            }
        }
        record['operationAmount'] = operation_amount
        transformed_records.append(record)

    return transformed_records
