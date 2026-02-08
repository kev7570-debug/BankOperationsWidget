import csv

import pandas as pd


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
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(dict(row))

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
    return [record for record in records if any(record.values())]
