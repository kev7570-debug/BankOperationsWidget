from collections import Counter


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция группирует операции по заданным категориям и возвращает их количество.

    Args:
        data (list[dict]): Список словарей с операциями.
        categories (list): Список категорий для подсчета.

    Returns:
        dict: Словарь, где ключи — категории, а значения — количество операций.
    """
    counts = Counter()
    for txn in data:
        category = txn.get('description', '').upper()
        if category in map(str.upper, categories):
            counts[category] += 1
    return dict(counts)
