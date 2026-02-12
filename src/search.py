import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция фильтрует список операций по заданной строке в описании.

    Args:
        data (list[dict]): Список словарей с операциями.
        search (str): Строка для поиска в описании операций.

    Returns:
        list[dict]: Список операций, содержащих заданную строку в описании.
    """
    pattern = re.compile(search, re.IGNORECASE)
    return [txn for txn in data if pattern.search(txn.get('description', ''))]
