# src/generators.py

def filter_by_currency(transactions: list, currency: str):
    """
    Возвращает итератор, содержащий транзакции с заданной валютой.

    Args:
        transactions (list): Список транзакций.
        currency (str): Валюта для фильтрации.

    Yields:
        dict: Транзакция с заданной валютой.
    """
    for txn in transactions:
        if txn["operationAmount"]["currency"]["code"] == currency:
            yield txn


def transaction_descriptions(transactions: list):
    """
    Генератор, возвращающий описания транзакций.

    Args:
        transactions (list): Список транзакций.

    Yields:
        str: Описание транзакции.
    """
    for txn in transactions:
        yield txn["description"]


def card_number_generator(start: int, stop: int):
    """
    Генератор, производящий номера карт в заданном диапазоне.

    Args:
        start (int): Начало диапазона.
        stop (int): Окончание диапазона.

    Yields:
        str: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for num in range(start, stop + 1):
        formatted_num = "{:016}".format(num)
        yield "{} {} {} {}".format(formatted_num[:4], formatted_num[4:8], formatted_num[8:12], formatted_num[12:])
